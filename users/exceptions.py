class UserException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class RegistrationException(UserException):
    pass
