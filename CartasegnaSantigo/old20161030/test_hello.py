#!/usr/bin/python
#coding:utf-8


import argparse
'''Liberia usada para parsear el texto TAL CUAL SE VE en el codigo'''
import textwrap
import gettext

import locale
import os

import unittest
'''
Obtenemos el lenguaje del SO
'''  
from io import StringIO
from hello import *

t = gettext.translation(
    'hello', 'locale',
    fallback=True,
    )
_ = t.gettext


greeting = _("Hello, world!")


class PyHelloTest(unittest.TestCase):
	'''Testeo de los metodos de hello
	'''
	def testSimple(self):
		'To test default without arguments'
		#create to redirect standard output & error
		out = [StringIO(),StringIO()] 
		main([],out)
		self.assertEqual(out[0].getvalue(),_("Hello, world!"))

	#def testTraditional(self):
                
        #def testFail(self):
         #       out = [StringIO(),StringIO()]
          #      with self.assertRaises(SystemExit):
           #         main(['-x'],out)
                        
if __name__ == '__main__':
	unittest.main()
