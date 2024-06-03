from domain.base.exception import CustomException


class UserNotFoundException(CustomException):
    code = 404
    error_code = "USER__NOT_FOUND"
    message = "Users not found"
