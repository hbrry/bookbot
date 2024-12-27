def main():
    with open("/home/barry/workspace/github.com/hbbry/bookbot/books/frankenstein.txt") as f:
        text = f.read()
    
    print(f"--- Begin report of {"/home/barry/workspace/github.com/hbbry/bookbot/books/frankenstein.txt"} ---")
    print(f"{get_num_words(text)} words found in the document")
    print()

    for item in char_to_list(count_characters(text)):
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def sort_on(d):
    return d["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def char_to_list(dict):
    sorted = []
    for char in dict:
        sorted.append({"char": char, "num":dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

if __name__ == "__main__":
    main()