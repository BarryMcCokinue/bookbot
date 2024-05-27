def main():

    #List of variables and method calls to make the variables

    book_path = "books/frankenstein.txt" 
    text = get_text(book_path)
    count = word_counter(text)
    characters = letter_counter(text)
    make_report(text)

## function to create the 'text' variable. Opens the file at 'path' then reads and stores the text
def get_text(path):
    with open(path) as f:
        return f.read()

## function to create a word count variable
def word_counter(text):
    word_count = 0
    words = text.split()
    
    for word in words:
            word_count += 1

    return word_count

## function to count all the characters and convert them to lowercase
def letter_counter(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

## provides a list of each of the alphabetical characters in the text and orders them by frequency
def make_report(text):
    
    char_count_dict = letter_counter(text)
    char_count_list = convert(char_count_dict)
    count = word_counter(text)

    char_count_list.sort(reverse=True, key=sort_on)
        
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in this document")
    print("")
    for num in char_count_list:
        list_item = num
        for value in list_item:
            if value.isalpha() == True:
                print(f"The '{value}' character was found {list_item[value]} times")

    print("--- End report ---")

## takes a dictionary an converts it to a list of dictionaries
def convert(dictionary):
    return [{key: value} for key, value in dictionary.items()]

def sort_on(dictionary):
    for num in dictionary:
        return dictionary[num]






main()
