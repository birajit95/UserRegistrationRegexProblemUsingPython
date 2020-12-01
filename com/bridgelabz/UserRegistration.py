import re


class User:

    def __init__(self, userInputValidator):
        self.userInputValidator = userInputValidator
        self.__firstName = None
        self.__lastName = None
        self.__email = None
        self.__mobileNumber = None
        self.__password = None

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

    def setMobileNumber(self):
        self.__mobileNumber = self.userInputValidator.inputValidator("Mobile Number")

    def getMobileNumber(self):
        return self.__mobileNumber

    def setPassword(self):
        self.__password = self.userInputValidator.inputValidator("Password")

    def getPassword(self):
        return self.__password


class UserInputValidation:
    __NAME_PATTERN = "^[A-Z][a-zA-Z]{2,}"
    __EMAIL_PATTERN = "^[a-zA-Z]{1}[a-zA-Z0-9]+([-\\.\\_\\+]?[0-9a-zA-Z]+)*\\@[a-zA-Z]+([\\.][a-z]{2,4})?([\\.][a-z]{2,4})$"
    __MOBILE_NUMBER_PATTERN = "^(\\+91|91)[ ]{1}[6-9]{1}[0-9]{9}$"
    __PASSWORD_PATTERN = "(?=.*[A-Z])(?=.*[0-9])([a-zA-Z0-9]|[^a-zA-Z0-9]){8,}"

    def getPattern(self, inputTitle):
        """This function returns Pattern based on the inputTitle
        :param inputTitle:
        :return: Patern"""
        if inputTitle == "First Name" or inputTitle == "Last Name":
            return self.__NAME_PATTERN
        elif inputTitle == "Email":
            return self.__EMAIL_PATTERN
        elif inputTitle == "Mobile Number":
            return self.__MOBILE_NUMBER_PATTERN
        elif inputTitle == "Password":
            return self.__PASSWORD_PATTERN
        return None

    def inputValidator(self, inputTitle):
        """This function takes inputTitle as parameter from the User class functions
        and taking userInput based on this and validates and returns the userInput once validated"""

        pattern = self.getPattern(inputTitle)
        while True:
            userInput = input("Please Enter " + inputTitle + ": ")
            if re.fullmatch(pattern, userInput):
                return userInput
            elif inputTitle == "Email" or inputTitle == "Mobile Number":
                print(f"Opps! Invalid {inputTitle}! Please try with different One")
            elif inputTitle == "Password":
                print(f"Invalid {inputTitle} format, {inputTitle} must contains "
                      f"atleast one upper case, atleast one lower case, atleast one numeric, "
                      f"atleast one special char and minimum of 8 chars")
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
        user.setMobileNumber()
        print("Mobile: " + str(user.getMobileNumber()))
    user.setPassword()
    print("Password: " + user.getPassword())
