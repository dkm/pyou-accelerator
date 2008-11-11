#!/usr/bin/env python2.5

import pygame

class Graph:
    fontheight = 20
    # These four values sould go into the configuration file
    winheight = 800     # Window height at startup
    width = 700      # Window width at startup

    bgcolor = (255,255,255)          # Background color for the window

    color = [(255,0,0), (0,255,0), (0,0,255)]

    txtcolor = (255,0,0)

    previous_points = (0,0,0)
    t = 0

    prev_display_debug = None

    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, self.fontheight)

        self.screen = pygame.display.set_mode( (self.width, self.winheight), pygame.RESIZABLE )

        pygame.display.set_caption( "Pyou Pyou" )
        self.screen.fill( self.bgcolor )

        pygame.display.flip()

    def display_debug(self, dtext):
        text = self.font.render(dtext, 1, self.txtcolor)
        pos = text.get_rect(left=0, top=self.winheight -self.fontheight - 5)

        if self.prev_display_debug:
            self.screen.fill(self.bgcolor, self.prev_display_debug)

        self.screen.blit(text, pos)

        if self.prev_display_debug:
            pygame.display.update(self.prev_display_debug)
        else:
            pygame.display.update(pos)

        self.prev_display_debug = pos

    def do_acc3d(self, accs):
        self.t += 1

        yoff = 0
        norms = [a * 250/255 for a in accs]

        pygame.draw.aaline(self.screen, self.color[0], (self.t-1, self.previous_points[0]+yoff), (self.t,norms[0]+yoff), 1)

        yoff = 250
        pygame.draw.aaline(self.screen, self.color[1], (self.t-1, self.previous_points[1]+yoff), (self.t, norms[1]+yoff), 1)

        yoff = 500
        pygame.draw.aaline(self.screen, self.color[2], (self.t-1, self.previous_points[2]+yoff), (self.t, norms[2]+yoff), 1)

        self.display_debug("X: %.3d  Y: %.3d  Z: %.3d" %accs)
        rect = pygame.Rect(self.t-1, 0, 40, self.winheight)
        pygame.display.update(rect)


        if self.t >= 700:
            self.t = 0
            self.screen.fill( self.bgcolor )

        self.previous_points = norms
