# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
import pandas as pd
# from prometheus_client import values

dict_letter = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (idx, row) in dict_letter.iterrows()}
# print(nato_dict)
#
# print(dict_letter.index)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("input the word:\n").upper()
input_letter = [item for item in input_word]
phonetic = {keys: values for (keys, values) in nato_dict.items() if keys in input_letter}
print(phonetic)
phonetic_list = [nato_dict[item] for item in input_letter]
print(phonetic_list)

