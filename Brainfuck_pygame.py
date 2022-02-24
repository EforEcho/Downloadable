#------[ Brainfuck IDE ]------#

#-- imports ------------------#
import pygame
from pygame.constants import *
import os
import threading
import json
import locale
from Engine import *
#-----------------------------#

print(locale.getdefaultlocale())

#-- pygame --#
pygame.init()

size = [1280, 720]
win = pygame.display.set_mode(size)
fullscreen = False

flag = True
Clock = pygame.time.Clock()

#-- Surfaces --#
class Surface:
    def __init__(self, size):
        self.size_ = size
        self.surf = pygame.Surface(size)
    def size(self, size):
        self.size_ = size

        self.surf = pygame.Surface(size)

editor = Surface([1280 ,565])
menu = Surface([1280, 45])
output = Surface([1280, 110])
File = Surface([1280, 720])

#-- options --#
fps = False

#-- Colors --#
#--[ constants ]--#
bg = '#1e1e23'
bg_l = '#2d2d37'
bg_d = '#18181c'
fg = '#c8c8c8'
fg_d = '#b4b4b4'
mint = '#cfffe5'
berry = '#e31b5b'
    
#--[ variables ]--#
accent = berry


#-- fonts --#
code_f = pygame.font.SysFont('consolas', 16)
main_f = pygame.font.SysFont('consolas', 12)
indicator = pygame.font.SysFont('consolas', 8)
num_1 = pygame.font.SysFont('consolas', 18)
num_2 = pygame.font.SysFont('consolas', 12)
num_3 = pygame.font.SysFont('consolas', 10)

#-- Variables
line_ = 0
cursor_pos = 0

#-- Mod Keys --#
LCTRL = False
LALT = False
RALT = False
LSHIFT = False

#-- Brainfuck --#
interpret = None
inp = ''
output_string = ''
loop = []

#-- Cell --#
cell = 30000 * [0]
cell_ = 0

#-- Code --#
code = [char for char in inp]
code_ = 0

mode = 'file'

#-- Main Loop --#
while flag:
    if mode == 'edit':
        if line_ < 0:
            line = 0
        
        if line_ + 1 > len(line):
            line.append('')

        if cursor_pos < 0:
            cursor_pos = 0
    
        line_surf = []

    events = Event.get_events()
    if events['QUIT']:
        flag = False
        pygame.quit()
        break
    if mode == 'file':
        for key in events['Keydown']:
            pass

    for event in pygame.event.get():
        #-- Quit --#
        if event.type == QUIT:
            flag = False

        #-- Key Down --#
        elif event.type == KEYDOWN:
            #-- Mod Keys --#
            if event.key == K_LCTRL:
                LCTRL = True
            elif event.key == K_RALT:
                RALT = True
            elif event.key == K_LSHIFT:
                LSHIFT = True
            elif event.key == K_LALT:
                LALT = True

            #-- If Mod Key Pressed --#
            
            #-- Right Alt --#
            if LALT:
                if event.key == K_RETURN:
                    fullscreen = not fullscreen
                    if fullscreen:
                        size = [1920, 1080]
                        pygame.display.set_mode(size, FULLSCREEN)
                        menu.size([1920, 45])
                        editor.size([1920, 925])
                        output.size([1920, 110])
                    else: 
                        size = [1280, 720]
                        pygame.display.set_mode(size, SHOWN)
                    
            elif RALT:
                if event.key == K_BACKSPACE:
                    line[line_] = line[line_][:cursor_pos - 1 if cursor_pos > 0 else cursor_pos] + line[line_][cursor_pos:]
                    cursor_pos -= 1
                elif event.key == K_DELETE:
                    line[line_] = line[line_][:cursor_pos] + line[line_][cursor_pos + 1:]
                elif event.key == K_RETURN:
                    line_ += 1
                    line.append('')
                    cursor_pos = len(line[line_])


                #-- interpret --#
                elif event.key == K_F5:
                    inp = ''
                    output_string = ''
                    for string in line:
                        inp += string
                        interpret = True
                         #-- Cell --#
                        cell = []
                        cell_ = 0
                        
                        #-- Code --#
                        code = [char for char in inp]
                        code_ = 0
                        
                        #-- loop --#
                        loop = []
                        
                        
                        output = ''

                #-- Check Mod Keys--#
                elif event.key == K_RALT:
                    pass
                elif event.key == K_LCTRL:
                    pass
                elif event.key == K_LSHIFT:
                    pass

                #-- Moving Cursor
                elif event.key == K_UP:
                    line_ -= 1
                    if line_ + 1 > len(line):
                        line.append('')
                    cursor_pos = len(line[line_])
                elif event.key == K_DOWN:
                    line_ += 1
                    if line_ + 1 > len(line):
                        line.append('')
                    cursor_pos = len(line[line_])
                elif event.key == K_LEFT:
                    cursor_pos -= 1
                elif event.key == K_RIGHT:
                   cursor_pos += 1
                   if cursor_pos > len(line[line_]):
                       cursor_pos = len(line[line_])
                else: 
                    line[line_] = line[line_][:cursor_pos] + event.unicode + line[line_][cursor_pos:]
                    cursor_pos += 1

            #-- Control --#
            elif LCTRL:
                if event.key == K_BACKSPACE:
                    line[line_] = line[line_][cursor_pos:]
                    cursor_pos = 0
                elif event.key == K_DELETE:
                    line[line_] = line[line_][:cursor_pos]
                elif event.key == K_LEFT:
                    cursor_pos = 0
                elif event.key == K_RIGHT:
                    cursor_pos = len(line[line_])

                elif event.key == K_s:
                    with open('scripts/test.txt', 'w') as f:
                        for line__ in line:
                            f.write(f'{line__}\n')
                        f.close()


            #-- None --#
            else:
                if event.key == K_BACKSPACE:
                    line[line_] = line[line_][:cursor_pos - 1 if cursor_pos > 0 else cursor_pos] + line[line_][cursor_pos:]
                    cursor_pos -= 1
                elif event.key == K_DELETE:
                    line[line_] = line[line_][:cursor_pos] + line[line_][cursor_pos + 1:]
                elif event.key == K_RETURN:
                    line_ += 1
                    line.append('')
                    cursor_pos = len(line[line_])

                #-- interpret --#
                elif event.key == K_F5:
                    inp = ''
                    output_string = ''
                    for string in line:
                        inp += string
                        interpret = True
                         #-- Cell --#
                        cell = 30000 * [0]
                        cell_ = 0
                        
                        #-- Code --#
                        code = [char for char in inp]
                        code_ = 0
                        
                        #-- loop --#
                        loop = []

                #-- Check Mod Keys--#
                elif event.key == K_RALT:
                    pass
                elif event.key == K_LCTRL:
                    pass
                elif event.key == K_LSHIFT:
                    pass
                elif event.key == K_LALT:
                    pass

                #-- Moving Cursor
                elif event.key == K_UP:
                    line_ -= 1
                    if line_ + 1 > len(line):
                        line.append('')
                    cursor_pos = len(line[line_])
                elif event.key == K_DOWN:
                    line_ += 1
                    if line_ + 1 > len(line):
                        line.append('')
                    cursor_pos = len(line[line_])
                elif event.key == K_LEFT:
                    cursor_pos -= 1
                elif event.key == K_RIGHT:
                   cursor_pos += 1
                   if cursor_pos > len(line[line_]):
                       cursor_pos = len(line[line_])
                else: 
                    line[line_] = line[line_][:cursor_pos] + event.unicode + line[line_][cursor_pos:]
                    cursor_pos += 1

        #-- Key Up --#
        elif event.type == KEYUP:
            if event.key == K_LCTRL:
                LCTRL = False
            elif event.key == K_LALT:
                LALT = False
            elif event.key == K_RALT:
                RALT = False
            elif event.key == K_LSHIFT:
                LSHIFT = False

    if interpret:
        for i in range(1024):
            if code_ < len(inp):
                #-- + --#
                if code[code_] == '+':
                    cell[cell_] += 1
    
                #-- - -- #
                elif code[code_] == '-':
                    cell[cell_] -= 1
    
                #-- > --#
                elif code[code_] == '>':
                    cell_ += 1
    
                #-- < --#
                elif code[code_] == '<':
                    cell_ -= 1
    
                #-- . --#
                elif code[code_] == '.':
                    print(cell[cell_])
                    output_string += chr(cell[cell_])
    
                #-- [ --#
                elif code[code_] == '[':
                    loop.append(code_)
                
                #-- ] --#
                elif code[code_] == ']':
                    if cell[cell_] == 0: 
                        loop = loop[:-1]
                    else:
                        code_ = loop[-1]
    
                code_ += 1
                if cell[cell_] > 255:
                    cell[cell_] = 255
                if cell[cell_] < 0:
                    cell[cell_] = 0

            else:
               interpret = False

    output_ = []

    File.surf.fill(bg)
    
    if mode == 'edit':

        output.surf.fill(bg)
        editor.surf.fill(bg)
        menu.surf.fill(bg_d)
        
        #-- menu --#
        pygame.draw.line(menu.surf, accent, [0, 44], [menu.size_[0], 44], 3)

        #-- editor --#
        for string in line:
            line_surf.append(code_f.render(string, True, fg))
        for render in range(len(line_surf)):
            editor.surf.blit(line_surf[render], [0, render * 16])
        pygame.draw.line(editor.surf, fg, [cursor_pos * 9, line_ * 16 + 16], [cursor_pos * 9, line_ * 16 + 2], 2)

        #-- output --#
        pygame.draw.rect(output.surf, bg_l, [0, 0, output.size_[0], 110], 4)
        pygame.draw.rect(output.surf, bg_l, [0, 0, output.size_[0], 20])

        cap_out = main_f.render('Output', True, fg)
        output.surf.blit(cap_out, [8, 4])

        for cell_out in range(64):
            num = indicator.render(str(cell_out), True, fg_d)
            output.surf.blit(num, [22 * cell_out + 20 - 3 * len(str(cell_out)), 24])

        for cell_out in range(64):
            if len(str(cell[cell_out])) == 1:
                output_.append(num_1.render(str(cell[cell_out]), True, fg))
            elif len(str(cell[cell_out])) == 2:
                output_.append(num_2.render(str(cell[cell_out]), True, fg))
            elif len(str(cell[cell_out])) == 3:
                output_.append(num_3.render(str(cell[cell_out]), True, fg))
        for cell_out in range(64):
            if len(str(cell[cell_out])) == 1:
                output.surf.blit(output_[cell_out], [22 * cell_out + 14, 36])
            elif len(str(cell[cell_out])) == 2:
                output.surf.blit(output_[cell_out], [22 * cell_out + 12, 40])
            elif len(str(cell[cell_out])) == 3:
                output.surf.blit(output_[cell_out], [22 * cell_out + 10, 40])

        for cell_out in range(64):
            pygame.draw.rect(output.surf, fg, [22 * cell_out + 8, 34, 22, 22], 1)

        pygame.draw.polygon(output.surf, fg, [[22 * cell_ + 14, 66], [22 * cell_ + 18, 60], [22 * cell_ + 22, 66]])

        #-- win --#
        output_render = main_f.render(output_string, True, fg)
        output.surf.blit(output_render, [8, 90])

        win.blit(output.surf, [0, size[1]-110])
        win.blit(editor.surf, [0, 45])
        win.blit(menu.surf, [0, 0])

    if mode == 'file':
        win.blit(File.surf, [0, 0])

    #--[ FPS ]--#
    if fps:
        Fps = Clock.get_fps()
        Fps_render = code_f.render(str(int(Fps)), True, fg)
        win.blit(Fps_render, [size[0]-30, 0])

    pygame.display.update()
    
    Clock.tick(60)