from fastapi import HTTPException


class CustomException(HTTPException):
    def __init__(self, code=None, error_code=None, message=None):
        super().__init__(
            status_code=self.code,
            detail=self.message or self.__class__.message,
        )

    code = 400  # Статус-код по умолчанию
    error_code = "BAD_GATEWAY"  # Код ошибки по умолчанию
    message = "BAD_GATEWAY"  # Сообщение об ошибке по умолчанию
