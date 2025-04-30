from stats import words_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    count = words_count(text)
    print(f"{count} words found in the document")


main()



