#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import argparse


def error():
    print ('Usage: set-target <trgtdc/trgt1/trgt2/trgt3> <New Target IP> <bash/zsh>')
    exit()

# now you can import and use this specific function, set_target
def set_target(trgt_old, trgt_new, rc)
    try:
        if trgt_old and trgt_new:
        #if sys.argv[1] and sys.argv[2]:
            #TRGT_REPLACE = sys.argv[1]
            TRGT_REPLACE = trgt_old
            if TRGT_REPLACE not in ['trgtdc', 'trgt1', 'trgt2', 'trgt3']:
                error()
    
            #TRGT_IP = sys.argv[2]
            TRGT_IP = trgt_new

            if rc in ['zsh', 'ZSH' 'Zsh']:
                with open(f'/home/{os.getlogin()}/.zshrc') as f:
                    for l in f.readlines():
                        if TRGT_REPLACE in l and '=' in l:
                            old_ip = l.split('=')[1].strip('\n')
                            os.system(f"sudo sed -i 's/{TRGT_REPLACE}={old_ip}/{TRGT_REPLACE}={TRGT_IP}/g' /home/{os.getlogin()}/.zshrc")
                            print ('{}: {} --> {}'.format(TRGT_REPLACE, old_ip,
                                    TRGT_IP))
                            exit()
                            
            elif rc in ['bash', 'Bash']:
                with open(f'/home/{os.getlogin()}/.bashrc') as f:
                    for l in f.readlines():
                        if TRGT_REPLACE in l and '=' in l:
                            old_ip = l.split('=')[1].strip('\n')
                            os.system(f"sudo sed -i 's/{TRGT_REPLACE}={old_ip}/{TRGT_REPLACE}={TRGT_IP}/g' /home/{os.getlogin()}/.bashrc")
                            print ('{}: {} --> {}'.format(TRGT_REPLACE, old_ip,
                                    TRGT_IP))
                            exit()
        else:
            error()

    except IndexError:
        error()

def main():
    set_target(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()
