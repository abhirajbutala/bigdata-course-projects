bigdata-course-projects
=======================

Repository for 'Web Intelligence and Big Data' course projects I worked on.

More details of the course can be found here:
https://class.coursera.org/bigdata-003/class/index

Project-1
=========

Wrote a parallel map-reduce program for the task mentioned below using
mincemeat.py, which is a lightweight map-reduce implementation written in
python. More details of mincemeat are here:
https://github.com/michaelfairley/mincemeatpy

The task was to compute the term counts across titles for each author, from
the data set provided in 'data' folder.

For example, for the author 'Alberto Pettorossi' the following terms occur in
titles with the indicated cumulative frequencies (across all his papers):
program:3, transformation:2, transforming:2, using:2, programs:2, and logic:2.

Note that an author might have written multiple papers, which might be listed
in multiple files. Further notice that ‘terms’ must exclude common stop-words,
such as prepositions etc. The stop-words that need to be omitted are listed in
the script stopwords.py. In addition, single letter words, such as "a" were
ignored. Also, hyphens are ignored (i.e. deleted). Lastly, periods, commas,
etc. are ignored. Thus it means that only alphabets and numbers can be part
of a title term. For example, “program” and “program.” should both be counted
as the term ‘program’, and "map-reduce" should be taken as 'mapreduce'.
Finally, stemming is not done, i.e. "algorithm" and "algorithms" are treated
as separate terms.
