class BaseService:
    def __init__(
            self,
            gettext: callable,
            logger: callable
    ) -> None:
        self._gettext = gettext
        self._logger = logger
        self._errors = {}

    def handle_errors(self):
        if not self._errors:
            return

        errors = self._errors
        self._errors = {}
        raise ValueError(errors)
