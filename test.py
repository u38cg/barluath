#! /usr/bin/env python3

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
print(parse_result.dump())


