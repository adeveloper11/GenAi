def capitalize_words(text):
    word_list = text.split(" ")
    words = ""
    for word in word_list:
        words += word.capitalize() + " "
    return words
    
def reverse_string(text):
    word_list = text.split(" ")
    reversed_words = ""
    for word in word_list[::-1]:
        reversed_words += word + " "
    return reversed_words

def word_count(text):
    word_list = text.split(" ")
    count = 0
    for word in word_list:
        count += 1
    return count

