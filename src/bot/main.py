import asyncio

from bot.app import dp, bot
from bot.dispatcher.setup import start_bot

if __name__ == '__main__':
    asyncio.run(start_bot(dp, bot))
