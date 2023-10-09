import discord
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()
token = str(os.getenv("TOKEN"))

@bot.event
async def on_ready():
       print(f"Logged in as {bot.user} ID: {bot.user.id}")
       print("Bot Online!")

@bot.commands()
async def test(ctx):
       await ctx.respond(f"Hello! {client.user}")

@bot.commands()
async def embed():
       embed = discord.Embed(title="Client is ready")
       await ctx.send(embed=embed)

bot.run(token)
