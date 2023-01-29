import discord
import dotenv
import os
from discord.ext import commands
from discord.ext.commands import bot
from discord import default_permissions

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
    
@bot.command(name="whoami", description="Displays your username, creation date, status, and roles.")
async def whoami(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        title=f"{member}",
        description=f"Creation Date: {member.created_at}",
        color=discord.Color.blurple()
    )
    embed.add_field(name="Status", value=member.status)
    embed.add_field(name="Roles", value=", ".join([role.name for role in member.roles]))
    await ctx.send(embed=embed)

bot.run(token)
