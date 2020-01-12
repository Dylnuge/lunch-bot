import os
from os import path
import sys
from typing import List
import zulip

from lib import lunch_bot
from lib import state_handler


ZULIPRC_FILE_NAME = ".zuliprc"


def main(args: List[str]):
    client = zulip.Client(
        config_file=path.join(path.abspath(os.getcwd()), ZULIPRC_FILE_NAME)
    )

    try:
        with state_handler.StateHandler() as storage:
            bot = lunch_bot.LunchBotHandler(client, storage)
            client.call_on_each_message(bot.handle_message)
    except KeyboardInterrupt:
        pass
    print()


if __name__ == "__main__":
    main(sys.argv)
