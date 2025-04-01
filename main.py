from modules.get_book_text import get_book_text
from modules.get_book_word_count import get_book_word_count


def main():
        print(get_book_word_count(get_book_text("./books/frankenstein.txt")))


if __name__ == "__main__":
        main()
