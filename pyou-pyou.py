#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-
# Copyright (C) 2008 Marc Poulhiès
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# Author: Marc Poulhiès

import cwiid
import time
import sys
from testpygame import Graph
import pygame
import os
import getopt

pattern = "X[%s] Y[%s] Z[%s]\r"

max=15

cliargs = [('g', 'gui', "Use Graphical User Interface"),
           ('f:', 'freq=', "Sampling frequency in ms (defaults: 10ms) "),
           ('w', 'wiimote', "Wiimote BT address (ex:00:1D:BC:3B:2D:C3)"),
           ('v', 'verbose', "Be verbose and display lots of garbage"),
           ('h','help','Displays this help text')]


def help():
    print "Wii fun stuff :p"
    for s,l,c in cliargs:
        print "-%s" %s.replace(":",""),
        if l != '':
            print "/--%s" %l.replace("=",""),
        print ""
        print "   %s" %c
        print ""

def get_str(x):
    full = max*x/255
    empty = max-full
    s = " "*empty + "#"*full
    return s




def main():
    wiimote_hwaddr = None
    sampling_freq = 10
    use_gui = False
    verbose = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "".join([x[0] for x in cliargs]),
                                   [x[1] for x in cliargs])
    except getopt.GetoptError, e:
        help()
        print e
        sys.exit(2)


    for o, a in opts:
        if o in ("-g", "--gui"):
            use_gui = True
        if o in ("-f", "--freq"):
            sampling_freq = int(a.strip())
        if o in ("-w", "--wiimote"):
            wiimote_hwaddr = a.strip()
        if o in ("-v", "--verbose"):
            verbose = True
        if o in ("-h", "--help"):
            help()
            return

    if verbose:
        if gui:
            print "Will use GUI"
        else:
            print "Won't use GUI"
        print "Sampling freq is %dms" %sampling_freq
        print "Wiimote address: ", wiimote_hwaddr

    wm = cwiid.Wiimote(wiimote_hwaddr)

    rpt_mode = 0

    rpt_mode ^= cwiid.RPT_ACC

    wm.rpt_mode = rpt_mode

    if use_gui:
        g = Graph()

    while True:
        st = wm.state
        if use_gui:
            g.do_acc3d(st['acc'])
        pygame.time.wait(10)

if __name__ == '__main__':
    sys.exit(main())
