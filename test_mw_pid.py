#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:16:15 2017

@author: acseckin
"""

from Pmwii import MultiWii
import time
vals=[0,0,0,0,0,0,0,0,0]
mw = MultiWii("/dev/ttyO1")
i=0
bt=time.time()
ct=time.time()
while True:
    if time.time()-ct>1:
        pidval=mw.getPID()
        print ">Read:",pidval
        ct=time.time()
        if i>=20:
            break
    if time.time()-bt>5:
        i=i+1
        print i
        vals[:]=[i for x in vals]
        mw.setPID(vals)
        print ">Write",vals
        bt=time.time()
        time.sleep(1)
