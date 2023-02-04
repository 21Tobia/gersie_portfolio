import sys
import pickle   # to access the pickle
import os
import re


# Person class to describe a person object
class Person:
    # init method
    def __init__(employee, last, first, mi, id, phone):
        employee.last = last
        employee.first = first
        employee.mi = mi
        employee.id = id
        employee.phone = phone

    # display method
    def display(employee):
        print("Employee id:", employee.id)
        print("\t    ", employee.first, employee.mi, employee.last)
        print("\t    ", employee.phone)

# Function to read a file and return a text which is of type string
def readFile(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text = f.read()
    return text

# Function to process a text and returns a dictionary of person objects
def processText(text):
    dict = {}
    # read all sentence from the data
    sentences = text.split('\n')

    # iterate for each data without the first line
    for sentence in sentences[1:]:
        # take all parts of the person object
        tokens = sentence.split(',')

        # capitalize the first letter using upper last and first name.
        # and make other lower case
        upper_last_Name = tokens[0][0].upper() + tokens[0][1:].lower()
        upper_first_Name = tokens[1][0].upper() + tokens[1][1:].lower()

        # check the middle and if it is empty make it X else set it upper case
        mid = tokens[2].upper() if tokens[2] != '' else 'X'

        # get the person ID from the tokenizer
        person_Id = tokens[3]

        # check if the pattern of the ID which is 2 letters followed by 4 numbers
        pattern_Checker = re.search("[a-zA-Z]{2}[0-9]{4}", person_Id)

        # check if the pattern, if not prompt the user to enter until it is correct
        while not pattern_Checker:
            print("ID is invalid:", person_Id)
            print("ID is two letters followed by 4 digits")
            person_Id = input("Please input a valid id: ")
            pattern_Checker = re.search("[a-zA-Z]{2}[0-9]{4}", person_Id)

        # check if the number is of the format 123-456-7890
        num = tokens[4]
        numberPattern = re.search("([0-9]{3})-([0-9]{3})-([0-9]{4})", num)

        # check if the format is correct, if not prompt the user to enter until it is correct
        while not numberPattern:
            print(f"Phone {num} is invalid")
            print("Enter phone number in the form 123-456-7890")
            num = input("Enter phone number: ")
            numberPattern = re.search("([0-9]{3})-([0-9]{3})-([0-9]{4})", num)

        # create the person object by calling the person class
        person = Person(upper_last_Name, upper_first_Name, mid, person_Id, num)
        # check if the person_ID already exist in the dictionary
        if person_Id in dict:
            print(f"{person_Id} already exists!")
        else:
            dict[person_Id] = person
    return dict


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('The argument is not correct please enter the proper command')
    else:
        # take the second argument from the terminal
        fp = sys.argv[1]
        readText = readFile(fp)
        dict = processText(readText)

        pickle.dump(dict, open('dict.p', 'wb'))   # save to pickle file
        # read the pickle file
        dict_in = pickle.load(open('dict.p', 'rb'))  # read the pickle file
        print("Employee list:\n")
        # display the all outputs in the consolo
        for person in dict_in.values():
            person.display()
            print()