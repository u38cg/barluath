# barluath

A notation tool for the great highland bagpipe.  

A very simple GUI will allow opening and editing of plain text files.  These act as inputs to the typesetter in alanguage similar to the well known ABC language, but with some changes to optimise it for writing bagpipe music.

The GUI (written in wxPython) will display SVGs and export PDFs.

Roadmap:

1. write a very basic parser
2. Build GUI
3. PDF export
4. ????
5. Profit

The code is not at present licensed until any requirements from included libraries become clear, though the intent is that it will be GPL or similar.

#Initial parser wishlist:

Info fields: 
XTMLCRSI - X(ref), Title, Composer, Rhythm, Source, Info, Meter, Length (note default)

Music
notes, gracenotes, barlines, music lines.  Leave duration until later.

Comment fields (ie do nothing) - use '>'

Command fields (eg scale, etc) - use '%'
NB command fields can occur inside a music line.

Text - any free text not identified as above is a text block. 

#Info & acknowledgements

Icons are taken (with thanks) from http://publicicons.org/

