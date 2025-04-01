

def get_book_text(filepath:str) -> str:
    """Reads from file at filepath returning the content of the file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()

    return file_content