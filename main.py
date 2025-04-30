from stats import words_count
from stats import character_count
from stats import report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    count = words_count(text)
    c_count = character_count(text)
    f_report = report(c_count)
    print(f'''
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------
{f_report}
============= END ===============''')


main()



