def main():
    with open("/home/barry/workspace/github.com/hbbry/bookbot/books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
    return print(count_characters(text))

def count_characters(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

if __name__ == "__main__":
    main()