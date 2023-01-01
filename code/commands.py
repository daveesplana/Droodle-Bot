import discord
import os
import random
from googletrans import Translator
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext

bot = Client(intents=Intents.default())
slash = SlashCommand(bot)

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="you"))
    print(f'Logging in as {bot.id}')
    print('Online!')

@slash.slash(name="echo", description="use this command for fun")    
async def echo(ctx, *, content:str):
    embed = discord.Embed(title=f"{ctx.author.name} says",description=(content), color=0x42F56C)
    await ctx.send(embed=embed)

@slash.slash(name="ping", description="Bot Latency")
async def ping(ctx):
   embed = discord.Embed(title="Pong!", description="Latency: {0}".format(bot.latency), color=0x08bee2)
   await ctx.send(embed=embed)

@slash.slash(name="whoami", description="Displays your username")
async def whoami(ctx):
    embed=discord.Embed(title=f'{ctx.author.name}', 
    description=f'ID: {ctx.guild.id}', 
    color=0x83e50b)
    await ctx.send(embed=embed)

@slash.slash(name="translate", description="Translates a message")
async def translate(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    embed=discord.Embed(title="Translated to", description=(translation.text), color=0x8005fa)
    await ctx.send(embed=embed)
    
bot.run(token)
