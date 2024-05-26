def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count = word_counter(book_path)
    print(count)

def get_text(path):
    with open(path) as f:
        return f.read()

def word_counter(path):
    word_count = 0
    words = get_text(path).split()
    
    for word in words:
            word_count += 1

    return word_count
main()
