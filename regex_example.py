# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 08:12:06 2021

@author: mjach
"""

'''
RegEx

- Regular expressions also called REs, or regexes, or regex patterns
- It is available through the python re module.
- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
- Using the pattern you can specify the rules for the set of possible strings that you want to match;
- this set of string might contain English sentences, or e-mail addresses, etc ....

Here’s a complete list of the metacharacters; their meanings will be discussed
. ^ $ * + ? { } [ ] \ | ( )

Metacharacters meaning--

. Period	- A period is used to match any single character - except newline \n\r\f\v

^ Caret 	- The caret symbol ^ is used to check if a string start with certain character.
				^a 	abc	        1 match
					bac	       no match
				^ab abc      1 match
					bca	       no match

$ Dollar	- The dollar symbol is used to check if a string ends with a certain character.

				$a	baba	1 match
					baby	no match

* Star		- The star symbol is used to check to match zero or more occurances of the pattern left to it.

				ca*b 	ab		1 match
						can		no match as a is not followed by b

+ Plus		- The plus symbol + is used to matches one or more occurances of the pattern left to is.

				ca+b	cb		no match as there is no a character
						cab		1 match
						can		no match as a is not followed by b

? Question Mark		The question mark symbol is used to matches zero or one occurance of the pattern left to it.

				ca?b	cb		1 match
						cab		1 match
						caaab	No match as there are more than one a character
						can		no match as a is not followed by b

{}	Brces	- The braces is used to check repetitions of the pattern left to it.
            example {a,b} this means at least a , and at most b repetitions of the pattern left to it.

				b{2,3}	abc bca		no match
						abba baac	    1 match as there is bb pattern
						abba abbba	2 match as there are two bb and bbb pattern

[] Bracket	- This square bracket is used to specifies a set of characters you want to match.

				[abc]	a				1 match
						ab				2 match
						how are you?	1 match

			you can also specify a range of characters using - inside square brackets.
				[a-e] is the same [abcde]
				[1-5] is the same [12345]
			you can skip characters set by using caret ^ symbol at the start of a square bracket.
				[^abcd]	that means any character except a b c d
				[^0-8]	-	-	-	any non-digit character.


\ Backslash - Backslash is used to excape characters including all metacharacters.

| Alternation  - The alternation or vertical bar is used for or operator

			a|b 	efg		no match
					ade		1 match
					acbda	3 match

() Group 	- The parenthesis is used to group sub patterns.
            Example (x|y|z)abc match any string either x or y or z followed by abc

			(x|y|z)abc		xy abc 	no match
							xyabc	       1 match (match from yabc)
							xabc xzabc	2 match xabcand zabc


Special Sequences

\A	Matches if the specified characters are at the start of a string.

\b 	Matches if the specified characters are at the beginning or end of a word.

\B	Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.

\d	Matches any decimal digit; this is equivalent to the class [0-9].

\D	Matches any non-digit character; this is equivalent to the class [^0-9].

\s	Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

\S	Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

\w	Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

\W	Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

\Z Matches if the specified characters are at the end of a string. this is equivalent to the class
	Expression - Python\Z 	- I am learning Python 	match
							- I am doing Python Project - No match

NB-https://regex101.com/ - very good site to learn regex

'''

#example-1
#. Period	- A period is used to match any single character - except newline \n\r\f\v

import re

text = 'Python Programming'
result = re.findall('Py..on', text)
#print(result)

#exaple -2
#^ Caret 	- The caret symbol ^ is used to check if a string start with certain character.

caret_result = re.findall('^Python', text)
# if caret_result:
#     print('Yes the string start with P')
# else:
#     print('No..start with different character')

#example 3
#$ Dollar	- The dollar symbol is used to check if a string ends with a certain character.

doller_result = re.findall('Programming$', text)
# if doller_result:
#     print('Yes the string end with Programming')
# else:
#     print('No..end with different character')

#example 4
#* Star		- The star symbol is used to check to match zero or more occurances of the pattern left to it.

text = 'Python Programming'
start_result = re.findall('Py.*m', text)
#print(start_result)

#example 5
#+ Plus		- The plus symbol + is used to matches one or more occurances of the pattern left to is.
text = 'Python Programming'
plus_result = re.findall('Py.+h', text)
#print(plus_result)

#example 6
#? Question Mark		The question mark symbol is used to matches zero or one occurance of the pattern left to it.

#text = 'Python Programming'
text = 'banana'
question_result = re.findall('ba.?a', text)
#print(question_result)
#example 7

#{}	Brces	- The braces is used to check repetitions of the pattern left to it.
#            example {a,b} this means at least a , and at most b repetitions of the pattern left to it.

text = 'Python Programming'
brace_result = re.findall('Pro.{7}g', text)
#print(brace_result)

#example 8

#[] Bracket	- This square bracket is used to specifies a set of characters you want to match.

text = 'Python Programming'
bracket_result = re.findall('[a-h]', text)
#print(bracket_result)

#example 9
#\ Backslash - Backslash is used to excape characters including all metacharacters.
text = 'Python Programming 2021'
blackslash_result = re.findall('\d', text)
#print(blackslash_result)

#example 10
# | Alternation  - The alternation or vertical bar is used for or operator

text = 'Python Programming 2021 basic and advance learning'
#alternation_result = re.findall('NLP | machine', text)
alternation_result = re.findall('basic | machine', text)

# if alternation_result:
#     print('Yes there is a match')
# else:
#     print('No there is no match')

#\A 	Matches if the specified characters are at the start of a string.

text = 'Python Programming 2021'
result = re.search('\AProgramming', text)

if result:
    print('Yes there is a text in the begining')
else:
    print('No there is no match in the begining')
'''
The re module offers a set of functions that allows us to search a string for a match:

findall()	Returns a list containing all matches
search()	Returns a Match object if there is a match anywhere in the string
split() 	Returns a list where the string has been split at each match
sub()		Replaces one or many matches with a string
match()		Determine if the RE matches at the beginning of the string.

match() and search() return None if no match can be found. If they’re successful, a match object instance is returned
'''