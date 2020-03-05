# page 83 in Python Magazine

import time
import hashlib
from getpass import getpass


LOGINS_FILENAME = "logins.txt"


class UserStore:
    """A simple user database.

    >>> import os
    >>> os.unlink('test.txt')
    >>> u = UserStore('test.txt')
    >>> u.check_exists('foo')
    False
    >>> u.add_user('foo', 'bar')
    >>> u.check_exists('foo')
    True
    """

    def __init__(self, filename):
        self._filename = filename
        self._users = self._loadFromFile()

    def _loadFromFile(self):
        users = {}
        try:
            with open(self._filename, "r") as f:
                for line in f:
                    parts = line.split()
                    if len(parts) == 2:
                        username, password = parts
                        users[username] = password
        except FileNotFoundError:
            pass
        return users

    def add_user(self, username, password):
        hashed = hashPasswd(password)
        self._users[username] = hashed
        with open(self._filename, "a") as f:
            f.write(username + " " + hashed + "\n")

    def check_exists(self, username):
        return username in self._users

    def check_password(self, username, password):
        return self._users.get(username) == hashPasswd(password)


def mainMenu():
    users = UserStore(LOGINS_FILENAME)

    while True:
        status = input("Do you have a login account? y/n Or press q to quit.")
        if status == "y":
            oldUser(users)
        elif status == "n":
            newUser(users)
        elif status == "q":
            quit()


def newUser(users):
    createLogin = input("Create a login name: ")

    if users.check_exists(createLogin):
        print("\nSorry, that login name already exists. Please try a different one.\n")
    else:
        createPassw = getpass("Create password: ")
        users.add_user(createLogin, createPassw)
        print("User created!")


def oldUser(users):
    login = input("Enter the login name: ")
    passw = getpass("Enter password: ")

    # Check if user exists and login matches password
    if users.check_password(login, passw):
        print("\nLogin successful!\n")
        print("User: ", login, "accessed the system on: ", time.asctime())
    else:
        print("\nUser doesn't exist or wrong password!\n")


def hashPasswd(plain):
    """Return the SHA256 hex digest of a string.

    >>> hashPasswd('hello') 
    '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
    """
    return hashlib.sha256(plain.encode()).hexdigest()


if __name__ == "__main__":
    mainMenu()
