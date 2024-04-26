import pandas
data_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = pandas.DataFrame(data_alphabet)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

end = False
while end is False:
    string_to_transform = input("Give me a word to translate: ").upper()

    try:
        letter_list = [letter for letter in string_to_transform]
        code_list = [alphabet_dict[letter] for letter in string_to_transform]

    except KeyError:
        print("Please enter only letters - not numbers")
    else:
        print(code_list)
        end = True
