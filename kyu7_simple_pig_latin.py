# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.


text = "hello world, how are you?"


def pig_it(text):
    pig_it_list = []
    text_split = text.split(" ")

    for word in text_split:
        # if word is not punctuation
        if word.isalpha():
            # save letters after index 0 + index 0 + "ay" to new_word
            new_word = word[1:] + word[0] + "ay"
            pig_it_list.append(new_word)
        else:
            pig_it_list.append(word)

    pig_it_string = " ".join(pig_it_list)
    return pig_it_string


pig_it(text)

