#python 3.6
import os
import fileinput
import sys

#file read error handler
def filecheck(filename):
    if filename == 'custom_command.txt':
        filepath = '../config/'
    else:
        filepath = ''

    if not os.path.isfile(filepath + filename):
        print('Cannot find file',filename)
        exit(1)

#configparser cannot read international characters. code write required
def readcommand(config_file):
    filecheck('custom_command.txt')
    f_commands = open('../config/custom_command.txt',encoding='UTF8')
    lines = f_commands.readlines()

    commands = {}
    for i in lines:
        if '=' in i:
            item = i.split('=')
            #delete space, 'feff' exception, delete '\n'
            commands[item[0].replace(' ','').replace('\ufeff','')] = 'cmd_' + item[1].replace(' ','').replace('\n','')
    f_commands.close()
    return commands

#erase contents and write string in r+ file
def clearwrite(file,string):
    file.seek(0)
    file.truncate(0)
    file.write(string)

#main
#check if makred
filecheck('bot.py')
f_botpy = open('bot.py','r+',encoding='UTF8')

#if modified, restore back-up
if "#custom command" in f_botpy.readline():
    filecheck('bot.back')
    f_backup = open('bot.back', 'r', encoding='UTF8')
    clearwrite(f_botpy,f_backup.read())
# if not modified, make back-up
else:
    f_backup = open('bot.back', 'w', encoding='UTF8')
    f_backup.write(f_botpy.read())
f_botpy.close()
f_backup.close()

#modify and mark bot.py
f_botpy = open('bot.py','r+',encoding='UTF8')
strings = f_botpy.read()
commands = readcommand('../config/custom_command.txt')
for key, value in commands.items():
    strings = strings.replace(key,value)
clearwrite(f_botpy,'#custom command\n' + strings)
f_botpy.close()
