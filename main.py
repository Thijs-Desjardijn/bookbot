def main():
    with open("books/frankenstein.txt") as f:
        word_count = 0
        file_contents = f.read()
        words_total = file_contents.split()
        for word in words_total:
            word_count += 1
    print(word_count)
main()

