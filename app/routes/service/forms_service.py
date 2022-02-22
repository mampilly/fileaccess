import csv

from h11 import Data


def read_csv(first_name, second_name):
    data_exist = False
    with open("app/data/username.csv") as f:
        for l, i in enumerate(f):
            data = i.replace("\n", "").split(";")
            if data[0].lower() == first_name.lower() and data[1].lower() == second_name.lower():
                data_exist = True
    return data_exist
