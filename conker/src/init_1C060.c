
#include <libaudio.h>
#include "n_libaudio.h"
#include <os_internal.h>
#include <ultraerror.h>

void n_alEvtqNew(ALEventQueue *evtq, N_ALEventListItem *items, s32 itemCount)
{
    s32 i;
    ALLink *item, *to;

    evtq->eventCount     = 0;
    evtq->allocList.next = 0;
    evtq->allocList.prev = 0;
    evtq->freeList.next  = 0;
    evtq->freeList.prev  = 0;

    for (i = 0; i < itemCount; i++) {
        item = &items[i];
        to = &evtq->freeList;
        // effectively alLink, TODO: macro this?
        item->next = to->next;
        item->prev = to;
        if (to->next) {
            to->next->prev = item;
        }
        to->next = item;
    }

}

/* Non-matching C placeholders for asm/nonmatchings/init_1C060/n_alEvtqNextEvent.s. */
ALMicroTime n_alEvtqNextEvent(ALEventQueue *evtq, N_ALEvent *evt)
{
    N_ALEventListItem *item;
    ALMicroTime delta;
    ALLink *unlink;
    ALLink *linkItem;
    ALLink *freeList;

    /* Conker: no osSetIntMask (PD/libreultra always mask). */
    item = (N_ALEventListItem *)evtq->allocList.next;

    if (item) {
        unlink = (ALLink *)item;
        if (unlink->next != 0) {
            unlink->next->prev = unlink->prev;
        }
        if (unlink->prev != 0) {
            unlink->prev->next = unlink->next;
        }
        bcopy(&item->evt, evt, sizeof(*evt));
        linkItem = (ALLink *)item;
        freeList = &evtq->freeList;
        linkItem->next = freeList->next;
        linkItem->prev = freeList;
        if (freeList->next != 0) {
            freeList->next->prev = linkItem;
        }
        freeList->next = linkItem;
        delta = item->delta;
    } else {
        /* sct 11/28/95 - overflowed the event queue */
        evt->type = -1;
        delta = 0;
    }

    return delta;
}
// s32 n_alEvtqNextEvent(void *arg0, void *arg1) {
//     void *sp2C;
//     s32 sp28;
//     void *sp24;
//     void *sp20;
//     void *sp1C;
//
//     sp2C = arg0->unk8;
//     if (sp2C != 0) {
//         sp24 = sp2C;
//         if (sp24->unk0 != 0) {
//             sp24->unk0->unk4 = (s32) sp24->unk4;
//         }
//         if (sp24->unk4 != 0) {
//             *sp24->unk4 = (s32) sp24->unk0;
//         }
//         bcopy(sp2C + 0xC, arg1, 0x10);
//         sp20 = sp2C;
//         sp1C = arg0;
//         sp20->unk0 = (s32) *sp1C;
//         sp20->unk4 = sp1C;
//         if (*sp1C != 0) {
//             (*sp1C)->unk4 = sp20;
//         }
//         *sp1C = sp20;
//         sp28 = sp2C->unk8;
//     } else {
//         *arg1 = (u16)-1;
//         sp28 = 0;
//     }
//     return sp28;
// }

/* Non-matching C placeholders for asm/nonmatchings/init_1C060/n_alEvtqPostEvent.s. */
void n_alEvtqPostEvent(ALEventQueue *evtq, N_ALEvent *evt, ALMicroTime delta, s32 arg3)
{
    N_ALEventListItem *item;
    N_ALEventListItem *nextItem;
    ALLink *node;
    s32 postAtEnd;
    OSIntMask mask;
    ALLink *unlink;
    ALLink *element;
    ALLink *after;
    ALLink *element2;
    ALLink *after2;

    postAtEnd = 0;

    /* Conker: mask only when arg3 bit1 set (PD always masks). */
    if (arg3 & 2) {
        mask = osSetIntMask(1);
    }

    item = (N_ALEventListItem *)evtq->freeList.next;

    if (item == 0) {
        if (arg3 & 2) {
            osSetIntMask(mask);
        }
        return;
    }

    /* Conker: bit0 allows posting the last free item (PD uses !arg3). */
    if ((item->node.next == 0) && ((arg3 & 1) == 0)) {
        if (arg3 & 2) {
            osSetIntMask(mask);
        }
        return;
    }

    unlink = (ALLink *)item;
    if (unlink->next != 0) {
        unlink->next->prev = unlink->prev;
    }
    if (unlink->prev != 0) {
        unlink->prev->next = unlink->next;
    }
    bcopy(evt, &item->evt, sizeof(*evt));

    if (delta == AL_EVTQ_END) {
        postAtEnd = -1;
    }

    for (node = &evtq->allocList; node != 0; node = node->next) {
        if (node->next == 0) { /* end of the list */
            if (postAtEnd != 0) {
                item->delta = 0;
            } else {
                item->delta = delta;
            }

            element = (ALLink *)item;
            after = node;
            element->next = after->next;
            element->prev = after;
            if (after->next != 0) {
                after->next->prev = element;
            }
            after->next = element;
            break;
        } else {
            nextItem = (N_ALEventListItem *)node->next;

            if (delta < nextItem->delta) {
                item->delta = delta;
                nextItem->delta -= delta;

                element2 = (ALLink *)item;
                after2 = node;
                element2->next = after2->next;
                element2->prev = after2;
                if (after2->next != 0) {
                    after2->next->prev = element2;
                }
                after2->next = element2;
                break;
            }

            delta -= nextItem->delta;
        }
    }

    if (arg3 & 2) {
        osSetIntMask(mask);
    }
}
// void n_alEvtqPostEvent(void *arg0, s32 arg1, s32 arg2, s32 arg3) {
//     void *sp3C;
//     void *sp38;
//     void *sp34;
//     s32 sp30;
//     s32 sp2C;
//     void *sp28;
//     void *sp24;
//     void *sp20;
//     void *sp1C;
//     void *sp18;
//     void *temp_t3;
//     void *temp_t5;
//
//     sp30 = 0;
//     if ((arg3 & 2) != 0) {
//         sp2C = osSetIntMask(1);
//     }
//     sp3C = *arg0;
//     if (sp3C == 0) {
//         if ((arg3 & 2) != 0) {
//             osSetIntMask(sp2C);
//         }
//         return;
//     }
//     if ((sp3C->unk0 == 0) && ((arg3 & 1) == 0)) {
//         if ((arg3 & 2) != 0) {
//             osSetIntMask(sp2C);
//         }
//         return;
//     }
//     sp28 = sp3C;
//     if (sp28->unk0 != 0) {
//         sp28->unk0->unk4 = (s32) sp28->unk4;
//     }
//     if (sp28->unk4 != 0) {
//         *sp28->unk4 = (s32) sp28->unk0;
//     }
//     bcopy(arg1, sp3C + 0xC, 0x10);
//     if (arg2 == 0x7FFFFFFF) {
//         sp30 = -1;
//     }
//     temp_t3 = arg0 + 8;
//     sp34 = temp_t3;
//     if (temp_t3 != 0) {
// loop_18:
//         if (*sp34 == 0) {
//             if (sp30 != 0) {
//                 sp3C->unk8 = 0;
//             } else {
//                 sp3C->unk8 = arg2;
//             }
//             sp24 = sp3C;
//             sp20 = sp34;
//             sp24->unk0 = (s32) *sp20;
//             sp24->unk4 = sp20;
//             if (*sp20 != 0) {
//                 (*sp20)->unk4 = sp24;
//             }
//             *sp20 = sp24;
//         } else {
//             sp38 = *sp34;
//             if (arg2 < sp38->unk8) {
//                 sp3C->unk8 = arg2;
//                 sp38->unk8 = (s32) (sp38->unk8 - arg2);
//                 sp1C = sp3C;
//                 sp18 = sp34;
//                 sp1C->unk0 = (s32) *sp18;
//                 sp1C->unk4 = sp18;
//                 if (*sp18 != 0) {
//                     (*sp18)->unk4 = sp1C;
//                 }
//                 *sp18 = sp1C;
//             } else {
//                 arg2 = arg2 - sp38->unk8;
//                 temp_t5 = *sp34;
//                 sp34 = temp_t5;
//                 if (temp_t5 != 0) {
//                     goto loop_18;
//                 }
//             }
//         }
//     }
//     if ((arg3 & 2) != 0) {
//         osSetIntMask(sp2C);
//     }
// }

/* Non-matching C placeholders for asm/nonmatchings/init_1C060/func_1001C4F0.s. */
ALMicroTime func_1001C4F0(ALEventQueue *evtq, s16 type)
{
    N_ALEventListItem *current;
    N_ALEventListItem *next;
    N_ALEventListItem *item;
    N_ALEventListItem *nextEvent;
    OSIntMask mask;
    ALMicroTime firstDelta;
    ALMicroTime itemTime;
    ALLink *unlink;
    ALLink *linkItem;
    ALEventQueue *queue;

    /* Conker: also returns absolute time of the first flushed event. */
    firstDelta = 0;
    itemTime = 0;
    mask = osSetIntMask(1);

    current = (N_ALEventListItem *)evtq->allocList.next;
    if (current != 0) {
        do {
            next = (N_ALEventListItem *)current->node.next;
            item = current;
            nextEvent = next;
            itemTime += item->delta;

            if (item->evt.type == type) {
                if (firstDelta == 0) {
                    firstDelta = itemTime;
                }
                if (nextEvent != 0) {
                    nextEvent->delta += item->delta;
                }

                unlink = (ALLink *)current;
                if (unlink->next != 0) {
                    unlink->next->prev = unlink->prev;
                }
                if (unlink->prev != 0) {
                    unlink->prev->next = unlink->next;
                }

                linkItem = (ALLink *)current;
                queue = evtq;
                linkItem->next = queue->freeList.next;
                linkItem->prev = &queue->freeList;
                if (queue->freeList.next != 0) {
                    queue->freeList.next->prev = linkItem;
                }
                queue->freeList.next = linkItem;
            }

            current = next;
        } while (current != 0);
    }

    osSetIntMask(mask);
    return firstDelta;
}
// s32 func_1001C4F0(void *arg0, s16 arg1) {
//     void *sp3C;
//     void *sp38;
//     void *sp34;
//     void *sp30;
//     s32 sp2C;
//     s32 sp28;
//     s32 sp24;
//     void *sp20;
//     void *sp1C;
//     void *sp18;
//
//     sp28 = 0;
//     sp24 = 0;
//     sp2C = osSetIntMask(1);
//     sp3C = arg0->unk8;
//     if (sp3C != 0) {
// loop_1:
//         sp38 = *sp3C;
//         sp34 = sp3C;
//         sp30 = sp38;
//         sp24 = sp24 + sp34->unk8;
//         if (sp34->unkC == arg1) {
//             if (sp28 == 0) {
//                 sp28 = sp24;
//             }
//             if (sp30 != 0) {
//                 sp30->unk8 = (s32) (sp30->unk8 + sp34->unk8);
//             }
//             sp20 = sp3C;
//             if (sp20->unk0 != 0) {
//                 sp20->unk0->unk4 = (s32) sp20->unk4;
//             }
//             if (sp20->unk4 != 0) {
//                 *sp20->unk4 = (s32) sp20->unk0;
//             }
//             sp1C = sp3C;
//             sp18 = arg0;
//             sp1C->unk0 = (s32) *sp18;
//             sp1C->unk4 = sp18;
//             if (*sp18 != 0) {
//                 (*sp18)->unk4 = sp1C;
//             }
//             *sp18 = sp1C;
//         }
//         sp3C = sp38;
//         if (sp3C != 0) {
//             goto loop_1;
//         }
//     }
//     osSetIntMask(sp2C);
//     return sp28;
// }
