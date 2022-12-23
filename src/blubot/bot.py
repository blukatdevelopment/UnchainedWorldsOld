import sys
import discord
from discord.ext import commands
sys.path.append('./commands/')
from database import Db

from pet import pet_command
from abilities import abilities_commands
from character import character_commands
from check import check_command
from save import save_command
from attack import attack_commands


bot = discord.Bot()
bot.db = Db()

pet_command(bot, discord)
abilities_commands(bot, discord)
character_commands(bot, discord)
check_command(bot, discord)
save_command(bot, discord)
attack_commands(bot, discord)

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True


@bot.event
async def on_ready():
    print(f'I have logged in as {bot.user}. Meow! :3')

# Read token from a file that's not in version control XD
token = open('./token', 'r').read()

bot.run(token)