def get_chars_dict(file):
    char_list = list(file.lower())
    result_dict = {}
    for char in char_list:
        if char.isalpha():
            if char in result_dict:
                result_dict[char] += 1
            else:
                result_dict[char] = 1
        
    return result_dict

def generate_report(book, wordcount, charsdict):
    print(f"--- Begin report of {book} ---")
    print(f"{wordcount} words found in the document")
    print()
    report_list = []
    for char in charsdict:
        report_list.append({"name":char,"num":charsdict[char]})
    report_list.sort(reverse=True, key=sort_on)
    for report_item in report_list:
        print(f"The '{report_item["name"]}' character was found {report_item["num"]} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    generate_report(book_path,num_words,chars_dict)

main()