import requests


def reach_url():
    url = "https://" + input("Please enter a website to reach ")

    try:
        response = requests.get(url)
        print(response.status_code)

    except BaseException as e:
        print("Something went wrong\n", e.args)


def attempt_division():
    while True:
        try:
            a = int(input("Enter 1st number\t"))
            b = int(input("Enter 2nd number\t"))
            print(a/b)
            break
        except ValueError:
            print("enter a correct number value")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except BaseException as e:
            print("General issue")
            print(e.args)


def get_user_age():
    try:
        user_age = int(input("Please enter age"))
    except BaseException:
        print("General error in input")
    if user_age < 0:
        raise ValueError("age cannot be a negative number")


def get_user_age_class_exception():
    class NegativeAgeError(Exception):
        """Exception raised for negative user age."""
        def _init_(self, age, message="Age cannot be negative"):
            self.age = age
            self.message = message
            super()._init_(self.message)

        def _str_(self):
            return f"{self.message}: {self.age}"

    def get_user_age_with_exception():
        try:
            user_age = int(input("enter age "))
        except BaseException:
            print("General issue")
        if user_age < 0:
            raise NegativeAgeError("")

    try:
        get_user_age_with_exception()
    except NegativeAgeError as e:
        print("age can't be negative")
        print(e)


# reach_url()
# attempt_division()
# get_user_age()
get_user_age_class_exception()
