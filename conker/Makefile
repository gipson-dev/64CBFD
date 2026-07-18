BASENAME := conker

BUILD_DIR = build
VERSION   := us

### Split configuration

OFFSETS_LENGTH      := 2048
TEXT_SECTION_LENGTH := 1335000
DATA_SECTION_LENGTH := 92000

### Version differences

ifeq ($(VERSION),us)
SRC_DIR  := src
else
ifeq ($(VERSION),eu)
SRC_DIR := src_eu
else
ifeq ($(VERSION),ects)
SRC_DIR := src_ects
else
SRC_DIR := src_debug
OFFSETS_LENGTH      := 2112
TEXT_SECTION_LENGTH := 1380000
COMPRESS_DIR_ARGS   := --num-offsets 528 --total-size 1380000
endif
endif
endif

### Directories

ASM_DIRS  = asm \
            asm/libultra asm/libultra/audio asm/libultra/gu asm/libultra/io asm/libultra/libc asm/libultra/os \
			asm/data asm/data/init asm/data/init/data asm/data/game asm/data/libultra

BIN_DIRS  = assets

SPLIT_DIR := $(BUILD_DIR)/split

DEBUGGER_SRC_DIRS := $(SRC_DIR)/debugger $(SRC_DIR)/debugger/data
INIT_SRC_DIRS     := $(SRC_DIR)/init $(SRC_DIR)/init/data
GAME_SRC_DIRS     := $(SRC_DIR)/game $(SRC_DIR)/game/data $(SRC_DIR)/game/done
LIBULTRA_SRC_DIRS := $(SRC_DIR)/libultra $(SRC_DIR)/libultra/audio $(SRC_DIR)/libultra/gu \
            				 $(SRC_DIR)/libultra/io $(SRC_DIR)/libultra/libc $(SRC_DIR)/libultra/os

SRC_DIRS := $(SRC_DIR) \
						$(DEBUGGER_SRC_DIRS) \
						$(INIT_SRC_DIRS) \
						$(GAME_SRC_DIRS) \
						$(LIBULTRA_SRC_DIRS)


S_FILES   = $(foreach dir,$(ASM_DIRS),$(wildcard $(dir)/*.s))
S_FILES   := $(filter-out asm/142560.s asm/179F30.s asm/B3020.s asm/1C2C60.s \
                         asm/1BA1D0.s asm/20AE20.s asm/1E73B0.s asm/49D30.s asm/1FA770.s \
                         asm/1F4650.s asm/11C2B0.s asm/71820.s asm/17CAF0.s asm/1D6E80.s \
                         asm/5D2C0.s asm/1CC440.s asm/58F80.s asm/185560.s asm/133190.s \
                         asm/176A00.s asm/18A8F0.s asm/13D350.s asm/1D92F0.s asm/1B1600.s \
                         asm/AEB40.s,$(S_FILES))
S_FILES   += src/game/generated_jlabels.s
C_FILES   = $(foreach dir,$(SRC_DIRS),$(wildcard $(dir)/*.c))
H_FILES   = $(foreach dir,$(SRC_DIRS),$(wildcard $(dir)/*.h))
BIN_FILES = $(foreach dir,$(BIN_DIRS),$(wildcard $(dir)/*.bin))

O_FILES := $(foreach file,$(S_FILES),$(BUILD_DIR)/$(file:.s=.s.o)) \
           $(foreach file,$(C_FILES),$(BUILD_DIR)/$(file:.c=.c.o)) \
           $(foreach file,$(BIN_FILES),$(BUILD_DIR)/$(file:.bin=.bin.o))

TARGET = $(BUILD_DIR)/$(BASENAME).$(VERSION)

LD_SCRIPT = $(BASENAME).ld

CC     := ../ido/ido5.3_recomp/cc

CROSS   = mips-linux-gnu-
AS      = $(CROSS)as
CPP     = cpp
LD      = $(CROSS)ld
OBJDUMP = $(CROSS)objdump
OBJCOPY = $(CROSS)objcopy
PYTHON  = python3

RZIP    := $(PYTHON) ../tools/rarezip.py
RZIPDIR := $(PYTHON) ../tools/compress_dir.py
SPLIT := split -b 4096 -d --additional-suffix=.bin --suffix-length=4

OPT_FLAGS := -O2 -g3
MIPSBIT := -mips2 -o32

ASM_PROCESSOR_DIR := ../tools/asm-processor

# Target version differences

ifeq ($(VERSION),ects)
TARGET_GAME_BIN = $(TARGET).game.bin
TARGET_ROOT_GAME_BIN = ../assets/game.$(VERSION).bin
else
TARGET_GAME_BIN = $(TARGET).game.rzip.bin
TARGET_ROOT_GAME_BIN = ../assets/game.$(VERSION).rzip.bin
endif

# Files requiring pre/post-processing
GREP := grep -rl
GLOBAL_ASM_C_FILES := $(shell $(GREP) GLOBAL_ASM $(SRC_DIR) </dev/null)
GLOBAL_ASM_O_FILES := $(foreach file,$(GLOBAL_ASM_C_FILES),$(BUILD_DIR)/$(file:.c=.c.o))

INCLUDE_CFLAGS := -I . -I include -I include/2.0L -I include/2.0L/PR -I include/libc -I src/libultra/os -I src/libultra/audio -I src/libultra/io

ASFLAGS = -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include

CFLAGS := -G 0 -Xfullwarn -Xcpluscomm -signed -nostdinc -non_shared -Wab,-r4300_mul
CFLAGS += -D_LANGUAGE_C -D_FINALROM -DF3DEX_GBI_2 -D_MIPS_SZLONG=32
# ignore compiler warnings about anonymous structs
CFLAGS += -woff 649,838
CFLAGS += $(INCLUDE_CFLAGS)

LDFLAGS = -T $(BUILD_DIR)/$(LD_SCRIPT) -Map $(TARGET).map -T undefined_syms.$(VERSION).txt -T undefined_funcs.$(VERSION).txt -T undefined_syms_auto.txt -T undefined_funcs_auto.txt --no-check-sections --no-warn-mismatch

### Overrides

$(BUILD_DIR)/$(SRC_DIR)/libultra/audio/%.o: OPT_FLAGS := -g

# TODO: blindly move all of this into libultra/audio
$(BUILD_DIR)/$(SRC_DIR)/init_17F10.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_17F80.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_19B50.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_1AAE0.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_1C060.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_1E480.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_1E4A0.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_1E530.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_1FB40.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_20000.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_214F0.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_22040.c.o: OPT_FLAGS := -g
$(BUILD_DIR)/$(SRC_DIR)/init_22460.c.o: OPT_FLAGS := -g


$(BUILD_DIR)/$(SRC_DIR)/libultra/io/ai.c.o: OPT_FLAGS := -O1
$(BUILD_DIR)/$(SRC_DIR)/libultra/io/aigetstat.c.o: OPT_FLAGS := -O1
$(BUILD_DIR)/$(SRC_DIR)/libultra/io/aisetfreq.c.o: OPT_FLAGS := -O1

$(BUILD_DIR)/$(SRC_DIR)/libultra/os/getthreadpri.c.o: OPT_FLAGS := -O1

$(BUILD_DIR)/$(SRC_DIR)/init_3920.c.o: OPT_FLAGS := -O2

# uses native 64-bit ops (func_150ADA20's PRNG step) - needs MIPS III, not
# the project-wide default MIPS II, or IDO emits __ll_lshift/__ull_rshift
# software-emulation calls instead of dsll/dsrl/daddiu/ld/sd.
$(BUILD_DIR)/$(SRC_DIR)/game_DAE50.c.o: MIPSBIT := -mips3

# $(BUILD_DIR)/$(SRC_DIR)/init_B1B0.o: OPT_FLAGS := -O2

# $(BUILD_DIR)/$(SRC_DIR)/game_14FF90.o: OPT_FLAGS := -O3

### Non-matching
ifeq ($(NON_MATCHING),1)
VERIFY :=
else
VERIFY := verify
endif

### Targets

default: all

all: dirs $(TARGET).bin $(VERIFY)

dirs:
	$(foreach dir,$(SRC_DIRS) $(ASM_DIRS) $(BIN_DIRS) ,$(shell mkdir -p build/$(dir)))

clean:
	rm -rf build

really-clean: clean
	rm -rf asm
	rm -rf bin
	rm -rf assets
	rm -rf $(BASENAME).*.ok
	rm -f *auto.txt
	rm -rf conker.us.bin conker.eu.bin conker.ects.bin conker.debug.bin

extract: $(BUILD_DIR)/splat

# sanity check base bin
check: $(BASENAME).$(VERSION).ok

# check built bin
verify: $(TARGET).ok

progress: $(VERIFY) progress.csv

# Byte-matching progress: how many C-converted functions compile to the
# exact retail bytes (progress.csv only counts conversion to C). Compares
# the linked ELF per function symbol against the pristine code image, so
# it works even while the rebuilt binary has layout drift. Use
# LIST=1 to print every non-exact function, smallest diff first.
match-progress: $(VERIFY) progress.csv $(TARGET).elf
	$(PYTHON) ../tools/match_progress.py progress.csv $(TARGET).elf \
		$(BASENAME).$(VERSION).bin --version $(VERSION) \
		--objdump $(CROSS)objdump $(if $(LIST),--list)

# replace original binaries
replace: $(VERIFY) $(TARGET).header.bin $(TARGET).boot.bin $(TARGET).init.bin $(TARGET_GAME_BIN) $(TARGET).debugger.bin
	cp $(TARGET).header.bin ../assets/header.$(VERSION).bin
	cp $(TARGET).boot.bin ../assets/boot.$(VERSION).bin
	cp $(TARGET).init.bin ../assets/init.$(VERSION).bin
	cp $(TARGET).debugger.bin ../assets/debugger.$(VERSION).bin
	cp $(TARGET_GAME_BIN) $(TARGET_ROOT_GAME_BIN)


### Recipes

$(BUILD_DIR)/$(LD_SCRIPT): $(LD_SCRIPT) ../tools/patch_generated_slice_ld.py
	$(CPP) -P -DBUILD_DIR=$(BUILD_DIR) -o $@ $<
	$(PYTHON) ../tools/patch_generated_slice_ld.py $@

$(TARGET).elf: $(O_FILES) $(BUILD_DIR)/$(LD_SCRIPT) $(GLOBAL_ASM_O_FILES)
	$(LD) $(LDFLAGS) -o $@

ifndef PERMUTER
$(GLOBAL_ASM_O_FILES): $(BUILD_DIR)/%.c.o: %.c include/variables.h include/structs.h include/functions.h
	$(PYTHON) $(ASM_PROCESSOR_DIR)/asm_processor.py $(OPT_FLAGS) $< > $(BUILD_DIR)/$<
	$(CC) -c -32 $(CFLAGS) $(OPT_FLAGS) $(LOOP_UNROLL) $(MIPSBIT) -o $@ $(BUILD_DIR)/$<
	$(PYTHON) $(ASM_PROCESSOR_DIR)/asm_processor.py $(OPT_FLAGS) $< --post-process $@ \
		--assembler "$(AS) $(ASFLAGS)" --asm-prelude include/asm_processor_prelude.inc
endif

$(BUILD_DIR)/%.c.o: %.c
	$(CC) -c -32 $(CFLAGS) $(OPT_FLAGS) $(MIPSBIT) -o $@ $<

$(BUILD_DIR)/%.s.o: %.s
	$(AS) $(ASFLAGS) -o $@ $<

$(BUILD_DIR)/%.bin.o: %.bin
	$(LD) -r -b binary -o $@ $<

$(TARGET).bin: $(TARGET).elf
	$(OBJCOPY) $(OBJCOPYFLAGS) -O binary $< $@

# extract
$(BUILD_DIR)/splat: check $(BASENAME).$(VERSION).yaml
	$(PYTHON) ../tools/n64splat/split.py $(BASENAME).$(VERSION).yaml

%.ok: %.bin
	@echo "$$(cat $(BASENAME).$(VERSION).sha1)  $<" | sha1sum --check
	@touch $@

conker.$(VERSION).bin:
	make extract -C ..

# dump sections
$(TARGET).header.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .header $< $@

$(TARGET).boot.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .boot $< $@

$(TARGET).init.bin: $(TARGET).init.code.bin $(TARGET).init.data.bin
	cat $^ > $@

$(TARGET).init.code.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .init $< $@

$(TARGET).init.data.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .init_data $< $@

#ects only
$(TARGET).game.bin: $(TARGET).game.code.bin $(TARGET).game.data.bin
	cat $^ > $@

$(TARGET).game.code.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .game $< $@

$(TARGET).game.data.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .game_data $< $@

$(TARGET).debugger.bin: $(TARGET).debugger.code.bin $(TARGET).debugger.data.bin
	cat $^ > $@

$(TARGET).debugger.code.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .debugger $< $@

$(TARGET).debugger.data.bin: $(TARGET).elf
	$(OBJCOPY) -O binary --only-section .debugger_data $< $@

# split code section
$(SPLIT_DIR)/0000.bin: $(TARGET).game.code.bin
	mkdir -p $(SPLIT_DIR)
	$(SPLIT) $< $(SPLIT_DIR)/

# create offsets file
$(SPLIT_DIR)/offsets.bin: $(SPLIT_DIR)/0000.bin
	$(RZIPDIR) $(SPLIT_DIR) $(SPLIT_DIR) --offsets-file $@ $(COMPRESS_DIR_ARGS)

# concatenate compressed code blocks
$(TARGET).game.code.rzip.bin: $(TARGET).game.code.bin $(SPLIT_DIR)/offsets.bin
	cat $(SPLIT_DIR)/*.gz > $@

# compressed data section
$(TARGET).game.data.rzip.bin: $(TARGET).game.data.bin
	$(RZIP) $< $@

# create padding
$(TARGET).game.code.padding.bin:
	cp ../assets/game/code_padding.bin $@

$(TARGET).game.data.padding.bin: $(TARGET).game.data.rzip.bin
	dd if=/dev/zero of=$@ bs=1 count=$$(($(DATA_SECTION_LENGTH)-$$(wc -c <$<)))

$(TARGET).game.rzip.bin: $(SPLIT_DIR)/offsets.bin $(TARGET).game.code.rzip.bin $(TARGET).game.code.padding.bin $(TARGET).game.data.rzip.bin $(TARGET).game.data.padding.bin
	cat $^ > $@

progress.csv: progress.init.csv progress.game.csv progress.debugger.csv
	cat $^ > $@

progress.init.csv: $(TARGET).elf
	$(PYTHON) ../tools/progress.py . $(TARGET).map .init --version $(VERSION) > $@
progress.game.csv: $(TARGET).elf
	$(PYTHON) ../tools/progress.py . $(TARGET).map .game --version $(VERSION) > $@
progress.debugger.csv: $(TARGET).elf
	$(PYTHON) ../tools/progress.py . $(TARGET).map .debugger --version $(VERSION) > $@


# settings
.PHONY: all clean default
SHELL = /bin/bash -e -o pipefail
