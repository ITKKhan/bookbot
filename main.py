def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

file_info = main()

def count_words(file_info):
    num_words = len(file_info.split())    
    return num_words  

count = count_words(file_info)
print(count)
