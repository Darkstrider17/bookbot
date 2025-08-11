def get_num_words(text):
    return len(text.split())    #counts and returns the amount of words in text

def character_count(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] +=1
        else:
            char_count[lower_char] =1

    return char_count

def clean_list(char_count):
    filtered_list = []
    for char, amount in char_count.items():
        if char.isalpha():
            filtered_list.append({"char": char, "num": amount})
    filtered_list.sort(key=lambda item: item["num"], reverse=True)
    return filtered_list