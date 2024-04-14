import pandas
#TODO 1. Create a dictionary in this format:
data_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = pandas.DataFrame(data_alphabet)
# print(alphabet)

alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

string_to_transform = input("Give me a word to translate: ").upper()
letter_list = [letter for letter in string_to_transform]

code_list =[alphabet_dict[letter] for letter in string_to_transform]
print(code_list)
