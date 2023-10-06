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
    await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="to you"
                )
            )
    print(f"Logged in as {bot.user}")
    print("Bot Online")

    print(f"Logged in as {bot.user} ID: {bot.user.id}")
    
@bot.command(description="Sends bot Latency.")
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description=f"Latency is {bot.latency}.",
        color=discord.Colour.blurple()
    )
    await ctx.respond(embed=embed)

@bot.command(description="Prompts the user to display a message.")
async def echo(ctx, *, message):
    embed = discord.Embed(
            description=f"{message}"
            )
    await ctx.respond("Here's the message.", embed=embed)

@bot.command(description="Allows the bot to join a voice channel.")
async def join(ctx):
    if not ctx.author.voice:
        await ctx.respond("You must be in a voice channel.")
        return

    channel = ctx.author.voice.channel
    voice_channel = await channel.connect()
    embed = discord.Embed(
            title=f"Joined {channel.name}",
            color=discord.Color.blue()
            )
    await ctx.respond(embed=embed)

@bot.command(description="Allows the bot to leave a voice channel.")
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        embed = discord.Embed(title="Left the voice channel.", color=discord.Color.green())
        await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title="I'm not in a voice channel.", color=discord.Color.red())
        await ctx.respond(embed=embed)

bot.run(token)
