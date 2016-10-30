#!/usr/bin/python
#coding:utf-8

import gettext

import locale
import os

import unittest

from io import StringIO
from hello import *

'''
Obtenemos el lenguaje del SO
'''  
t = gettext.translation(
    'hello', 'locale',
    fallback=True,
    )
_ = t.gettext

class PyHelloTest(unittest.TestCase):
        '''Testeo de los metodos de hello
        '''
        def testNoArgument(self):
                'To test default without arguments'
                #create to redirect standard output & error
                out = [StringIO(),StringIO()] 
                main([],out)
                self.assertEqual(out[0].getvalue(),_("Hello, world!"+"\n"))

        def testTraditionalArgument(self):
                #create to redirect standard output & error
                out = [StringIO(),StringIO()]
                main(['-t'],out)
                self.assertEqual(out[0].getvalue(),_("Hello world"+"\n"))

        def testGrettingArgument(self):
                #create to redirect standard output & error
                out = [StringIO(),StringIO()]
                main(['-gPrueba Gretting'],out)
                self.assertEqual(out[0].getvalue(),_("Prueba Gretting"+"\n"))
                        
        def testWrongArgument(self):
                out = [StringIO(),StringIO()]
                with self.assertRaises(SystemExit):
                        main(['-x'],out)
                        
if __name__ == '__main__':
        unittest.main()
