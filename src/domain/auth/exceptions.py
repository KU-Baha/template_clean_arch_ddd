from domain.base.exception import BusinessException


class DecodeTokenException(BusinessException):
    code = 400
    error_code = "TOKEN__DECODE_ERROR"
    message = "token decode error"


class ExpiredTokenException(BusinessException):
    code = 400
    error_code = "TOKEN__EXPIRE_TOKEN"
    message = "expired token"


class InvalidTokenException(BusinessException):
    code = 400
    error_code = "TOKEN__INVALID_TOKEN"
    message = "invalid token"
