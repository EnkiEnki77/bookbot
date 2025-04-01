def get_book_text(filepath:str) -> str:

    with open(filepath) as f:
        file_content = f.read()

    return file_content

def get_book_word_count(book_content:str) -> int:
    """Takes a books content as input and returns the number of words in that content"""

    words = book_content.split(" ")

    return len(words)