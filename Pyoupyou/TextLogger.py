#!/usr/bin/env python2.5

class TextLogger:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")

    def log(self, timestamp, ac_values=None, gps_data=None):

