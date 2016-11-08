#!/usr/bin/python
#coding:utf-8

#####################################################
__author__ = "Santiago Cartasegna (cartasegnals@gmail.com)"
__copyright__ = "Copyright (C) 2016 Santiago Cartasegna"
__license__ = "GPL 3.0"
__version__ = "0.1"
__year__ = "2016"
#####################################################

import argparse
'''Liberia usada para parsear el texto TAL CUAL SE VE en el codigo'''
import textwrap
import gettext

def obtenerParametros():
    parser = argparse.ArgumentParser(
            prog='hello',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=''' Print a friendly, customizable greeting.''',
            epilog=textwrap.dedent('''\
                      Report bugs to:null@null 
                      PHello home page: <> 
                      General help using GNU software: <> '''))

    parser.add_argument('-v','--version',action="store_true",required=False,
                    help='display version information and exit')
    parser.add_argument('-t','--traditional',dest='', required=False,
                    help='use traditional greeting')
    parser.add_argument('-g','--greeting',action="store",dest='text', required=False,
                    help='use TEXT as the greeting message')

    return(parser.parse_args())


def definirLenguaje():
    t = gettext.translation(
    'hello', 'locale',
    fallback=True,
    )
    catalogs = gettext.find('hello', 'locale', all=True)
    print('Catalogs:', catalogs)
    _ = t.gettext
    print(_('This message is in the script2.'))
    
def printVersion():
    #print(__author__)
    #print(__copyright_)
    print(_("""
Copyright (C) {} Cartasegna Luis Santiago.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""").format(__year__))

results = obtenerParametros()                                   
print(results)

definirLenguaje()

if results.text != None:
    print(results.text)
else:
    print("No hay nada en TEXT")

if results.version==True:
    printVersion()


