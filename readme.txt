ace-query.py
ace-children.py
by Austin Erickson
last updated 4/23/18

------NOTE---------
These scripts were created in python 2.7 and may not be 
compatible with python 3

===========================================================================
------General Info---------------------------------------------------------
===========================================================================
------KEYWORDS------
Most dbpedia articles begin with a capital letter. 
Because of this, the keyword parameter associated with the 
following scripts must begin with a capital letter.
If the keyword is a phrase, capitalize the first letter,
insert underscores ('_') characters as spaces, and use
lowercase letters for all other words in the phrase.
	ex1. alligator
	python ace-query.py Alligator

	ex2. american crocodile
	python ace-query.py American_crocodile

------RETURNED TYPES------
Using these scripts, data will be returned from dbpedia in
a variety of formats. 
'type':
  Statements in which the keyword exists as a subject.
  This implies an 'is-a' relationship. 
  Ex. using keyword 'Cat' the 'type' may be 'Mammal' or 'Animal'

'subject':
  Other keywords associated with the topic of the resource.
  Ex. using keyword 'Cat' the 'subject' may be 'Cosmopolitan_animals'
    or 'Invasive_mammal_species' or 'Articles_containing_video_clips'



===========================================================================
------ace-query.py---------------------------------------------------------
===========================================================================
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
where q is the keyword or list of keywords to search. 
To search multiple keywords:
	python ace-query.py q r ... s
where q, r, and all parameters up to s are keywords to search. 


===========================================================================
------ace-children.py------------------------------------------------------
===========================================================================
------FUNCTION------
This script searches dbpedia for a keyword, and returns 
the subclasses and objects associated with the keyword. 
Ex. searching 'Mammal' should return subclass 'Cats' or 'Felines'
and objects that fall under the class such as 'Domestic_cat' and
'Lion'

------USAGE------
from command line, type:
	python ace-children.py q
where q is the keyword to search. 
At this time, the script supports only a single keyword at a time.

	
