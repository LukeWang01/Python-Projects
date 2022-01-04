import datetime as dt
import pandas as pd
import random

# today = dt.datetime.now()
# month = today.month
# day = today.day

today_month, today_day = dt.datetime.now().month, dt.datetime.now().day
# print(today_month, today_day)
data = pd.read_csv("birthdays.csv")
birthday_list = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}
if (today_month, today_day) in birthday_list:
    file_path = f"letter_{random.randint(1,3)}"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_con = contents.replace("[NAME]", birthday_list.name) # replace should be assigned


# new_dict = {new_keyL new_value for (key, value) in dict.items()}
