

def get_book_word_count(book_content:str) -> int:
    """Takes a books content as input and returns the number of words in that content"""

    words = book_content.split(" ")

    return len(words)