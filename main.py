def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_char(text)
    print(print_report(book_path,num_words,char_count))

    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_char(string):
    chars = {}
    char_list = []
    string = string.lower()
    for char in string:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    sorted_keys = sorted(chars.keys())
    char_list = sorted(chars.items(), key=lambda x: x[1], reverse=True)

    return char_list

def print_report(book, number, list):
    print("--- Begin report of ", book, " ---")
    print(f"{number} words found in the document")
    for char, count in list:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()