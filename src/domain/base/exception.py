from fastapi import HTTPException


class BusinessException(HTTPException):
    def __init__(self, code=None, error_code=None, message=None):
        self.code = code or self.__class__.code
        self.error_code = error_code or self.__class__.error_code
        self.message = message or self.__class__.message

        super().__init__(
            status_code=self.code,
            detail=self.message or self.error_code,
        )

    code = 400  # Статус-код по умолчанию
    error_code = "BAD_GATEWAY"  # Код ошибки по умолчанию
    message = None  # Сообщение об ошибке по умолчанию
