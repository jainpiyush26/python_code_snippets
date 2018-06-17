# Value Error Classes
class BaseValueError(ValueError):
    pass


class NotIntError(BaseValueError):
    pass


class NotStrError(BaseValueError):
    pass


class UnknownError(BaseValueError):
    pass


class StringTooLongError(BaseValueError):
    pass