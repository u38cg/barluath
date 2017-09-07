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
		
	def test_info_fields( self ):
		self.assertEqual(self.tunefile.elements[0].element.fields['X'], "0")
		self.assertEqual(self.tunefile.elements[0].element.fields['T'], "Test Tune")
		self.assertEqual(self.tunefile.elements[0].element.fields['M'], "3/4")
		self.assertEqual(self.tunefile.elements[0].element.fields['L'], "1/8")
		self.assertEqual(self.tunefile.elements[0].element.fields['C'], "A. Composer")
		self.assertEqual(self.tunefile.elements[0].element.fields['R'], "Reel")
		self.assertEqual(self.tunefile.elements[0].element.fields['S'], "A book")
		self.assertEqual(self.tunefile.elements[0].element.fields['I'], "This is an information field that can be printed with the tune")
		
	def test_note_fields(self):
		self.assertEqual(self.tunefile.elements[1].element.note, "hello")
	
unittest.main()
