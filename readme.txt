ace-query.py
by Austin Erickson

last updated 4/11/18

A python 2.7 Script

------FUNCTION------
This script searches dbpedia for a keyword, and returns 
the ontological classes that the keyword falls under. 
It does this by returning the type of the keyword as 
described by http://www.w3.org/1999/02/22-rdf-syntax-ns#type
and the subject of the keyword as described by
http://purl.org/dc/terms/subject

------USAGE------
from command line, type:
	python ace-query.py q
where q is the keyword to search. 

------KEYWORDS------
Most dbpedia articles begin with a capital letter. 
Because of this, the keyword must begin with a capital.
If the keyword is a phrase, capitalize the first letter,
insert underscores ('_') characters as spaces, and use
lowercase letters for all other words in the phrase.
	ex1. alligator
	python ace-query.py	Alligator

	ex2. american crocodile
	python ace-query.py American_crocodile
	
