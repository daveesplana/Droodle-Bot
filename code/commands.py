import discord
import dotenv
import os
from discord.ext import commands
from discord.ext.commands import bot
from discord import default_permissions

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
    
@bot.on_command("whoami")
async def whoami(message):
    member = message.author
    fields = [
        {"name": "Status", "value": member.status},
        {"name": "Roles", "User ID," "value": ", ".join([role.name for role in member.roles])}
        {"name": "User ID", "value": member.id}
    ]
    embed = {
        "title": f"{member}",
        "description": f"Creation Date: {member.created_at}",
        "color": 0x7289da,
        "fields": fields
    }
    await ctx.respond(embed=embed)

bot.run(token)
