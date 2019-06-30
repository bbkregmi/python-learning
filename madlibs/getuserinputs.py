
def askForText(parts_of_speech):
    return_list = []
    for text in parts_of_speech:
        userInput = input("Please enter a %s " % text)
        while (len(userInput) == 0):
            userInput = input("Please enter a %s " % text)
        return_list.append(userInput)

    return return_list

