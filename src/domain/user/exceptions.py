from domain.base.exception import BusinessException


class UserNotFoundException(BusinessException):
    code = 404
    error_code = "USER__NOT_FOUND"
    message = "Users not found"
