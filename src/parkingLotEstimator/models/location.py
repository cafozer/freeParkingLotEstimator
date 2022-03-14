class Location:
    __slots__ = ["id", "latitude", "longitude"]

    def __init__(self, id: int, latitude: str, longitude: str) -> None:
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
