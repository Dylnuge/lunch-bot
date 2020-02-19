from lib.models.message import Message


class Subscription:
    def __init__(self, user_email: str = ""):
        self.user_email = user_email

    def __eq__(self, other: object) -> bool:
        """
        Check if two subscription objects are for the same user
        """
        if not isinstance(other, Subscription):
            return False
        return self.user_email == other.user_email
