"""Closed scheduling and cached-model use retargeting for func_15031FC8."""

FLAGS, OUTER_BRANCH, MODEL_COPY = 19, 20, 21
NESTED_CONSTANT, NODE_HOME, CASE99 = 302, 305, 322
MODEL_USES = {193:0x1481000F,232:0x14810017,269:0x14810011,968:0x14810005}


def is_branch(word):
    opcode = word >> 26
    return opcode in (1,4,5,6,7,20,21,22,23) or opcode == 17 and word >> 21 & 31 == 8


def normalize_words(words):
    if len(words) != 1148:
        raise ValueError('attachment-selection schedule extent changed')
    anchors = {FLAGS:0x01E05025,OUTER_BRANCH:0x1020006C,MODEL_COPY:0x00602025,
        NESTED_CONSTANT:0x240B0015,NODE_HOME:0x8FAE0048,CASE99:0x244FFFEC,CASE99-1:0x24060002,
        **MODEL_USES}
    if any(words[index] != expected for index,expected in anchors.items()):
        raise ValueError('attachment-selection schedule topology changed')
    uses = {index for index,word in enumerate(words[:1080])
        if is_branch(word) and (word >> 21 & 31 == 4 or word >> 26 in (4,5,20,21) and word >> 16 & 31 == 4)}
    if uses != MODEL_USES.keys():
        raise ValueError('attachment-selection cached-model uses changed')
    # Relocate existing instructions, then derive all affected local branches.
    tokens = []
    for index in range(len(words)):
        if index == MODEL_COPY:
            continue
        if index == CASE99:
            tokens.append(NODE_HOME)
        tokens.append({FLAGS:OUTER_BRANCH,OUTER_BRANCH:FLAGS,
            NESTED_CONSTANT:MODEL_COPY,NODE_HOME:NESTED_CONSTANT}.get(index,index))
    if sorted(tokens) != list(range(len(words))):
        raise ValueError('attachment-selection instruction permutation changed')
    positions = {old:new for new,old in enumerate(tokens)}
    # The case entry must execute its relocated node load before the old cursor.
    labels = {**positions,CASE99:positions[NODE_HOME]}
    normalized, branches = [], []
    for new,old in enumerate(tokens):
        word = words[old]
        if is_branch(word):
            displacement = word & 65535
            displacement -= 65536 if displacement & 0x8000 else 0
            target = old+1+displacement
            if target not in labels or target == MODEL_COPY:
                raise ValueError('attachment-selection branch target changed')
            delta = labels[target]-new-1
            if not -32768 <= delta <= 32767:
                raise ValueError('attachment-selection branch range changed')
            if old in MODEL_USES:
                word = word & ~(31 << 21) | 3 << 21
            word = word & 0xFFFF0000 | delta & 65535
            branches.append(dict(source=old,target=target,output=new,output_target=labels[target]))
        normalized.append(word)
    return dict(words=normalized,tokens=tokens,positions=positions,labels=labels,branches=branches)


def emitted_token(source):
    return {FLAGS:OUTER_BRANCH,OUTER_BRANCH:FLAGS,NESTED_CONSTANT:MODEL_COPY,
        NODE_HOME:NESTED_CONSTANT}.get(source,source)
