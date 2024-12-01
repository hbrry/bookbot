def main():
    with open("/home/barry/workspace/github.com/hbbry/bookbot/books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
    return print(len(words))

def count_characters(text):
    lowered_text = text.lower()


if __name__ == "__main__":
    main()