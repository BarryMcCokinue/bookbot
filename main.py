

def main():
    book_path = "books/frankenstein.txt"
    text = print_text(book_path)
    print(text)


def print_text(path):
    with open(path) as f:
        return f.read()
main()
