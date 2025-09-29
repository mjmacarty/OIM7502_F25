import hashlib


class User:

    def __init__(self, username=None, password=None,
                 email=None, birthday=None):
        self.username = username
        self.password = self._encrypt_password(password)
        self.email = email
        self.birthday = birthday


    def __str__(self):
        return f"Usename: {self.username}\nPassword: {self.password}\nemail: {self.email}\nbirthday: {self.birthday}"


    def __repr__(self):
        return f"{self.__class__}({self.__dict__})"


    def __eq__(self, other):
        return self.username == other.username


    def _encrypt_password(self, password):
        password = password.encode('utf-8')
        return hashlib.sha256(password).hexdigest()


    def check_password(self, password):
        password = self._encrypt_password(password)
        return password == self.password


if __name__ == "__main__":
    user = User("Maria", "password",
                "maria@somew.com", "3/17/2000")
    other = User("Maria", "password",
                 "sasi@some.com", "5/15/2000" )
    print(user)
    print(repr(user))
    print(user == other)
    print(user.check_password("Password"))