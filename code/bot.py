import discord
import dotenv
import os
from discord.ext import commands
from discord.ext.commands import bot
from discord import default_permissions
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ID: {bot.user.id}")
    print("Bot Online!")
    
@bot.command(description="Sends bot Latency.")
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description=f"Latency is {bot.latency}.",
        color=discord.Colour.blurple()
    )
    await ctx.respond(embed=embed)
    
bot.run(token)