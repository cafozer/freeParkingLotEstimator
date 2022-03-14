class CarAndParkRelation:
    __slots__ = ["id", "car_id", "park_id"]

    def __init__(self, id: int, car_id: int, park_id: int) -> None:
        self.id = id
        self.car_id = car_id
        self.park_id = park_id
