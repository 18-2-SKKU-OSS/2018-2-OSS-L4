#python 3.6
import os
import fileinput
import sys


#check if back-up exist
if not os.path.isfile('musicbot/bot.back'):
    #if back-up is not exist
    f1 = open('musicbot/bot.back','w')
    f2 = open('musicbot/bot.py','r')
    f1.write(f2.read())
    f1.close()
    f2.close()


