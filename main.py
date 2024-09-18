def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    words = num_words(text)
    char_freq_dict = num_chars(text)
    sorted_chars = dict_to_sorted_list(char_freq_dict)
    
    print(f"--- Begin Report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    
    print("--- End Report ---")
    
def num_words(text): 
    words = text.split()
    return len(words)

def num_chars(text):
    freq = {}
    text = text.lower()
    
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
   
def sort_on(dictionary: dict):
    return dictionary["num"]

def dict_to_sorted_list(freq_dict: dict):
    sorted_list = []
    for c in freq_dict:
        sorted_list.append({"char": c, "num": freq_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
main()
