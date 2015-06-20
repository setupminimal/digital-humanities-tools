Digital Humanities Tools
========================

This is a set of tools that I have created to help my mother (Sparrow F. Alden, https://wordsthatyouweresaying.wordpress.com/) with her masters degree researching the use of language in Tolkein's writing.

These tools are provided in the public domain, to make them easyer to use with any research projects they may help with.

Rundown of the Tools
====================

concordance.py
--------------

This script should be run with 'python concordance.py'.
It will ask for the location of a stopword file, a list of words to be ignored, and then a location of a file to parse.
It will create a concordance in the style of my mother from any properly formatted text file with phrases separated with 'xx' and paragraphs with '[paragraph-label]'.
An example of a properly marked paragraph:
>	[01.123] xx The fish loved to eat chese. xx A nonsensical fire, xx the ashes of which would fertilize xx the crops of the dead, xx was used as an example. xx Good luck. xx
It will then ask for a location of the output file, which will be a csv file.

goToWord.py
-----------

This script will extract a small portion of text around a specified position in a text.
It will ask for a file to look through, and then ask for a number of a word.
Run it as 'python goToWord.py'

markWords.py
------------

This script will take a file to replace words in, a list of words to replace, a marker to replace them with, and a location to put the finished result.
This script is useful for marking large texts with tags that other analysis software can search on and manipulate.
Run it as 'python markWords.py'

Final Note
==========

While these scripts are provided with no warenty, or claim of usefulness, if you have questions about using them, or improvements to suggest, feel free to email setupminimal@gmail.com.
