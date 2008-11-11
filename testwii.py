#!/usr/bin/env python2.5
import cwiid
import time
import sys
from testpygame import Graph
import pygame

pattern = "X[%s] Y[%s] Z[%s]\r"

max=15

def get_str(x):
    full = max*x/255
    empty = max-full
    s = " "*empty + "#"*full
    return s

wiimote_hwaddr = "00:1D:BC:3B:2D:C3"

wm = cwiid.Wiimote(wiimote_hwaddr)

rpt_mode = 0

rpt_mode ^= cwiid.RPT_ACC

wm.rpt_mode = rpt_mode

g = Graph()

while True:
    st = wm.state

    g.do_acc3d(st['acc'])
    pygame.time.wait(10)
#     print pattern %(get_str(st['acc'][0]),
#                     get_str(st['acc'][1]),
#                     get_str(st['acc'][2])),
#     sys.stdout.flush()
