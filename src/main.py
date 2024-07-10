import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot(intents=discord.Intents.all()) 
token = os.getenv("TOKEN")
cogs_list = [
    'join',
    'leave',
    'ping',
    'remindme',
    'say',
    'translate',
    'userinfo',
    'dictionary'
]

@bot.event
async def on_ready():
    server_count = len(bot.guilds)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{server_count} servers suffer.",
        )
    )
    print(f"Logged in as {bot.user}")
    print("Bot Online!")

# Load each cog from the cogs directory
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(token)
