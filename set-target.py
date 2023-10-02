#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys


def error():
    print ('Usage: set-target <trgtdc/trgt1/trgt2/trgt3> <New Target IP>')
    exit()

try:
    if sys.argv[1] and sys.argv[2]:
        TRGT_REPLACE = sys.argv[1]
        if TRGT_REPLACE not in ['trgtdc', 'trgt1', 'trgt2', 'trgt3']:
            error()

        TRGT_IP = sys.argv[2]

        with open('/home/kali/.zshrc') as f:
            for l in f.readlines():
                if TRGT_REPLACE in l and '=' in l:
                    old_ip = l.split('=')[1].strip('\n')
                    os.system("sudo sed -i 's/{}={}/{}={}/g' /home/kali/.zshrc".format(TRGT_REPLACE,
                              old_ip, TRGT_REPLACE, TRGT_IP))
                    print ('{}: {} --> {}'.format(TRGT_REPLACE, old_ip,
                            TRGT_IP))
                    exit()
    else:

        error()
        
except IndexError:
    error()
