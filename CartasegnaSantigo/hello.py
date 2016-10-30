#!/usr/bin/python
#coding:utf-8

#####################################################
__author__ = "Santiago Cartasegna (cartasegnals@gmail.com)"
__copyright__ = "Copyright (C) 2016 Santiago Cartasegna"
__license__ = "GPL 3.0"
__version__ = "0.1"
#####################################################

'''Libery used to parse the arguments'''
import argparse
'''Parse the text as it is written
https://docs.python.org/3.4/library/textwrap.html'''
import textwrap

'''Use to make intarnatilization work
https://docs.python.org/3.4/library/textwrap.html'''
import gettext

'''Miscellaneous operating system interface
https://docs.python.org/3.4/library/os.html'''
import os


'''Base System actions to redirect outputs and exits
https://docs.python.org/3.4/library/os.html'''
import sys


'''
This function is responsible for analyzing the various arguments
hello may receive.
Each argumment has an explination and way of beeing used
'''
def getArguments():
    parser = argparse.ArgumentParser(
        prog='hello',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=_(''' Print a friendly, customizable greeting.'''),
        epilog=textwrap.dedent(_('''\
                   Report bugs to: cartasegnals(at)gmail.com 
                   PHello home page: <> 
                   General help using GNU software: <> ''')))
    parser.add_argument('-v','--version',action='store_true',required=False,
                        help=_('display version information and exit'))

    parser.add_argument('-t','--traditional',action='store_true', required=False,
                        help=_('use traditional greeting'))


    parser.add_argument('-g','--greeting',action="store",dest='text', required=False,
                        help=_('use TEXT as the greeting message'))

    #parser.print_help()
    return parser


'''
In case it is invoced, prepares the hello.py version output
'''
def printVersion():
    __year__="2016"
    version =(_("""
Copyright (C) {} Cartasegna Luis Santiago.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""").format(__year__))
    return version


'''
DEPRACATED: use to test the diferent locale configurations
'''
def getLocale():
    locale.setlocale(locale.LC_ALL, '')

    print('Environment settings:')
    for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
        print('\t{} = {}'.format(
            env_name, os.environ.get(env_name, ''))
        )
    
'''
Gets the locale configuration to make translation work (in case the
especific hello.mo / po trasntaltion is on the sistem
'''
t = gettext.translation(
    'hello', 'locale',
    fallback=True,
    )
_ = t.gettext


'''
Main hello implementation
'''
def main(args_list,streams=None):

    #Added to redirect hello output to unit testing
    if streams:
        sys.stdout = streams[0]
        sys.stderr = streams[1]

    #define the default salutation
    greeting = _("Hello, world!"+"\n")

    #get the argument passed to the program
    parser = getArguments()
    results = parser.parse_args(args_list)
    
    
    if results.text != None:
        greeting = results.text +"\n"
    if results.version:
        greeting = printVersion()
    if results.traditional:
        greeting = _("Hello world"+"\n")

    sys.stdout.write(greeting)

if __name__=='__main__':
    main(sys.argv[1:])
