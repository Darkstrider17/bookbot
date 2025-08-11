import sys

if len(sys.argv) != 2:  #checks for the correct arguments - in this case, a path to the book being read
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


from stats import get_num_words, character_count, clean_list #imports the named functions from stats.py

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents    #Returns the file contents to be used later

def main():
    text = get_book_text(sys.argv[1])
    count = get_num_words(text)
    characters = character_count(text)
    sorted_char_list = clean_list(characters)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
    
    


main()