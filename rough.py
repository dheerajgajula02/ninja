# import pandas as pd

# data = pd.read_csv("output.csv")

# user_details = {
#     "name":"dheeraj",
#     "email":"dheerajgajula2202@gmail.com",
#     "phone_number":"6281405953",
#     "location":"bangalore"
# }

# df = pd.DataFrame([user_details])

# # print(df)

# new_df = pd.concat([data, df], ignore_index=True)

# print(new_df)

# new_df.to_csv("output.csv", index=False)

# import json

# to_change = '''
# {
# "stage": "yes",
# "name": "dheeraj",
# "message":"may I know your email address"
# }
# '''

# my_dict = {}

# print(json.loads(to_change))

# json_val = json.loads(to_change)
# list_ =  list(json_val.keys())
# print(list_)

# if json_val['stage']=="yes":
#     key = list(json_val.keys())[1]
#     my_dict[key]= json_val[key]

# print(my_dict)




import re


def search(the_prompt:str):
    # List of words to search for
    words_to_search = ["name", "email", "address", "location"]

    # The big string
    big_string = the_prompt

    # Create a regular expression pattern to match any of the words
    pattern = '|'.join(words_to_search)

    # Use regex to find the first match
    match = re.search(pattern, big_string, re.IGNORECASE)

    # If a match is found, return the matched word
    if match:
        matched_word = match.group(0)
        return matched_word
    else:
        return "no"
    


print(search("this is an outupt"))
