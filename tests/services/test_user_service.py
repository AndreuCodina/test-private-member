from pytest_mock import MockerFixture

from src.services.user_service import UserService


class TestUserService:
    def test_associate_bank_account(self, mocker: MockerFixture) -> None:
        user_service = UserService()

        associate_bank_account_mock = mocker.patch(
            f"{UserService.__module__}.{UserService._associate_bank_account.__qualname__}",
        )

        user_service.sign_up("fran@gmail.com")

        associate_bank_account_mock.assert_called_once_with()
