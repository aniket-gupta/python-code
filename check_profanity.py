import urllib


def read_text():
    with open('/home/aniket/github/python-code/movie_quotes.txt') as quotes:
        contents_of_file = quotes.read()
        print contents_of_file
        check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdyl.com/profanity?q='
                                + text_to_check)
    output = connection.read()

    if 'true' in output:
        print 'Profanity Alert!!'
    elif 'false' in output:
        print 'There is no curse word in your text :)'
    else:
        print 'Somthing wrong happened'


if __name__ == '__main__':
    read_text()
