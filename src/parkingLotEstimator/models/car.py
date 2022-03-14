class Car:
    __slots__ = ["id", "user_id", "height", "fuel_type"]

    def __init__(self, id: int, user_id: int, height: int, fuel_type: str) -> None:
        self.id = id
        self.user_id = user_id
        self.height = height
        self.fuel_type = fuel_type
