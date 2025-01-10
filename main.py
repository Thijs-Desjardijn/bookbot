def main():
    print("--- Word Count Report ---")
    print("Total words:", word_counting())
    print("\n--- Letter Count Report ---")
    letter_dict = letter_count()
    
    # Find the maximum count to help with scaling
    max_count = max(letter_dict.values())
    
    # Now for each letter, let's create a scaled bar
    for letter, count in sorted(letter_dict.items()):
        # Let's scale it to maximum 50 asterisks
        scaled_count = int((count / max_count) * 50)
        print(f"{letter}: {count:6d} {'*' * scaled_count}")

def word_counting():
    with open("books/frankenstein.txt") as f:
        word_count = 0
        file_contents = f.read()
        words_total = file_contents.split()
        for word in words_total:
            word_count += 1
    return word_count


def letter_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letters = "abcdefghijklmnopqrstuvwxyz"
        letters_dictionary = {letter: 0 for letter in letters}
        for char in file_contents.lower():
            if char in letters :
                letters_dictionary[char] += 1
            else: pass
    return letters_dictionary
main()
