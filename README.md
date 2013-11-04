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

Project-2
=========

Wrote a simple python program to encode the Bayesian Network mentioned in the
checked-in pdf file.

After running the python program, an sqlite3 db called test.db is generated.

Ran various SQL queries on the db to answer the questions asked in programming
quiz.

For example, the SQL query for the case where the person has Tuberculosis, given
that he has visited Asia, is a Non Smoker, has no symptoms of Dyspneoa and has
positive X-Ray, can be encoded as below:


SELECT pta.tub, SUM(pa.p * pbs.p * pdeb.p * pelt.p * pls.p * ps.p * pta.p * pxe.p)
    FROM pa,pbs,pdeb,pelt,pls,ps,pta,pxe
    WHERE pa.asia = pta.asia
        and ps.smoke = pls.smoke
        and ps.smoke = pbs.smoke
        and pls.lc = pelt.lc
        and pta.tub = pelt.tub
        and pelt.elt = pxe.elt
        and pdeb.elt = pelt.elt
        and pdeb.bron = pbs.bron
        and pa.asia = "Y" and ps.smoke = "N" and pxe.xray = "Y" and pdeb.dys = "N"
    GROUP BY pta.tub;
