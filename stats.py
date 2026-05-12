def get_num_words(text_from_book):
    text_to_words = text_from_book.split()
    num_words = len(text_to_words)
    return num_words


def get_num_characters(text_from_book):
    lower_case = text_from_book.lower()
    num_char = {}
    for text in lower_case:
        if text.isalpha():
            if text in num_char:
                num_char[text] = num_char[text] + 1
            else:
                num_char[text] = 1
    return num_char


def sort_list_dictionary(dictionary):
    new_list = []
    for key in dictionary:
        new_list.append({"char": key, "num": dictionary[key]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


def sort_on(items):
    return items["num"]
