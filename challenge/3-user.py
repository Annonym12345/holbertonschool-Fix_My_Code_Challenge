#!/usr/bin/python3

class User:
    def __init__(self):
        self.__password = None

    def set_password(self, pwd):
        if isinstance(pwd, str):
            self.__password = pwd

    def is_valid_password(self, pwd):
        if self.__password is None:
            return False
        return pwd == self.__password


if __name__ == "__main__":
    user = User()
    user.set_password("Test User")

    print("Test User")
    print("is_valid_password should return True if it's the right password")
