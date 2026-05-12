import sys

from stats import get_num_characters, get_num_words, sort_list_dictionary


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    character_count = get_num_characters(book_text)
    dictionary_to_list = sort_list_dictionary(character_count)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for key in dictionary_to_list:
        character = key["char"]
        num = key["num"]
        print(f"{character}: {num}")
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        read_file = f.read()
    return read_file


main()
