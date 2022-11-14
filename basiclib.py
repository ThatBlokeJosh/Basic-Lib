# Random
import random
def rand(start, end):
    return random.randint(start, end)

# Fun functions
def hello():
    print("Hello, world!")


# Lists
def symbols():
    symbols = "!@#$%^&*()_+-=<>?/.,;:[]{}|"
    return symbols

def letters():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters

def numbers():
    numbers = "1234567890"
    return numbers

def cap_letters():
    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return cap_letters

lower_alfabet = letters()
uper_alfabet = cap_letters()

# Changing the message
def upper(message):
    new_message = ""
    for letter in message:
        if letter in lower_alfabet:
            index = lower_alfabet.index(letter)
            new_message += uper_alfabet[index]
        else:
            new_message += letter
    return new_message

def lower(message):
    new_message = ""
    for letter in message:
        if letter in uper_alfabet:
            index = uper_alfabet.index(letter)
            new_message += lower_alfabet[index]
        else:
            new_message += letter
    return new_message

def title(message):
    new_message = ""
    if message[0] in lower_alfabet:
        index = lower_alfabet.index(message[0])
        new_message += uper_alfabet[index]
        for letter in message[1:]:
            if letter in uper_alfabet:
                index = uper_alfabet.index(letter)
                new_message += lower_alfabet[index]
            else:
                new_message += letter
    else:
        new_message += message
    return new_message

# Indexing
def letter_id(message):
    new_message = ""
    for letter in message:
        if letter in lower_alfabet:
            new_message += str(f"{lower_alfabet.index(letter)} ")
        elif letter in uper_alfabet:
            new_message += str(f"{uper_alfabet.index(letter)} ")
        else:
            new_message += letter    
    return new_message

def index(list, message):
    num = -1
    for item in list:
        if item == message:
            num += 1
            return num
        else:
            num += 1

# Formating
def format(list):
    formated = []

    for i in list:
        formated.append(f"{i}, ")

    formated[-1] = formated[-1].replace(", ", "")

    for i in formated:
        print(i, end="")

def format_list(list):
    new_list = []
    for i in list:
        new_list.append(f"{i}")

    for i in range(len(new_list)):
        new_list[i] = f"{new_list[i]} "

    new_list[-1] = new_list[-1].replace(" ", ".")
    
    message = ""
    for i in new_list:
        message += i
    return message

