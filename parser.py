from error import *
import re

class TuneFile:
	
	def __init__(self):
		"""
		A complete file, with tunes and other elements to typeset
		
		elements: a single chunk, such as format info, a tune, text, or something else.
		"""
		self.elements = [] 
	
	def parse(self, filelines):
		"""
		Accepts a list of text lines, which make up the input tune file, then parses the list.
		"""
		
		if len(filelines)<3:
			raise TuneFileError("File too short: 3 line minimum")
		
		element = Element()
		
		for line in filelines:
			if element.new_element(line):
				self.elements.append(element)
				element = Element()
			element.parse(line)
			
class Element:
	def __init__( self ):
		self.element = None # A generic element
	
	def parse( self, text):
		
		if self.element is None:
			# Match X(ref), Title, Composer, Rhythm, Source, Info, Meter, Length (note default) information fields
			r = r'[XTMLCRSI]:.*' 
			match = re.match(r, text)
			if match:
				self.element = InfoField()
			else:
				self.element = Note()
			
		self.element.parse(text)
		
	def new_element(self, text):
		"""
		Decide if the given text is a new element or a continuation of the one we already have.
		"""
		if text == "H A B C D E F G I\n":
			return True
		else:
			return False	
		
class InfoField:
	def __init__(self):
		self.fields = {}
		
	def parse(self, text):
		r = r'([XTMLCRSI]):\s*(.*)'
		match = re.match(r, text)
		self.fields[match.group(1)] = match.group(2)
		
class Note:
	
	def __init__( self ):
		self.note = None
		
	def parse(self, text):
		self.note = text
