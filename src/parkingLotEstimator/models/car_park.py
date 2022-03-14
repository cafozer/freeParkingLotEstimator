from typing import Optional


class CarPark:
    __slots__ = ["id", "capacity", "n_of_current_cars", "rating", "location_id"]

    def __init__(
        self,
        id: int,
        capacity: int,
        n_of_current_cars: int,
        rating: Optional[float],
        location_id: int,
    ) -> None:
        self.id = id
        self.capacity = capacity
        self.n_of_current_cars = n_of_current_cars
        self.rating = rating
        self.location_id = location_id
