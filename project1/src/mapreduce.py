#/usr/bin/env python
import glob
import pprint
import mincemeat

###############################################################################
def input_file_contents(filename):
    """
    Reads & returns the contents of the file provided.
    """
    f = open(filename)
    try:
        return f.read()
    finally:
        f.close()



###############################################################################
input_files = glob.glob('../data/*')
datasource = dict((filename, input_file_contents(filename))
                  for filename in input_files)



###############################################################################
def mapfn(file_name, file_contents):
    """Map Function

    """
    import string
    from stopwords import allStopWords

    exclude = set(string.punctuation)
    result = {}
    for line in file_contents.splitlines():
        line_contents = line.split(':::')
        authors = line_contents[1]
        words = line_contents[2]

        for author in authors.split('::'):
            lauthor = author.lower()
            if lauthor not in result.keys():
                result[lauthor] = {}
            for word in words.split(' '):
                # Validate and sanitize the word
                vword = word.lower()
                if vword in allStopWords.keys():
                    # Stopwords should be ignored
                    continue
                if len(vword) == 1:
                    # Single letter words should be ignored
                    continue

                # Ignore punctuation characters from words
                vword = ''.join(ch for ch in vword if ch not in exclude)

                # Finally, add word in result
                if vword in result[lauthor].keys():
                    result[lauthor][vword] += 1
                else:
                    result[lauthor][vword] = 1

    for author in result.keys():
        yield author, result[author]


###############################################################################
def reducefn(author, words_dict_list):
    """Reduce Function

    """
    result = {}
    for words_dict in words_dict_list:
        for word in words_dict.keys():
            if word in result.keys():
                result[word] = result[word] + words_dict[word]
            else:
                result[word] = words_dict[word]

    return result


###############################################################################
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="password")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)
