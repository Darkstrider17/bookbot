from stats import get_num_words #imports the get_num_words function from stats.py

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents    #Returns the file contents to be used later

def main():
    text = get_book_text("books/frankenstein.txt")
    count = get_num_words(text)
    print(f"{count} words found in the document")

main()