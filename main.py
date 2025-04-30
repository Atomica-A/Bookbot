import sys
from stats import words_count
from stats import character_count
from stats import report


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

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


