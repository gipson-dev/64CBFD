#include <ultra64.h>
#include "variables.h"
extern s16 D_8008FDCC;
extern u8 D_800E0B94;
extern u8 D_800BE616;
extern u8 D_800BE740;
extern s8 D_8008FD90;
extern s8 D_800E0BD3;
extern u8 **D_800E0BD8;
extern s32 (*D_8008FFF4[])(s32);
extern Gfx *(*D_8008FFC0[])(Gfx *);
extern s32 D_80090058;
extern s16 D_800E0C78;
extern s32 D_800BEBA4;
extern Gfx *D_800BE9C8[];
extern f32 D_8008FE1C;
extern f32 D_8008FE20;
extern u16 D_8008FDC0;
extern Gfx D_80090028;
extern u8 D_8009006C[];
extern u8 D_80090070[];
extern u8 D_800ABA90[][4];
extern u8 D_800ABAA0;
extern u8 D_800ABAA4;
extern f32 D_800ABAD8;
extern s8 D_80087268;
extern s8 *D_8008FDD4;
extern s32 D_800BE9AC;
extern s16 D_800E0AA0[];
extern s8 D_800E0BB0;
extern u16 D_800E0BCC;
extern s8 D_800E0C00[];
extern u8 D_D10;
extern u8 D_D14;
extern u8 D_D16;
s32 func_151ED1E0(void);
Gfx *func_151E966C(Gfx *, s32, s32, s8, u8);
Gfx *func_151E9D18(Gfx *, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/215960.s. */

s32 func_151E84B0(void) {
    /* Retain retail's local-slot gap under IDO's debug layout. */
    s32 stack_pad;
    s32 result;
    s32 index = 0;
    s32 (*callback)(s32);

    D_8003C8E0 = 0x09000001;
    result = func_151ED1E0();
    callback = D_8008FFF4[D_800E0B94];
    if (callback != NULL) {
        result = callback(result);
    }

    if (D_80000300 != 0) {
        if ((D_800BE616 != 0) && (D_8008FD90 >= 2)) {
            if ((D_800BE740 & 0xF) == 0) {
                if (D_800E0BD3 == 1) {
                    index = 0x33;
                } else if (D_800E0BD3 == 2) {
                    index = 0x16;
                }
            }
        } else if ((D_800BE740 & 1) == 0) {
            if (D_800E0BD3 == 1) {
                index = 0x32;
            } else if (D_800E0BD3 == 2) {
                index = 0x15;
            }
        }
    }

    if (index != 0) {
        func_1504332C(0xFF, 0xFF, 0xFF, 0xFF);
        func_15042D94(0x94, 0xC8, 0x81, D_800E0BD8[index]);
    }

    D_8003C8E0 = 0;
    return result;
}

Gfx *func_151E8620(Gfx *value) {
    s32 mode;
    Gfx *original;
    Gfx *(*callback)(Gfx *);
    s32 overflow;

    mode = D_800E0B94;
    callback = D_8008FFC0[mode];
    original = value;
    D_8003C8E0 = 0x09000000;
    if (callback != NULL) {
        value = callback(value);
        mode = D_800E0B94;
    }

    if (mode != 0) {
        D_80090058 = 0;
        D_800E0C78 = 0;
    }

    D_8003C8E0 = 0;
    if (D_800BEBA4 < (value - D_800BE9C8[D_800BE9C0])) {
        overflow = 1;
    } else {
        overflow = 0;
    }
    if (overflow != 0) {
        return original;
    }
    return value;
}

Gfx *func_151E86E4(Gfx *display_list, s32 ulx, s32 uly, s32 lrx, s32 lry,
                   s32 tile, s32 s, s32 t, s32 dsdx, s32 dtdy) {
    if (D_8008FE1C != 1.0f) {
        ulx = (s32) ((f32) ulx * D_8008FE1C);
        lrx = (s32) ((f32) lrx * D_8008FE1C);
        uly = (s32) ((f32) uly * D_8008FE20);
        lry = (s32) ((f32) lry * D_8008FE20);
        dsdx = (s32) ((f32) dsdx / D_8008FE1C);
        dtdy = (s32) ((f32) dtdy / D_8008FE20);
    }

    gSPScisTextureRectangle(display_list++, ulx, uly, lrx, lry, tile,
                            s, t, dsdx, dtdy);
    return display_list;
}

Gfx *func_151E89A0(Gfx *display_list, s32 arg1, s32 alpha) {
    u8 stack_pad[0x60];
    s32 row_x;
    s32 hud_y;
    s32 saved_index;
    s32 row_step;
    s32 selected;
    u8 nearby;
    u8 status_flags;
    f32 target_x;
    f32 target_y;
    f32 target_z;
    s32 color_alpha;
    s32 row_bottom;
    struct127 *object;
    u8 *owner;
    f32 dx;
    f32 dz;
    f32 distance_squared;
    s32 score;
    s32 divisor;
    s32 digit;
    s32 digit_x;
    s32 started;
    s32 done;
    s32 index;
    s32 texture;
    s32 icon_width;
    s32 icon_flag;
    s32 load_count;
    s32 tile_line;
    s32 icon_t;
    s32 icon_row;
    u16 hud_flags;
    s32 selected_value;
    u8 *resource;
    Gfx *command;

    status_flags = 0;
    D_8008FDBC &= 0xFFEF;

    command = display_list++;
    command->words.w0 = 0xDE000000;
    command->words.w1 = (u32) &D_80090028;
    command = display_list++;
    command->words.w1 = 0xFFFFF3F9;
    command->words.w0 = 0xFC12FE25;

    if (D_80082FA0 == 0) {
        hud_y = 0x320;
    } else {
        hud_y = 0x198;
    }

    row_step = 0x124;
    if (D_800E0BB0 > 0) {
        row_step = 0x124 / D_800E0BB0;
    }

    D_800E0BCC = 0;
    nearby = 0;
    selected_value = -1;
    index = 0;
    if (D_8008FD8C > 0) {
        object = D_800CC2D0;
        do {
            owner = (u8 *) object->unk31C;
            if ((object->unk13C != 0) || (owner[0x128] & 0x20)) {
                selected_value = *((u8 *) object + 0x128);
                D_800E0BCC |= 1 << index;
            }

            if ((selected_value != -1) && (D_8008FDC0 & 0x8000)) {
                if (selected_value == 0) {
                    status_flags |= 2;
                } else {
                    status_flags |= 1;
                }
                selected_value = -1;
            }

            if ((*((u8 *) object + 0x128) == 1) && (object->unk2E4 != 0) &&
                (D_8008FDC0 & 0x4000)) {
                status_flags |= 4;
            }

            if ((owner[0x75] & 0x7F) == 0x25) {
                selected = selected_value;
                saved_index = index;
                color_alpha = status_flags;
                func_15086CBC(func_15086D48(0x49), &target_x, &target_y, &target_z);
                dx = target_x - object->x_position;
                dz = target_z - object->z_position;
                target_x = dx;
                target_z = dz;
                distance_squared = (dx * dx) + (dz * dz);
                target_z = distance_squared;
                if (distance_squared < D_800ABAD8) {
                    nearby = 1;
                    D_8008FDBC |= 0x10;
                }
                selected_value = selected;
                D_800E0BCC |= 1 << index;
                status_flags = color_alpha;
                index = saved_index;
            }

            index++;
            object++;
        } while (index < D_8008FD8C);
    }

    hud_flags = D_8008FDC0;
    texture = 0;
    if ((D_800BE9AC & 0x1F) < 0xB) {
        D_800E0BCC = 0;
        nearby = 0;
        selected_value = -1;
        status_flags = 0;
    }

    selected = selected_value;
    if (hud_flags & 9) {
        texture = func_1510D0EC(&D_D14, 0, 3, 0);
        if (texture != 0x80000000) {
            command = display_list++;
            command->words.w1 = texture;
            command->words.w0 = 0xFD180000;
            command = display_list++;
            command->words.w1 = 0x07094250;
            command->words.w0 = 0xF5180000;
            command = display_list++;
            command->words.w1 = 0;
            command->words.w0 = 0xE6000000;
            command = display_list++;
            command->words.w1 = 0x073FF000;
            command->words.w0 = 0xF3000000;
            command = display_list++;
            command->words.w1 = 0;
            command->words.w0 = 0xE7000000;
            command = display_list++;
            command->words.w0 = 0xF5181000;
            command->words.w1 = 0x00094250;
            command = display_list++;
            command->words.w0 = 0xF2000000;
            command->words.w1 = 0x0007C07C;
            command = display_list++;
            command->words.w0 = 0xEF002C3F;
            command->words.w1 = 0x00504244;
        } else {
            texture = 0;
        }
    }

    if ((hud_flags & 8) && (texture != 0)) {
        row_x = row_step >> 1;
        if (D_800E0BB0 > 0) {
            row_bottom = hud_y + 0x1C;
            color_alpha = alpha & 0xFF;
            index = 0;
            do {
                started = 0;
                done = 0;
                score = func_150859AC((s16) index, 6);
                command = display_list++;
                command->words.w1 = 0;
                command->words.w0 = 0xE7000000;
                command = display_list++;
                command->words.w0 = 0xFB000000;
                command->words.w1 = (D_800ABA90[index][0] << 24) |
                                    (D_800ABA90[index][1] << 16) |
                                    (D_800ABA90[index][2] << 8) | color_alpha;

                digit_x = (row_x + 0xA) * 4;
                display_list = func_151E86E4(display_list, (row_x + 3) * 4,
                                             hud_y, digit_x, row_bottom, 0,
                                             0x1C0, 0x200, 0x400, 0x400);
                divisor = 10000;
                do {
                    digit = score / divisor;
                    if ((digit != 0) || (started != 0) || (divisor == 1)) {
                        started = 1;
                        display_list = func_151E86E4(
                            display_list, digit_x, hud_y, digit_x + 0x14,
                            row_bottom, 0, D_8009006C[digit & 3] << 5,
                            D_80090070[digit >> 2] << 5, 0x400, 0x400);
                        digit_x += 0x18;
                    }
                    score %= divisor;
                    if (divisor == 1) {
                        done = 1;
                    }
                    divisor /= 10;
                } while (done == 0);

                index++;
                row_x += row_step;
            } while (index < D_800E0BB0);
        }
    }

    if (hud_flags & 1) {
        display_list = func_151E966C(display_list, hud_y, selected, 0, 1);
    }

    if ((nearby != 0) || (selected != -1)) {
        if (D_8008FDC0 & 0x4000) {
            resource = &D_D16 + 1;
        } else {
            resource = &D_D16;
        }
        texture = func_1510D0EC(resource, 0, 3, 0);
        if (texture != 0x80000000) {
            command = display_list++;
            command->words.w0 = 0xFD500000;
            command->words.w1 = texture;
            command = display_list++;
            command->words.w0 = 0xF5500000;
            command->words.w1 = 0x07098260;
            command = display_list++;
            command->words.w1 = 0;
            command->words.w0 = 0xE6000000;
            command = display_list++;
            command->words.w1 = 0x073FF000;
            command->words.w0 = 0xF3000000;
            command = display_list++;
            command->words.w0 = 0xE7000000;
            color_alpha = alpha & 0xFF;
            command->words.w1 = 0;
            command = display_list++;
            command->words.w1 = 0x00098260;
            command->words.w0 = 0xF5400800;
            command = display_list++;
            command->words.w0 = 0xF2000000;
            command->words.w1 = 0x000FC0FC;
            command = display_list++;
            command->words.w1 = texture + 0x800;
            command->words.w0 = 0xFD100000;
            command = display_list++;
            command->words.w1 = 0;
            command->words.w0 = 0xE6000000;
            command = display_list++;
            command->words.w1 = 0x0603C000;
            command->words.w0 = 0xF0000000;
            command = display_list++;
            command->words.w0 = 0xEF00AC3F;
            command->words.w1 = 0x00504244;
            command = display_list++;
            command->words.w0 = 0xFB000000;
            command->words.w1 = color_alpha | 0xFFFFFF00;

            if (nearby != 0) {
                display_list = func_151E86E4(display_list, 0x238, 0xC, 0x268,
                                             0x48, 0, 0x640, 0x660, 0x400,
                                             0x400);
            }
            if (selected != -1) {
                if (D_8008FDC0 & 0x4000) {
                    display_list = func_151E86E4(display_list, 0x220, 0xC,
                                                 0x250, 0x48, 0, 0x600,
                                                 0x540, 0x400, 0x400);
                } else {
                    icon_row = 0;
                    if (D_8008FDC0 & 1) {
                        icon_t = 0x1A;
                    } else {
                        icon_t = 0x26;
                        icon_row = 0xB;
                    }
                    display_list = func_151E86E4(
                        display_list, 0x238, (icon_row + 3) * 4, 0x268,
                        (icon_row + 0xE) * 4, 0, 0x640, icon_t << 5,
                        0x400, 0x400);
                }
            }
        }
    }

    icon_width = 0x20;
    icon_flag = status_flags & 4;
    if (status_flags != 0) {
        if (icon_flag != 0) {
            resource = &D_D10 + 1;
            icon_width = 0x10;
        } else {
            resource = &D_D10;
        }
        texture = func_1510D0EC(resource, 0, 3, 0);
        if (texture != 0x80000000) {
            command = display_list++;
            command->words.w0 = 0xE7000000;
            command->words.w1 = 0;
            command = display_list++;
            command->words.w1 = texture;
            command->words.w0 = 0xFD180000;
            command = display_list++;
            command->words.w1 = 0x07094250;
            command->words.w0 = 0xF5180000;
            command = display_list++;
            command->words.w1 = 0;
            command->words.w0 = 0xE6000000;
            command = display_list++;
            command->words.w0 = 0xF3000000;
            load_count = (icon_width << 5) - 1;
            if (load_count >= 0x7FF) {
                load_count = 0x7FF;
            }
            command->words.w1 = ((load_count & 0xFFF) << 12) | 0x07000000;
            command = display_list++;
            command->words.w1 = 0;
            command->words.w0 = 0xE7000000;
            command = display_list++;
            tile_line = (((icon_width * 2) + 7) >> 3) & 0x1FF;
            command->words.w1 = 0x00094250;
            command->words.w0 = (tile_line << 9) | 0xF5180000;
            command = display_list++;
            command->words.w0 = 0xF2000000;
            command->words.w1 = ((((icon_width - 1) * 4) & 0xFFF) << 12) |
                                0x7C;
            command = display_list++;
            command->words.w0 = 0xEF000C3F;
            command->words.w1 = 0x00504244;
            command = display_list++;
            command->words.w1 = 0xFFFFFFFF;
            command->words.w0 = 0xFB000000;

            if (status_flags & 1) {
                icon_row = hud_y - 0x10;
                display_list = func_151E86E4(display_list, 0xA0, icon_row,
                                             0xE0, icon_row + 0x40, 0, 0,
                                             0x200, 0x400, 0x400);
            }
            if (status_flags & 2) {
                icon_row = hud_y - 0x10;
                display_list = func_151E86E4(display_list, 0x3B0, icon_row,
                                             0x3F0, icon_row + 0x40, 0,
                                             0x200, 0x200, 0x400, 0x400);
            }
            if (icon_flag != 0) {
                display_list = func_151E86E4(display_list, 0x250, 0xC, 0x280,
                                             0x48, 0, 0, 0x200, 0x400,
                                             0x400);
            }
        }
    }

    if (D_8008FDC0 & 0x6340) {
        display_list = func_151E9D18(display_list, hud_y, 1);
    }
    return display_list;
}

Gfx *func_151E966C(Gfx *arg0, s32 y, s32 selected_row,
                   s8 load_texture, u8 refresh_counts) {
    u8 stack_pad[0x68];
    s8 hidden_mask;
    s32 row_center;
    s32 row_step;
    s16 *cached_count;
    s32 first_center;
    s16 life_count;
    s16 player;
    s32 box;
    s32 box_x;
    s32 texture;
    s32 icon_center;
    Gfx *command;
    Gfx *display_list;

    display_list = arg0;
    hidden_mask = 0;
    if (load_texture != 0) {
        texture = func_1510D0EC(&D_D14, 0, 3, 0);
        if (texture == 0x80000000) {
            return display_list;
        }

        command = display_list++;
        command->words.w0 = 0xE7000000;
        command->words.w1 = 0;
        command = display_list++;
        command->words.w1 = 0xFFFFF3F9;
        command->words.w0 = 0xFC12FE25;
        command = display_list++;
        command->words.w0 = 0xFD180000;
        command->words.w1 = texture;
        command = display_list++;
        command->words.w0 = 0xF5180000;
        command->words.w1 = 0x07094250;
        command = display_list++;
        command->words.w0 = 0xE6000000;
        command->words.w1 = 0;
        command = display_list++;
        command->words.w0 = 0xF3000000;
        command->words.w1 = 0x073FF000;
        command = display_list++;
        command->words.w0 = 0xE7000000;
        command->words.w1 = 0;
        command = display_list++;
        command->words.w0 = 0xF5181000;
        command->words.w1 = 0x00094250;
        command = display_list++;
        command->words.w0 = 0xF2000000;
        command->words.w1 = 0x0007C07C;
        command = display_list++;
        command->words.w0 = 0xEF002C3F;
        command->words.w1 = 0x00504244;
    }

    row_step = 0x124;
    if (D_800E0BB0 > 0) {
        row_step = 0x124 / D_800E0BB0;
    }

    if (refresh_counts != 0) {
        hidden_mask = 0xF;
        player = 0;
        if (D_8008FD8C > 0) {
            do {
                if (func_150859AC(player, 3) != 0) {
                    hidden_mask &= ~(1 << D_800E0C00[player]);
                }
                player++;
            } while (player < D_8008FD8C);
        }
    }

    player = 0;
    first_center = row_step >> 1;
    row_center = first_center;
    if (D_800E0BB0 > 0) {
        cached_count = D_800E0AA0;
        do {
            if (refresh_counts != 0) {
                life_count = func_150859AC(player, 6);
                *cached_count = life_count;
            } else {
                life_count = *cached_count;
            }

            if (!(hidden_mask & (1 << player))) {
                box = 0;
                if (player == selected_row) {
                    life_count++;
                }

                command = display_list++;
                command->words.w0 = 0xE7000000;
                command->words.w1 = 0;
                command = display_list++;
                command->words.w0 = 0xFB000000;
                command->words.w1 = (D_800ABA90[player][0] << 24) |
                                    (D_800ABA90[player][1] << 16) |
                                    (D_800ABA90[player][2] << 8) | 0xFF;

                box_x = row_center - (D_80087268 * 4);
                if (D_80087268 > 0) {
                    do {
                        if (box == life_count) {
                            command = display_list++;
                            command->words.w0 = 0xE7000000;
                            command->words.w1 = 0;
                            command = display_list++;
                            command->words.w0 = 0xFB000000;
                            command->words.w1 = 0x40404040;
                        }
                        box++;
                        display_list = func_151E86E4(
                            display_list, box_x * 4, y, (box_x + 7) * 4,
                            y + 0x1C, 0, 0x1C0, 0x200, 0x400, 0x400);
                        box_x += 8;
                    } while (box < D_80087268);
                }
            }

            player++;
            cached_count++;
            row_center += row_step;
        } while (player < D_800E0BB0);
    }

    if (hidden_mask != 0) {
        texture = func_1510D0EC(&D_D16 + 1, 0, 3, 0);
        if (texture == 0x80000000) {
            return display_list;
        }

        command = display_list++;
        command->words.w0 = 0xE7000000;
        command->words.w1 = 0;
        command = display_list++;
        command->words.w0 = 0xFD500000;
        command->words.w1 = texture;
        command = display_list++;
        command->words.w0 = 0xF5500000;
        command->words.w1 = 0x07098260;
        command = display_list++;
        command->words.w0 = 0xE6000000;
        command->words.w1 = 0;
        command = display_list++;
        command->words.w0 = 0xF3000000;
        command->words.w1 = 0x073FF000;
        command = display_list++;
        command->words.w0 = 0xE7000000;
        command->words.w1 = 0;
        command = display_list++;
        command->words.w0 = 0xF5400800;
        command->words.w1 = 0x00098260;
        command = display_list++;
        command->words.w0 = 0xF2000000;
        command->words.w1 = 0x000FC0FC;
        command = display_list++;
        command->words.w0 = 0xFD100000;
        command->words.w1 = texture + 0x800;
        command = display_list++;
        command->words.w0 = 0xE6000000;
        command->words.w1 = 0;
        command = display_list++;
        command->words.w0 = 0xF0000000;
        command->words.w1 = 0x0603C000;
        command = display_list++;
        command->words.w0 = 0xEF00AC3F;
        command->words.w1 = 0x00504244;

        player = 0;
        icon_center = first_center;
        if (D_800E0BB0 > 0) {
            do {
                if (hidden_mask & (1 << player)) {
                    row_center = icon_center;
                    command = display_list++;
                    command->words.w0 = 0xE7000000;
                    command->words.w1 = 0;
                    command = display_list++;
                    command->words.w0 = 0xFB000000;
                    command->words.w1 = (D_800ABA90[player][0] << 24) |
                                        (D_800ABA90[player][1] << 16) |
                                        (D_800ABA90[player][2] << 8) | 0xFF;
                    display_list = func_151E86E4(
                        display_list, (row_center - 8) * 4, y - 0x18,
                        (row_center + 8) * 4, y + 0x28, 0, 0x600, 0x280,
                        0x400, 0x400);
                }
                player++;
                icon_center += row_step;
            } while (player < D_800E0BB0);
        }
    }

    command = display_list++;
    command->words.w0 = 0xE7000000;
    command->words.w1 = 0;
    return display_list;
}

Gfx *func_151E9D18(Gfx *display_list, s32 arg1, s32 arg2) {
    u8 stack_pad[0x40];
    s32 texture_t;
    s32 panel_y;
    s32 texture_s_left;
    s32 texture_s_right;
    s32 object_save;
    u8 *resource;
    struct127 *object;
    s16 value;
    s32 left_total;
    s32 right_total;
    s16 player;
    s32 texture_width;
    s32 load_count;
    s32 text_y;
    s32 texture;
    s32 tile_line;
    s8 *team;
    s8 *record;
    Gfx *command;

    panel_y = arg1 - 0x10;
    if ((D_8008FDC0 & 0x4000) || (D_8008FDD4[0x42] == 8)) {
        resource = &D_D10 + 1;
        texture_width = 0x10;
        if (D_8008FDD4[0x42] == 8) {
            resource = &D_D10 + 2;
        }
        texture_s_left = 0;
        texture_s_right = 0x200;
    } else {
        resource = &D_D10;
        texture_width = 0x20;
        texture_s_left = 0x200;
        texture_s_right = 0;
    }

    texture = func_1510D0EC(resource, 0, 3, 0);
    if (texture == 0x80000000) {
        return display_list;
    }

    command = display_list++;
    command->words.w0 = 0xE7000000;
    command->words.w1 = 0;
    command = display_list++;
    command->words.w0 = 0xFD180000;
    command->words.w1 = texture;
    command = display_list++;
    command->words.w1 = 0x07094250;
    command->words.w0 = 0xF5180000;
    command = display_list++;
    command->words.w0 = 0xE6000000;
    command->words.w1 = 0;
    command = display_list++;
    command->words.w0 = 0xF3000000;
    load_count = (texture_width << 5) - 1;
    if (load_count >= 0x7FF) {
        load_count = 0x7FF;
    }
    command->words.w1 = ((load_count & 0xFFF) << 12) | 0x07000000;
    command = display_list++;
    command->words.w0 = 0xE7000000;
    command->words.w1 = 0;
    command = display_list++;
    tile_line = (((texture_width * 2) + 7) >> 3) & 0x1FF;
    command->words.w0 = (tile_line << 9) | 0xF5180000;
    command->words.w1 = 0x00094250;
    command = display_list++;
    command->words.w0 = 0xF2000000;
    command->words.w1 = ((((texture_width - 1) * 4) & 0xFFF) << 12) | 0x7C;
    command = display_list++;
    command->words.w0 = 0xEF000C3F;
    command->words.w1 = 0x00504244;
    command = display_list++;
    command->words.w1 = 0xFFFFFFFF;
    command->words.w0 = 0xFB000000;

    texture_t = 0;
    left_total = 0;
    right_total = 0;
    if (arg2 != 0) {
        if (D_8008FDC0 & 0x6040) {
            left_total = func_150859AC(0, 6);
            right_total = func_150859AC(1, 6);
        } else if (D_8008FDC0 & 0x100) {
            object = D_800CC2D0;
            player = 0;
            if (D_8008FD8C > 0) {
                do {
                    object_save = (s32) object;
                    value = func_150859AC(player, 3);
                    if (value < 0) {
                        value = 0;
                    }
                    if (*((u8 *) object + 0x128) == 0) {
                        left_total += value;
                    } else {
                        right_total += value;
                    }
                    player++;
                    object++;
                } while (player < D_8008FD8C);
            }
        } else {
            texture_t = 0x200;
            if (D_8008FD8C > 0) {
                team = D_800E0C00;
                record = D_8008FDD4;
                do {
                    value = *(s16 *) (record + 0x46);
                    if (value < 0) {
                        value = 0;
                    }
                    if (*team == 0) {
                        left_total += value;
                    } else {
                        right_total += value;
                    }
                    team++;
                    record += 2;
                } while (team < &D_800E0C00[D_8008FD8C]);
            }
        }
        D_800E0AA0[0] = left_total;
        D_800E0AA0[1] = right_total;
    } else {
        left_total = D_800E0AA0[0];
        right_total = D_800E0AA0[1];
    }

    display_list = func_151E86E4(display_list, 0x108, panel_y, 0x148,
                                 panel_y + 0x40, 0, texture_s_left,
                                 texture_t, 0x400, 0x400);
    display_list = func_151E86E4(display_list, 0x318, panel_y, 0x358,
                                 panel_y + 0x40, 0, 0,
                                 texture_t + texture_s_right, 0x400, 0x400);
    func_1504332C(0xC0, 0xC0, 0xC0, 0xFF);
    text_y = (panel_y >> 2) + 1;
    func_15042D94(0x4F, text_y, 0x80, &D_800ABAA0, right_total);
    func_15042D94(0xD3, text_y, 0x80, &D_800ABAA4, left_total);
    return display_list;
}

s32 func_151EA15C() {
    return 0;
}

s32 func_151EADFC() {
    return 0;
}

s32 func_151EB06C() {
    return 0;
}

u8 *func_151EB930(u8 *arg0) {
    s16 temp = D_8008FDCC;

    if (temp != 0) {
        arg0 = (u8 *) func_151EA15C(arg0, 0x6A, temp, 0);
    }
    return arg0;
}

s32 func_151EB96C() {
    return 0;
}

s32 func_151EBB50() {
    return 0;
}

s32 func_151EC178() {
    return 0;
}

s32 func_151EC1F0() {
    return 0;
}

s32 func_151EC3E8() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_215960/func_151EC648.s")

s32 func_151ED09C() {
    return 0;
}

s32 func_151ED1E0() {
    return 0;
}

s32 func_151ED29C() {
    return 0;
}

s32 func_151ED430() {
    return 0;
}

s32 func_151ED90C() {
    return 0;
}

s32 func_151EDB58() {
    return 0;
}

s32 func_151EDBDC() {
    return 0;
}

s32 func_151EDF4C() {
    return 0;
}

s32 func_151EE184() {
    return 0;
}

s32 func_151EEBE8() {
    return 0;
}

void func_151EEFF0(void) {
    D_800E9D00 = 0;
}
