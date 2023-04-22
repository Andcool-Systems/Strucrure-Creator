import pygame
import sys
import math, time
import os
from tkinter import filedialog
import tkinter
screen = pygame.display.set_mode((1500, 1000), pygame.RESIZABLE)
pygame.font.init()
start_dir = os.getcwd()
try:
    os.chdir(sys._MEIPASS)
    import block
    block_dat, blocks_name = block.load()
    pygame_icon = pygame.image.load('data/textures/blocks/stone.png')
    pygame.display.set_icon(pygame_icon)
    save = pygame.image.load('data/textures/save.png').convert_alpha()
    export = pygame.image.load('data/textures/export.png').convert_alpha()
    load = pygame.image.load('data/textures/load.png').convert_alpha()
    grass_block_overlay = pygame.image.load('data/textures/blocks/grass_overlay/grass_block_overlay.png').convert_alpha()
    f3 = pygame.font.Font('data/fonts/PressStart2P-Regular.ttf', 10)
    leaves_list = []
    for x in range(8):
        leaves_list.append(pygame.image.load(f'data/textures/blocks/trees/{x}.png').convert_alpha())
except Exception:
    import block
    block_dat, blocks_name = block.load()
    pygame_icon = pygame.image.load('data/textures/blocks/stone.png')
    pygame.display.set_icon(pygame_icon)
    save = pygame.image.load('data/textures/save.png').convert_alpha()
    export = pygame.image.load('data/textures/export.png').convert_alpha()
    load = pygame.image.load('data/textures/load.png').convert_alpha()
    grass_block_overlay = pygame.image.load('data/textures/blocks/grass_overlay/grass_block_overlay.png').convert_alpha()
    f3 = pygame.font.Font('data/fonts/PressStart2P-Regular.ttf', 10)
    leaves_list = []
    for x in range(8):
        leaves_list.append(pygame.image.load(f'data/textures/blocks/trees/{x}.png').convert_alpha())



os.chdir(start_dir)

pygame.display.set_caption("Structure Creator v1.1")


# здесь будут рисоваться фигуры

grass_block_overlay.fill((39, 142, 42), special_flags=pygame.BLEND_RGBA_MULT)

pygame.display.update()
field_size = 10001
field = [0] * field_size
random_bl = [0] * field_size
rect_size = 20
last_press_move = False
field_pos_x = 0
field_pos_y = 0
mouse_move_x = 0
mouse_move_y = 0
map_dat = {}
for x in range(field_size):
    field[x] = [0] * field_size

for x_r in range(field_size):
    random_bl[x_r] = [0] * field_size

rect_last_x = rect_size
sel = 1


field_pos_x = (screen.get_width() / 2) - (field_size * rect_size / 2)
field_pos_y = (screen.get_height() / 2) - (field_size * rect_size / 2)
move_x = 150
move_y = 150
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 5:
                if rect_size > 18:
                    rect_size -= 3
                    field_pos_x += move_x
                    field_pos_y += move_y
            if i.button == 4:
                if rect_size < 100:
                    rect_size += 3
                    field_pos_x -= move_x
                    field_pos_y -= move_y
            if i.button == 1:
                files = [('Python Files', '*.py')]
                
                rect_btn = pygame.Rect(screen.get_width() - 180, 5, 180, 60)
                if rect_btn.collidepoint(pygame.mouse.get_pos()):
                    

                    top = tkinter.Tk()
                    top.withdraw()  # hide window
                    file_name = tkinter.filedialog.asksaveasfile(parent=top, filetypes = files, defaultextension = files)
                    top.destroy()
                    if file_name != None:
                        f = open(file_name.name, 'w')
                        f.write("import random" + '\n')
                        f.write("def structure(map1, y, x):" + '\n')
                        f.write("	air = [0, 11, 22, 23, 24, 25, 26, 27, 10, 31]" + '\n')
                        f.write("	try:" + '\n')
                        for key_map in map_dat:
                            
                            x, y = key_map.split("/")
                            x, y = int(x), int(y)
                            x_wr = (round(field_size / 2) - y) * -1
                            y_wr = (round(field_size / 2) - x) * -1

                            if x_wr > 0: x_txt = " + " + str(x_wr)
                            elif x_wr == 0:  x_txt = ""
                            else: x_txt = " - " + str(abs(x_wr))

                            if y_wr > 0: y_txt = " + " + str(y_wr)
                            elif y_wr == 0:  y_txt = ""
                            else: y_txt = " - " + str(abs(y_wr))
                            if random_bl[x][y] == 0:
                                f.write(f"		map1[x{x_txt}][y{y_txt}] = {field[x][y] if field[x][y] != -1 else 0}" + '\n')
                            elif random_bl[x][y] == -2: 
                                f.write(f"		if random.randint(0, 1) == 1: map1[x{x_txt}][y{y_txt}] = {field[x][y] if field[x][y] != -1 else 0}" + '\n')
                            elif random_bl[x][y] == -3:
                                f.write(f"		counter = 0" + '\n')
                                f.write(f"		while map1[x{x_txt} + counter][y{y_txt}] in air:" + '\n')
                                f.write(f"			map1[x{x_txt} + counter][y{y_txt}] = {field[x][y] if field[x][y] != -1 else 0}" + '\n')
                                f.write(f"			counter += 1" + '\n')
                        f.write("	except: pass" + '\n')
                        f.write("	return map1" + '\n')
                        
                        f.close()

                rect_btn = pygame.Rect(screen.get_width() - 180, 70, 180, 60)
                if rect_btn.collidepoint(pygame.mouse.get_pos()):
                    top = tkinter.Tk()
                    top.withdraw()  # hide window
                    files_l = [('Structure file', '*.structure')]
                    file_name1 = tkinter.filedialog.asksaveasfile(parent=top, filetypes = files_l, defaultextension = files_l)
                    top.destroy()
                    if file_name1 != None:
                        f_s = open(file_name1.name, 'w')
                        print(f_s)
                        
                        for key_map in map_dat:
                            x, y = key_map.split("/")
                            x, y = int(x), int(y)
                            x_wr = (round(field_size / 2) - y) * -1
                            y_wr = (round(field_size / 2) - x) * -1
                            if random_bl[x][y] < -1:
                                f_s.write(f"{x}/{y}/{random_bl[x][y]}" + '\n')
                            
                            f_s.write(f"{x}/{y}/{field[x][y]}" + '\n')
                        
                        
                        f_s.close()
                rect_btn = pygame.Rect(screen.get_width() - 180, 135, 180, 60)
                if rect_btn.collidepoint(pygame.mouse.get_pos()):
                    files_o = [('Structure file', '*.structure')]
                    top = tkinter.Tk()
                    top.withdraw()  # hide window
                    file_name_o = tkinter.filedialog.askopenfile(parent=top, filetypes = files_o, defaultextension = files_o)
                    top.destroy()
                    if file_name_o != None:
                        f_o = open(file_name_o.name, 'r')

                        for line in f_o:
                            x, y, dat = line.split("/")
                            x, y, dat = int(x), int(y), int(dat)
                            if dat < -1:
                                    random_bl[x][y] = dat
                            field[x][y] = dat
                            map_dat.update({f"{x}/{y}": dat})
                        f_o.close()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_c:
                for x in range(field_size):
                    field[x] = [0] * field_size
            if i.key == pygame.K_w:
                rect_size = 20
                field_pos_x = (screen.get_width() / 2) - (field_size * rect_size / 2)
                field_pos_y = (screen.get_height() / 2) - (field_size * rect_size / 2)    

    

        
    pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()



    if pressed[1]:
        field_pos_x += mouse_x - mouse_move_x
        field_pos_y += mouse_y - mouse_move_y


    for y1 in range(round(screen.get_height() / rect_size) + 2):
        for x1 in range(round(screen.get_width() / rect_size) + 2):
            x = x1 + round(abs(field_pos_x) / rect_size) - 1
            y = y1 + round(abs(field_pos_y) / rect_size) - 1
            rect = pygame.Rect(x * rect_size + field_pos_x, y * rect_size + field_pos_y, rect_size, rect_size)
            rect_btn = pygame.Rect(screen.get_width() - 180, 5, 180, 195)

            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            try:
                if field[x][y] != 0:
                    if field[x][y] == 10:
                        for x_leaves in range(8):
                            screen.blit(pygame.transform.scale(leaves_list[x_leaves], (rect_size, round(rect_size / 8))), 
                                                            (round(math.sin(time.time() * 5 + x_leaves) * round(rect_size * 2 / 64)) + (x * rect_size + field_pos_x), x_leaves * round(rect_size / 8) + (y * rect_size + field_pos_y)))
                    elif field[x][y] == 17:
                        screen.blit(pygame.transform.scale(block_dat[9], (rect_size, rect_size)), (x * rect_size + field_pos_x, y * rect_size + field_pos_y))
                        for x_leaves in range(8):
                            screen.blit(pygame.transform.scale(leaves_list[x_leaves], (rect_size, round(rect_size / 8))), 
                                                            (round(math.sin(time.time() * 5 + x_leaves) * round(rect_size * 2 / 64)) + (x * rect_size + field_pos_x), x_leaves * round(rect_size / 8) + (y * rect_size + field_pos_y)))
                    

                    elif field[x][y] == 29:
                        screen.blit(pygame.transform.scale(block_dat[28], (rect_size, rect_size)), (x * rect_size + field_pos_x, y * rect_size + field_pos_y))
                        for x_leaves in range(8):
                            screen.blit(pygame.transform.scale(leaves_list[x_leaves], (rect_size, round(rect_size / 8))), 
                                                            (round(math.sin(time.time() * 5 + x_leaves) * round(rect_size * 2 / 64)) + (x * rect_size + field_pos_x), x_leaves * round(rect_size / 8) + (y * rect_size + field_pos_y)))
                            
                    elif field[x][y] == 2:
                        screen.blit(pygame.transform.scale(block_dat[field[x][y]], (rect_size, rect_size)), (x * rect_size + field_pos_x, y * rect_size + field_pos_y))
                        screen.blit(pygame.transform.scale(grass_block_overlay, (rect_size, rect_size)), (x * rect_size + field_pos_x, y * rect_size + field_pos_y))
                    else:
                        screen.blit(pygame.transform.scale(block_dat[field[x][y]], (rect_size, rect_size)), (x * rect_size + field_pos_x, y * rect_size + field_pos_y))
                if random_bl[x][y] != 0: screen.blit(pygame.transform.scale(block_dat[random_bl[x][y]], (rect_size, rect_size)), (x * rect_size + field_pos_x, y * rect_size + field_pos_y))

                if rect.collidepoint(pygame.mouse.get_pos()) and not pygame.Rect(0, screen.get_height() - 75, screen.get_width(), 75).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not rect_btn.collidepoint(pygame.mouse.get_pos()):
                    if sel > -2 and sel != 0:
                        map_dat.update({f"{x}/{y}": sel})
                        field[x][y] = sel
                    elif sel < -1:
                        random_bl[x][y] = sel
                    

                

                if rect.collidepoint(pygame.mouse.get_pos()) and not pygame.Rect(0, screen.get_height() - 75, screen.get_width(), 75).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[2] and not rect_btn.collidepoint(pygame.mouse.get_pos()):
                    if sel > -2 and sel != 0:
                        field[x][y] = 0
                        try: map_dat.pop(f"{x}/{y}")
                        except: pass
                    elif sel < -1:
                        random_bl[x][y] = 0
                    
                if rect.collidepoint(pygame.mouse.get_pos()) and not pygame.Rect(0, screen.get_height() - 75, screen.get_width(), 75).collidepoint(pygame.mouse.get_pos()) and not rect_btn.collidepoint(pygame.mouse.get_pos()): pygame.draw.rect(screen, (0, 0, 0), rect, 2)

                

                if field[x][y] == 0: random_bl[x][y] = 0
                if rect.collidepoint(pygame.mouse.get_pos()):
                    l_x = x * rect_size + field_pos_x
                    b_x = x * (rect_size + 3) + field_pos_x
                    move_x = abs(b_x - l_x)

                    l_y = y * rect_size + field_pos_y
                    b_y = y * (rect_size + 3) + field_pos_y
                    move_y = abs(b_y - l_y)

                if x == round(field_size / 2) and y == round(field_size / 2): 
                    pygame.draw.rect(screen, (255, 255, 0), rect, 3)

            except: pass
            
            
    s = pygame.Surface((screen.get_width(), 75))
    s.set_alpha(150)
    s.fill((0, 0, 0))
    screen.blit(s,(0, screen.get_height() - 75))

    x_inv = 0
    len_l = (screen.get_width() / 2) - ((len(block_dat) * 69) / 2)
    for key in block_dat:
        if key == 10:
            for x_leaves in range(8):
                screen.blit(leaves_list[x_leaves], 
                            (round(math.sin(time.time() * 5 + x_leaves) * 2) + (len_l + x_inv * 69), x_leaves * 8 + (screen.get_height() - 70)))
        elif key == 17:
            screen.blit(block_dat[9], (len_l + x_inv * 69, screen.get_height() - 70))
            for x_leaves in range(8):
                screen.blit(leaves_list[x_leaves], 
                            (round(math.sin(time.time() * 5 + x_leaves) * 2) + (len_l + x_inv * 69), x_leaves * 8 + (screen.get_height() - 70)))
                

        elif key == 29:
            screen.blit(block_dat[28], (len_l + x_inv * 69, screen.get_height() - 70))
            for x_leaves in range(8):
                screen.blit(leaves_list[x_leaves], 
                                                (round(math.sin(time.time() * 5 + x_leaves) * 2) + (len_l + x_inv * 69), x_leaves * 8 + (screen.get_height() - 70)))
        elif key == 2:
            screen.blit(block_dat[key], (len_l + x_inv * 69, screen.get_height() - 70))
            screen.blit(grass_block_overlay, (len_l + x_inv * 69, screen.get_height() - 70))
        elif key == -2:
            screen.blit(block_dat[key], (len_l + x_inv * 69, screen.get_height() - 70))
            pygame.draw.line(screen, (0, 0, 0), 
                 [len_l + x_inv * 69, screen.get_height() - 70], 
                 [len_l + x_inv * 69, screen.get_height() - 6], 3)
        else:
            screen.blit(block_dat[key], (len_l + x_inv * 69, screen.get_height() - 70))
        if pygame.Rect(len_l + x_inv * 69, screen.get_height() - 70, 64, 64).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]: 
            sel = key

        if pygame.Rect(len_l + x_inv * 69, screen.get_height() - 70, 64, 64).collidepoint(pygame.mouse.get_pos()):
            txt = f3.render(str(blocks_name[key]), True,(255, 255, 255))
            poly_txt = ((len_l + x_inv * 69) + 32) - txt.get_width() / 2
            poly_txt_half = ((len_l + x_inv * 69) + 32)
            pygame.draw.polygon(screen, (50, 50, 50), 
                    [[poly_txt - 5, 0 + (screen.get_height() - 95)], 
                     [poly_txt + 5 + txt.get_width(), 0 + (screen.get_height() - 95)], 
                     [poly_txt + 5 + txt.get_width(), 20 + (screen.get_height() - 95)], 
                     [poly_txt + txt.get_width() - (txt.get_width() / 2 - 5), 20 + (screen.get_height() - 95)],
                     [poly_txt_half, 25 + (screen.get_height() - 95)],
                     [poly_txt + txt.get_width() - (txt.get_width() / 2 + 5), 20 + (screen.get_height() - 95)],
                     [poly_txt - 5, 20 + (screen.get_height() - 95)]])
            
            txt = f3.render(str(blocks_name[key]), True,(255, 255, 255))
            screen.blit(txt, (((len_l + x_inv * 69) + 32) - txt.get_width() / 2, (screen.get_height() - 90)))
        if key == sel: pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(len_l + x_inv * 69, screen.get_height() - 70, 64, 64), 4)
        x_inv += 1

    screen.blit(export,(screen.get_width() - 180, 5))
    screen.blit(save,(screen.get_width() - 180, 70))
    screen.blit(load,(screen.get_width() - 180, 135))

    rect_btn = pygame.Rect(screen.get_width() - 180, 5, 180, 60)
    if rect_btn.collidepoint(pygame.mouse.get_pos()):
        rect_btn_s = pygame.Surface((180, 60))
        rect_btn_s.set_alpha(100)
        rect_btn_s.fill((0, 0, 0))
        screen.blit(rect_btn_s,(screen.get_width() - 180, 5))

    rect_btn = pygame.Rect(screen.get_width() - 180, 70, 180, 60)
    if rect_btn.collidepoint(pygame.mouse.get_pos()):
        rect_btn_s = pygame.Surface((180, 60))
        rect_btn_s.set_alpha(100)
        rect_btn_s.fill((0, 0, 0))
        screen.blit(rect_btn_s,(screen.get_width() - 180, 70))

    rect_btn = pygame.Rect(screen.get_width() - 180, 135, 180, 60)
    if rect_btn.collidepoint(pygame.mouse.get_pos()):
        rect_btn_s = pygame.Surface((180, 60))
        rect_btn_s.set_alpha(100)
        rect_btn_s.fill((0, 0, 0))
        screen.blit(rect_btn_s,(screen.get_width() - 180, 135))


    


    pygame.display.update()
    screen.fill((135, 206, 235))
    pygame.time.delay(16)
    mouse_move_x, mouse_move_y = pygame.mouse.get_pos()

