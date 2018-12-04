#python 3.6
import os
import fileinput
import sys

def filecheck(filename):
    if filename == 'custom_command.txt':
        filepath = 'config/'
    else:
        filepath = 'musicbot/'

    if not os.path.isfile(filepath + filename):
        print('Cannot find file',filename)
        exit(1)

#configparser cannot read international characters
def readcommand(config_file):
    filecheck('custom_command.txt')
    f_commands = open('config/custom_command.txt',encoding='UTF8')
    lines = f_commands.readlines()

    commands = {}
    for i in lines:
        if '=' in i:
            item = i.split('=')
            #delete space, 'feff' exception, delete '\n'
            commands[item[0].replace(' ','').replace('\ufeff','')] = 'cmd_' + item[1].replace(' ','').replace('\n','')
    f_commands.close()

    return commands



#check if back-up exist
if not os.path.isfile('musicbot/bot.back'):
    #if back-up is not exist
    f1 = open('musicbot/bot.back','w')
    f2 = open('musicbot/bot.py','r')
    f1.write(f2.read())
    f1.close()
    f2.close()


