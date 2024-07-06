def read(file_contents):
    words = file_contents.split()
    count = len(words)
    return count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = read(file_contents)
    print (word_count)
    

if __name__ == "__main__":
     main()