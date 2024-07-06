
#count words in book
def word_counter(file_contents):
    words = file_contents.split()
    count = len(words)
    return count



#count letters in book
def char_counter(file_contents):
    chars = {}
    lowered_string = file_contents.lower()

    for char in lowered_string:
        if char.isalpha():  
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    # Print each character and its count
    for char, count in chars.items():
        print(f"Character '{char}' found {count} times.")


def main(book_title):
    with open(f"books/{book_title}.txt") as f:
        file_contents = f.read()

    print(f"--- Begin report of books/{book_title}.txt ---")

    word_count = word_counter(file_contents)
    print(f"Total words in {book_title}: {word_count}")

    char_counter(file_contents)
    
    
    print(f"--- End report of books/{book_title}.txt ---")
  
    

if __name__ == "__main__":
     main("frankenstein")