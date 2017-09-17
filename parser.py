#! /usr/bin/env python3

import pyparsing as pp

# The pyparsing format "bottom up" - so scroll down for the overall definition of the tune file structure and work up from there.  

comment = "#" + pp.restOfLine

duration = pp.Optional(pp.Word(pp.nums)) + pp.Optional("/") + pp.Optional(pp.Word(pp.nums))
note_base= pp.Word("HABCDEFGI", exact=1)
gracenotes = pp.OneOrMore(pp.Word("habcdefgi"))

dotcut = pp.Literal(">") | pp.Literal("<")
note = pp.Optional(gracenotes) + note_base + pp.Optional(duration)
barline = pp.Literal("|")

music_element = note | barline | dotcut

line = pp.OneOrMore(music_element) + pp.Optional(comment) + pp.LineEnd()

tune_type ="R:" + pp.restOfLine
note_length ="L:" + pp.restOfLine
meter ="M:" + pp.restOfLine
tempo ="Q:" + pp.restOfLine
composer = "C:" + pp.restOfLine

title = "T:" + pp.restOfLine 
tune_data = 	(pp.Optional(composer) & 
				pp.Optional(tune_type) & 
				pp.Optional(note_length) &
				pp.Optional(meter) &
				pp.Optional(tempo)
				)

music = pp.OneOrMore(pp.Group(line))
header = title + tune_data

textblock = pp.Literal("example text")

command = "%" + pp.restOfLine
tune = header + music

tunefile = ( 
			pp.OneOrMore(pp.Group(tune("tune"))) & 
			pp.ZeroOrMore(comment) & 
			pp.ZeroOrMore(command) &
			pp.ZeroOrMore(textblock) &
			pp.StringEnd() )



