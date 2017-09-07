#! /usr/bin/env python3

import parser
import unittest

class TestClassConstruction(unittest.TestCase):
	
	def test_Note( self ):
		z = parser.Note()
		
	def test_TuneFile( self ):
		z = parser.TuneFile()
		
	def test_Element( self ):
		z = parser.Element()
		
class TestNote(unittest.TestCase):
	
	def setUp( self ):
		self.z = parser.Note()
		
	def  test_plain_note( self ):
		self.z.parse("H")
		self.assertEqual(self.z.note, "H")

class TestTuneFile(unittest.TestCase):
	def setUp( self ):
		self.tunefile = parser.TuneFile()
		with open('testfiles/tune_test_file') as f:
			self.test_tunefile = f.readlines()
		self.tunefile.parse(self.test_tunefile)
		
	def test_line_one( self ):
		self.assertEqual(self.tunefile.elements[0].element.note, "A")
	
unittest.main()
