v = ('a', 'e', 'i', 'o', 'u')


def convert_word(word):
    first_letter = word[0]
    if first_letter in v:  # начало с гласной
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"


def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word)
        new_sentence += " "
    return new_sentence


print "Type a sentence"

text = raw_input()
print convert_sentence(text)