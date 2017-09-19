#! /usr/bin/env python3

#This file is just for scratch testing.  

import parser

f = """

# This is a comment

%COMMAND

example text

T:Title 1
R:Reel
C:Jock
M:4/4
L:1/4
A B2 gefE3/2 | gA2>gdcd f gefE2 |

#another comment

T:Title 2
A #This line finishes with a comment 
"""

parse_result = parser.tunefile.parseString(f)

for i in range(0,len(parse_result)):
	print (list(parse_result[i].asDict())[0])

