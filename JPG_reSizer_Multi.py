#!/usr/local/bin/env python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------
Filename:       JPG_reSizer_Multi.py
Author:         Martin Walch
Release Date:   2016-04-14
Description:    Iterates through a directory tree, and resizes all jpegs in place.
                
                Fullsize  Nikon D3200 file 	= 	4512 x 3000 	pixels.
             

Attributions:   dirwalk.py borrowed from the ActiveState Python Cookbook:
                http://code.activestate.com/recipes/105873/

---------------------------------------------------------------------------------------------------
"""
from __future__ import generators
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import EXIF, os, shutil
import dirwalk
from PIL import *
from multiprocessing import Pool

namePath = []
newSize = (1920,1278)
quality = 100

#inputDir = root directory that will be parsed (includes subdirectories)
#files are resized and original is overwritten
inputDir = '/Users/pyDev/Documents/JPG_TIMESLICERY/JPG_TimeSlice_Multi/input/08'     
#fileExt = '.jpg'        #restrict to .jpg's - the result of JPG_timeNamer.py                                                         


pictureList = dirwalk.dirwalk(inputDir)



count = 0


def reSize(name):

    img = Image.open(name)
    img = img.resize((newSize), Image.LANCZOS)
    img.save(name, 'jpeg', quality = quality)
    
    print 'Processed ', count, name
    print



def Timer(start, end):
    """
    Calculates the time it takes to run a process, based on start and finish times
    ---------------------------------------------------------------------------------------------
    Inputs:
    start:        Start time of process
    end:          End time of process
    ---------------------------------------------------------------------------------------------
    """
    elapsed = end - start
    # Convert process time, if needed
    if elapsed <= 59:
        time = str(round(elapsed,2)) + " seconds\n"
    if elapsed >= 60 and elapsed <= 3590:
        min = elapsed / 60
        time = str(round(min,2)) + " minutes\n"
    if elapsed >= 3600:
        hour = elapsed / 3600
        time = str(round(hour,2)) + " hours\n"
    return time


##### RUN #####

if __name__ == '__main__':
    start = time.clock()

    print '   '
    print 'Running JPG_reSizer_Multi.py   '
    print '   '

    pool = Pool()
    pool.map(reSize, pictureList)
    pool.close()
    pool.join()




    finish = time.clock()

    print '\nProcessing done in ', Timer(start, finish)
    print 'Images processed: ', str(count)




"""
if __name__ == '__main__':
    start = time.clock()

    print '   '
    print 'Running JPG_reSizer_Multi.py   '
    print '   '



    for name in pictureList:
        reSize(name)
        count +=1

        

    finish = time.clock()

    print '\nProcessing done in ', Timer(start, finish)
    print 'Images processed: ', str(count)
"""


