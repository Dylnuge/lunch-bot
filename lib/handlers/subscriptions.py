from datetime import timedelta

from lib import common
from lib import events
from lib.handlers import HandlerParams
from lib.models.plan import Plan
from lib.models.user import User
from lib.models.subscription import Subscription

# TODO something needs to register subscription messages to fire daily and
# something needs to actually handle sending the messages


def handle_subscribe(params: HandlerParams):
    """Sign a user up for daily lunch reminders"""
    user = User.get_sender(params.message)
    sub = Subscription(user_email=user.email)
    # TODO Get user subscription if it already exists. If it _does_ exist, tell
    # the user they're already subscribed to messages. Otherwise, add it.


def handle_unsubscribe(params: HandlerParams):
    """Remove a user from daily lunch reminders"""
    user = User.get_sender(params.message)
    # TODO Get user subscription and delete it. If none is found, tell the user
    # they're not subscribed to reminder messages
