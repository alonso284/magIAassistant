#Welcome, to the TI club discord bot code.

#introduction

""" mac
python3 -m pip install -U discord.py
windows
py -3 -m pip install -U discord.py """

#Import discord library and logging library
import discord, logging
#import intents
from discord.ext import commands
#Import JSON
import json

#Set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#setup intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# client = discord.Client()
bot = commands.Bot(command_prefix = '?')

#fix boot
""" #boot up
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot)) """

""" 
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('hello'):
#         await message.channel.send('Hello!') """

with open('./magIAObject.json') as myObject:
    magIA = json.load(myObject)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def getCode(ctx, modulo, dia):
    await ctx.send('El código es {}'.format(magIA[modulo][dia]))

@bot.command()
async def setCode(ctx, modulo, dia, codigo):
    magIA[modulo][dia] = codigo
    with open('./magIAObject.json', 'w') as myObject:
        json.dump(magIA, myObject)



bot.run('')