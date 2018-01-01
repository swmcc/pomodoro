#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import datetime
import os
import time

WORK_IN_SECS = 1200 
BREAK_IN_SECS = 300 
STATS_CSV_FILE = "/Users/swm/Dropbox/pomodoro_stats.csv"

def get_to_work():
    _announce('start working!')
    _record()
    time.sleep(WORK_IN_SECS)

def take_a_break():
    _announce('take a break')
    _record('break')
    time.sleep(BREAK_IN_SECS)

def _announce(message='Start working!'):
    os.system('say %s' % message)

def _record(type='pomodoro'):
    writer = open(STATS_CSV_FILE,'a')
    writer.seek(0,2)
    writer.writelines("\r")
    writer.writelines((',').join([_current_date(),_current_time(),type,]))

def _current_date():
    return _current_datetime().strftime('%Y-%m-%d') 

def _current_time():
    return _current_datetime().strftime('%H:%M')

def _current_datetime():
    return datetime.datetime.now()

if __name__ == '__main__':
    while 1:
        get_to_work()
        take_a_break()
