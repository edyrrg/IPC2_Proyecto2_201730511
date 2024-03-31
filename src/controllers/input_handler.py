class InputHandler:
    @staticmethod
    def handler_input_option(lower_limit, upper_limit):
        while True:
            try:
                user_response = int(input(">_: "))
                if lower_limit <= user_response <= upper_limit:
                    return user_response
                else:
                    print("Only numbers are accepted in the list of menu options")
            except ValueError:
                print("Enter only numbers")

    @staticmethod
    def handler_response_user(min_letters, text_err):
        while True:
            try:
                user_response = input(">_: ")
                if user_response is not None and len(user_response) >= min_letters:
                    return user_response
                else:
                    print(f"Warning: {text_err}")
            except ValueError as e:
                print(e)

    @staticmethod
    def handler_number_response_user():
        while True:
            try:
                user_response = int(input(">_: "))
                if user_response > 0:
                    return user_response
                else:
                    print("\t    Only numbers greater than zero")
            except ValueError:
                print("\t    Enter only numbers")

    @staticmethod
    def handler_price_value():
        while True:
            try:
                user_response = float(input(">_: "))
                if user_response > 0:
                    return user_response
                else:
                    print("\t    Only numbers greater than zero")
            except ValueError:
                print("\t    Enter only numbers")

    @staticmethod
    def handler_yorn_response_user():
        while True:
            user_response = input(">_: ")
            if user_response == "yes" or user_response == "y" or user_response == "Yes":
                return True
            elif user_response == "no" or user_response == "n" or user_response == "No":
                return False
            else:
                print('Please enter: y(Yes) or n(No)')

    @staticmethod
    def handler_continue_response_user():
        while True:
            user_response = input(">_: ")
            if (user_response == "continue" or user_response == "c" or user_response == "yes"
                    or user_response == "Yes" or user_response == "C" or user_response == "y"):
                return True
            elif user_response == "no" or user_response == "n" or user_response == "back":
                return False
            else:
                print('Please enter: c(Continue) or n(No)')
