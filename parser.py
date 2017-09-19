#! /usr/bin/env python3

import pyparsing as pp

# The pyparsing format is "bottom up" - so scroll down for the overall definition of the tune file structure and work up from there.  

comment = pp.Suppress("#") + pp.restOfLine

duration = pp.Optional(pp.Word(pp.nums)) + pp.Optional("/") + pp.Optional(pp.Word(pp.nums))
note_base= pp.Word("HABCDEFGI", exact=1)
gracenotes = pp.OneOrMore(pp.Word("habcdefgi"))

dotcut = pp.Literal(">") | pp.Literal("<")
note = pp.Optional(gracenotes) + note_base + pp.Optional(duration) #+ pp.Optional(whitespace) (worry about later)
barline = pp.Literal("|")

music_element = note | barline | dotcut

line = pp.OneOrMore(music_element) + pp.Literal("\n").suppress()

tune_type = pp.Suppress("R:") + pp.restOfLine
note_length = pp.Suppress("L:") + pp.restOfLine
meter =pp.Suppress("M:") + pp.restOfLine
tempo =pp.Suppress("Q:") + pp.restOfLine
composer = pp.Suppress("C:") + pp.restOfLine

title = pp.Suppress("T:") + pp.restOfLine 
tune_data = 	(pp.Optional(composer)("composer") & 
				pp.Optional(tune_type)("tune_type") & 
				pp.Optional(note_length)("note_length") &
				pp.Optional(meter)("meter") &
				pp.Optional(tempo)("tempo")
				)

music = pp.OneOrMore(pp.Group(line)("line"))
header = title("title") + tune_data

textblock = pp.Literal("example text")

command = pp.Suppress("%") + pp.restOfLine
tune = header + music

tunefile = ( 
			pp.OneOrMore(pp.Group(tune("tune"))) & 
			pp.ZeroOrMore(pp.Group(comment("comment"))) & 
			pp.ZeroOrMore(pp.Group(command("command"))) &
			pp.ZeroOrMore(pp.Group(textblock("textblock"))) &
			pp.StringEnd() )



