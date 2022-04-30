def task2_letter(string):
    for letter in string:
        if string.upper().find(letter.upper()) == string.upper().rfind(letter.upper()):
            return letter