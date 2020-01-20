from typing import List

from lib.models.user import User


class Plan:
    def __init__(self, restaurant: str, time: str, rsvps: List[User]):
        self.restaurant = restaurant
        self.time = time
        self.rsvps = rsvps

    def __eq__(self, other: object):
        if not isinstance(other, Plan):
            return False
        return (
            self.restaurant == other.restaurant
            and self.time == other.time
            and self.rsvps == other.rsvps
        )
