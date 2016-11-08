#!/usr/bin/python
#coding:utf-8

#####################################################
__author__ = "Santiago Cartasegna (cartasegnals@gmail.com)"
__copyright__ = "Copyright (C) 2016 Santiago Cartasegna"
__license__ = "GPL 3.0"
__version__ = "0.1"
#####################################################

import argparse
'''Liberia usada para parsear el texto TAL CUAL SE VE en el codigo'''
import textwrap
import gettext

import locale
import os
import pprint
import sys

def getArguments():
    parser = argparse.ArgumentParser(
        prog='hello',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=''' Print a friendly, customizable greeting.''',
        epilog=textwrap.dedent('''\
                   Report bugs to:null@null 
                   PHello home page: <> 
                   General help using GNU software: <> '''))
    parser.add_argument('-v','--version',action='store_true',required=False,
                        help=_('display version information and exit'))

    parser.add_argument('-t','--traditional',action='store_true', required=False,
                        help=_('use traditional greeting'))


    parser.add_argument('-g','--greeting',action="store",dest='text', required=False,
                        help=_('use TEXT as the greeting message'))

    #parser.print_help()
    return parser

def printVersion():
    __year__="2016"
    print(_("""
Copyright (C) {} Cartasegna Luis Santiago.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""").format(__year__))


def getLocale():
    locale.setlocale(locale.LC_ALL, '')

    print('Environment settings:')
    for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
        print('\t{} = {}'.format(
            env_name, os.environ.get(env_name, ''))
        )
    


t = gettext.translation(
    'hello', 'locale',
    fallback=True,
    )
_ = t.gettext



def main(args_list,streams=None):

    if streams:
        sys.stdout = streams[0]
        sys.stderr = streams[1]

    greeting = _("Hello, world!"+"\n")

    #catalogs = gettext.find('example', 'locale', all=True)
    #print('Catalogs:', catalogs)
    #getLocale()
    parser = getArguments()
    results = parser.parse_args()
    #print(results)
    
    if results.text != None:
        greeting = results.text +"\n"
    if results.version:
       sys.stdout.write(printVersion())
    if results.traditional:
        greeting = _("Hello world"+"\n")

    sys.stdout.write(greeting)

if __name__=='__main__':
    main(sys.argv[1:])
