import re


class User:

    def __init__(self, userInputValidator):
        self.userInputValidator = userInputValidator
        self.__firstName = None
        self.__lastName = None
        self.__email = None

    def setFirstName(self):
        self.__firstName = self.userInputValidator.inputValidator("First Name")

    def getFirstName(self):
        return self.__firstName

    def setLastName(self):
        self.__lastName = self.userInputValidator.inputValidator("Last Name")

    def getLastName(self):
        return self.__lastName

    def setEmail(self):
        self.__email = self.userInputValidator.inputValidator("Email")

    def getEmail(self):
        return self.__email


class UserInputValidation:

    __NAME_PATTERN = "^[A-Z][a-zA-Z]{2,}"
    __EMAIL_PATTERN = "^[a-zA-Z]{1}[a-zA-Z0-9]+([-\\.\\_\\+]?[0-9a-zA-Z]+)*\\@[a-zA-Z]+([\\.][a-z]{2,4})?([\\.][a-z]{2,4})$"

    def getPattern(self, inputTitle):
        """This function returns Pattern based on the inputTitle
        :param inputTitle:
        :return: Patern"""
        if inputTitle == "First Name" or inputTitle == "Last Name":
            return self.__NAME_PATTERN
        elif inputTitle == "Email":
            return self.__EMAIL_PATTERN
        return None

    def inputValidator(self, inputTitle):
        """This function takes inputTitle as parameter from the User class functions
        and taking userInput based on this and validates and returns the userInput once validated"""

        pattern = self.getPattern(inputTitle)
        while True:
            userInput = input("Please Enter " + inputTitle + ": ")
            if re.fullmatch(pattern, userInput):
                return userInput
            elif inputTitle == "Email":
                print(f"Opps! Invalid {inputTitle}! Please try with different One")
            else:
                print(f"Opps! {inputTitle} must start with capital letter and contains min 3 chars and no space")


if __name__ == "__main__":
    print("Welcome to User Registration Problem")

    userInputValidate = UserInputValidation()
    user = User(userInputValidate)
    user.setFirstName()
    print("First Name: " + user.getFirstName())
    user.setLastName()
    print("Last Name: " + user.getLastName())
    user.setEmail()
    print("Email: " + user.getEmail())

