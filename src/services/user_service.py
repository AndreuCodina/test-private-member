class UserService:
    def sign_up(self, email: str) -> None:
        if not self._is_valid_email(email):
            error_message = "Invalid email"
            raise ValueError(error_message)

        if self._exists(email):
            error_message = "User already exists"
            raise ValueError(error_message)

        if not self._associate_bank_account():
            error_message = "Not allowed to create account"
            raise ValueError(error_message)

    def _is_valid_email(self, email: str) -> bool:
        return "@" in email and "." in email

    def _exists(self, email: str) -> bool:
        return email == "foo@gmail.com"

    def _associate_bank_account(self) -> None:
        pass
