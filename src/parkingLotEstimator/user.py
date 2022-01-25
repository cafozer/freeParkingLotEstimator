from typing import Any

from flask import current_app
from flask_login import UserMixin


class User(UserMixin):
    def __init__(
        self,
        username: str,
        password: str,
        phone_number: str,
        mail_address: str,
        num_of_cars: int,
    ) -> None:
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.mail_address = mail_address
        self.num_of_cars = num_of_cars
        self.active = True
        self.is_admin = False


def get(user_id: int) -> Any:
    db = current_app.config["db"]
    return db.get_user(user_id)
