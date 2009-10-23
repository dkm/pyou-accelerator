#!/usr/bin/env python
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
import optparse
from datetime import datetime
import math

pattern = "X[%s] Y[%s] Z[%s]\r"

max=15

def get_str(x):
    full = max*x/255
    empty = max-full
    s = " "*empty + "#"*full
    return s

def do_log(file, accs):
    d = datetime.now()

    sum = math.sqrt((accs[0]+accs[1]+accs[2])**2)
    norm= math.pow(sum, 1/3.)

    s = d.isoformat() + " %f %f %f %f" %(accs[0], accs[1], 
                                         accs[2], norm)
    print >>file, s


def acc_norm(acc, cal):
    return [(v - c0)/float(c1 - c0) for v, c0, c1 in zip(acc, cal[0], cal[1])]


# def acc_normalize(acc_zero, acc_one, acc):
#     r = []
#     for i in xrange(3):
#         zero = acc_zero[i]
#         one = acc_one[i]
#         u = one-zero
#         v = acc[i]
        
#         print float(v-zero)/u
#         r.append(float(v-zero)/u)
            
#     return r

def main():
    parser = optparse.OptionParser(
        usage='Usage: %prog [options]',
        description="Acceleration pyou !")
    
    parser.add_option("-l", "--log",
                      help="Log to file", metavar="FILE")
    parser.add_option("-g", "--gui",
                      help="Use Graphical User Interface",
                      action="store_true", default=False, 
                      metavar="use_gui")
    parser.add_option("-f", "--freq",
                      help="Sampling frequency in ms (defaults: 10ms)",
                      default=10, type="int",
                      metavar="sampling_freq")
    parser.add_option("-w", "--wiimote",
                      help="Wiimote BT address (ex:00:1D:BC:3B:2D:C3)",
                      metavar="wiimote_hwaddr")
    parser.add_option("-v", "--verbose",
                      help="Be verbose and display lots of garbage",
                      action="store_true", default=False,
                      metavar="verbose")
    
    (options, args) = parser.parse_args(sys.argv[1:])

    use_gui = options.gui

    sampling_freq = options.freq
    wiimote_hwaddr = options.wiimote
    verbose = options.verbose
    logfile = None

    if verbose:

        if use_gui:
            print "Will use GUI"
        else:
            print "Won't use GUI"

        if options.log != None:
            print "Will log to", options.log,
            if options.log == "-":
                print " STDOUT"
                logfile = sys.stdout
            else:
                print "EXT FILE"
                logfile = open(options.log, "w")

        else:
            print "Won't log"
        print "Sampling freq is %dms" %sampling_freq
        print "Wiimote address: ", wiimote_hwaddr


    wm = cwiid.Wiimote(wiimote_hwaddr)

    rpt_mode = 0

    rpt_mode ^= cwiid.RPT_ACC

    wm.rpt_mode = rpt_mode

    cal = wm.get_acc_cal(cwiid.EXT_NONE)

    if use_gui:
        g = Graph()

    while True:
        st = wm.state
        stn = acc_norm(st['acc'], cal)

        if use_gui:
            g.do_acc3d(st['acc'])
        if logfile != None:
            do_log(logfile, stn)

        pygame.time.wait(sampling_freq)

if __name__ == '__main__':
    sys.exit(main())
