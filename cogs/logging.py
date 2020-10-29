import discord
import logging
import datetime
import requests
import time
from discord.ext import commands

r = requests.get("https://repl.it/@BArewrite/botpy#logs/spring.log")

class Logging(commands.Cog):
  def __init__(self, client):
    self.client = client
    #self.logger.start()

    #def cog_unload(self):
        #self.logger.cancel()

    async def logger(self):
        logging.basicConfig(filename="log.txt", filemode="a", format="%(asctime)s %(msecs)d- %(process)d -%(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S %p", level=logging.INFO)

        channel = client.get_channel(768261473415594004)
        tn = datetime.datetime.utcnow()
        await channel.send(f'{tn.strftime("%c")} log, timezone: UTC', file=discord.File('log.txt'))
        await channel.send(file=discord.File("spring.log"))
        time.sleep(10)
        with open("log.txt", "r+") as f:
            f.truncate()
        with open("./logs/spring.log", "r") as r:
            r.truncate()
        #await self.client.loop_task(logger())
              
def setup(client):
    client.add_cog(Logging(client))
    return