import re


class User:

    def __init__(self, userInputValidator):
        self.userInputValidator = userInputValidator
        self.__firstName = None

    def setFirstName(self):
        self.__firstName = self.userInputValidator.inputValidator("First Name")

    def getFirstName(self):
        return self.__firstName


class UserInputValidation:
    __NAME_PATTERN = "^[A-Z][a-zA-Z]{2,}"

    def getPattern(self, inputTitle):
        if inputTitle == inputTitle:
            return self.__NAME_PATTERN
        return None

    def inputValidator(self, inputTitle):
        pattern = self.getPattern(inputTitle)
        while True:
            userInput = input("Please Enter " + inputTitle + ": ")
            if re.fullmatch(pattern, userInput):
                return userInput
            print("Opps! " + inputTitle + "must start with capital letter and contains min 3 chars and no space")


if __name__ == "__main__":
    print("Welcome to User Registration Problem")

    userInputValidate = UserInputValidation()
    user = User(userInputValidate)
    user.setFirstName()
    print("First Name: " + user.getFirstName())

