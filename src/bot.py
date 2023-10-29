import discord
import dotenv
import os
import requests
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from discord import default_permissions
from dotenv import load_dotenv
from translate import Translator

load_dotenv()

bot = discord.Bot()
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))


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

@bot.command(description="Sends bot Latency.")
async def ping(ctx):
    embed = discord.Embed(
            title = "Pong!",
            description = f"Latency is {bot.latency}.",
            color = discord.Colour.blurple()
            )
    await ctx.respond(embed=embed)

@bot.command(description="Prompts the user to display a message.")
async def echo(ctx, *, message):
    embed = discord.Embed(
            description=f"{message}"
            )
    await ctx.respond("Here's the message.", embed=embed)
        
@bot.command(description="Gives users information.")
async def userinfo(ctx, user:discord.User):
    user_id = user.id
    username = user.name
    discriminator = user.discriminator
    created_at = user.created_at.strftime('%B %d, %Y')
    joined_at = user.joined_at.strftime('%B %d, %Y')
    embed = discord.Embed(
            title=f"{username}",
            description=f"{user_id}",
            color = discord.Color.green()
            )
    embed.add_field(
            name="Account Created:",
            value=f"`{created_at}`",
            inline=True
            )
    embed.add_field(
            name="Date Joined:",
            value=f"`{joined_at}`",
            inline=True
            )
    await ctx.respond(embed=embed)

@bot.command(description="Allows the bot to join a channel.")
async def join(ctx):
    if not ctx.author.voice:
        embed = discord.Embed(
                title = "You must be in a voice channel.",
                color = discord.Colour.red()
                )
        await ctx.respond(embed=embed)
        return

    channel = ctx.author.voice.channel
    voice_channel = await channel.connect()
    embed = discord.Embed(
            title=f"Joined {channel.name}",
            color = discord.Colour.green()
            )
    await ctx.respond(embed=embed)

@bot.command(description="Allows the bot to leave a voice channel.")
async def leave(ctx):
    if ctx.voice_client:
        embed = discord.Embed(
                title="Left the voice channel",
                color = discord.Colour.green()
                )
        await ctx.voice_client.disconnect()
        await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(
                title="I'm not in a voice channel",
                color = discord.Colour.red()
                )
        await ctx.respond(embed=embed)

@bot.command(description="Allows users to set reminders.")
async def remindme(ctx, time: int, *, message: str):
    try:
        time = int(time)
    except ValueError:
        await ctx.respond("The time must be an integer.")
        return

    if message == "":
        await ctx.respond("The message cannot be blank.")
        return
    
    user = discord.utils.get(ctx.guild.members, mention=ctx.author.mention)
    embed = discord.Embed(
            title=f"I will remind you in {time} seconds.",
            color=discord.Color.purple(),
            )
    await ctx.respond(embed=embed)
    await asyncio.sleep(time)
    embed = discord.Embed(
            title=f"@{user.name}, you wanted me to remind you:",
            description=f"{message}",
            color=discord.Color.purple(),
            )
    await ctx.respond(embed=embed)

@bot.command(description="Translates a message to a different language.")
async def translate(ctx, language, *, text):
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    text = translation
    embed = discord.Embed(
            title = "Translated to:",
            description = f"{text}",
            )
    await ctx.send(embed=embed)

bot.run(token)
