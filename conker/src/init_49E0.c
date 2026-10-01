#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_10004DB0(void);
/* End generated placeholder declarations. */

void func_100049E0(s32 arg0) {
    OSMesg message;
    OSPfs *client;
    OSScTask *task;
    OSTime delay;
    u8 counter;

    D_8003A581 = 0;
    D_8003A582 = 0;
    D_8003A584 = 1;
    D_8003A583 = 0;
    *(u16 *)&D_8003B240 = 1;
    message = NULL;
    *(u16 *)&D_8003A5C8 = 4;

    for (;;) {
        osRecvMesg(&D_8003B218, &message, OS_MESG_BLOCK);

        switch ((u32)message) {
        case 0:
            client = D_8003B234;
            while (client != NULL) {
                if ((client->channel & 1) == 0) {
                    osSendMesg(client->queue, &D_8003B240, OS_MESG_NOBLOCK);
                }
                client = (OSPfs *)client->status;
            }

            counter = D_8003B238;
            if ((counter != 0xFF) && ((s32)counter < 0xFF)) {
                D_8003B238 = counter + 1;
            }
            counter = D_8003B23A;
            if (counter != 0) {
                D_8003B23A = counter - 1;
            }

            if ((D_8003A581 == 0) && (D_8002AC6C == 0) &&
                (osRecvMesg(&D_8003B200, (OSMesg *)&D_8002AC54,
                            OS_MESG_NOBLOCK) == 0)) {
                delay = 0x30D40;
                if ((D_8003A582 != 0) ||
                    ((s32)(osAiGetStatus() << 0) >= 0)) {
                    delay = 0x4E20;
                }
                osSetTimer((OSTimer *)&D_8003A588, delay, 0,
                           &D_8003B218, (OSMesg *)3);
                D_8002AC6C = 1;
            }
            if (D_8003A581 == 0) {
                func_10004DB0();
            }
            break;

        case 2:
            if (D_8003A582 == 3) {
                if (osSpTaskYielded(&D_8002AC50->list) == 1) {
                    osSpTaskLoad(&D_8002AC54->list);
                    osSpTaskStartGo(&D_8002AC54->list);
                    D_8003A581 = 1;
                    D_8003A582 = 4;
                } else {
                    D_8003A582 = 1;
                    osSpTaskLoad(&D_8002AC54->list);
                    osSpTaskStartGo(&D_8002AC54->list);
                    D_8003A581 = 1;
                    D_8003A583 = 0;
                }
            } else if (D_8003A581 != 0) {
                task = D_8002AC54;
                osSendMesg(task->msgQ, task->msg, OS_MESG_BLOCK);
                D_8003A581 = 0;
                if (D_8003A582 == 4) {
                    osSpTaskLoad(&D_8002AC50->list);
                    osSpTaskStartGo(&D_8002AC50->list);
                    D_8003A580 = 1;
                    D_8003A582 = 1;
                }
            } else {
                D_8003A583 = 0;
                if (D_8003A584 == 1) {
                    func_10004FE0();
                }
            }
            break;

        case 1:
            D_8003A584 = 1;
            if (D_8003A583 == 0) {
                func_10004FE0();
            }
            break;

        case 3:
            D_8002AC6C = 0;
            if (D_8003A583 != 0) {
                osSpTaskYield();
                D_8003A582 = 3;
            } else {
                osSpTaskLoad(&D_8002AC54->list);
                osSpTaskStartGo(&D_8002AC54->list);
                D_8003A581 = 1;
            }
            break;

        case 6:
            if (D_8002AC5C == 0) {
                osContStartReadData(&D_800BE900);
            }
            break;

        default:
            break;
        }
    }
}

void func_10004DB0(void) {
    u8 active;

    if (D_8003A582 == 0) {
        if (osRecvMesg(&D_8003B1E8, (OSMesg *)&D_8002AC50, OS_MESG_NOBLOCK) == 0) {
            if (osViGetCurrentFramebuffer() == D_8002AC50->framebuffer) {
                goto task_busy;
            }
            if (osViGetNextFramebuffer() == D_8002AC50->framebuffer) {
                goto task_busy;
            }
            active = D_8003B23A;
            if ((active != 0) && (D_8003B238 < D_8003B239)) {
                goto task_busy;
            }
            if ((D_8003B238 != 0xFF) &&
                ((D_8003B238 >= D_8003B239) || (active == 0))) {
                D_8003B239 = D_8003B238;
            }
            func_10004F00();
            return;

task_busy:
            D_8003A582 = 2;
        }
    } else if (D_8003A582 == 2) {
        if ((D_8003B23A == 0) || (D_8003B238 >= D_8003B239)) {
            func_10004F00();
        }
    } else if (D_8003A582 == 6) {
        func_10004FE0();
    }
}

void func_10004F00(void) {
    if (D_8002AC5C == 0) {
        osSpTaskLoad(&D_8002AC50->list);
        osSpTaskStartGo(&D_8002AC50->list);
        D_8003A580 = 0;
        D_8002AC58 = D_8002AC50;
        D_8003A583 = 1;
        D_8003A584 = 0;
        if ((D_8003B238 == 255) ||
            ((D_8003B238 >= 11) && ((D_8003B238 >= 21) || (D_800C35EA != 1)))) {
            D_8003B238 = 2;
        }
        D_800BE9E4 = D_8003B238;
        D_8003B238 = 0 ;
        D_8003A582 = 1;
        osSendMesg(D_8003B230, &D_8003B240, 0);
    }
}

void func_10004FE0(void) {
    if (D_8003B238 <= 0) {
        D_8003A582 = 6;
    } else {
        func_10005020();
    }
}

void func_10005020(void) {
    void *fb;

    D_8003A582 = 0;
    fb = D_8002AC50->framebuffer;
    if ((D_8002AC50->flags & OS_SC_SWAPBUFFER) && (D_8002AC5C == 0)) {
        func_1515FDA0(fb);
        osViSwapBuffer(fb);
    }
    osSendMesg(D_8002AC50->msgQ, D_8002AC50->msg, 1);
}
