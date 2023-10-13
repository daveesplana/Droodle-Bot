import discord
import dotenv
import os
import requests
from discord.ext import commands
from discord.ext.commands import bot
from discord import default_permissions
from dotenv import load_dotenv

load_dotenv()

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))


class MyBot(discord.Bot):
    async def on_ready(self):
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
                    await ctx.respond("You must be in a voice channel.")
                    return
                channel = ctx.author.voice.channel
                voice_channel = await channel.connect()
                embed = discord.Embed(
                        title=f"Joined {channel.name}"
                        )
                await ctx.respond(embed=embed)

                @bot.command(description="Allows the bot to leave a voice channel.")
                async def leave(ctx):
                    if ctx.voice_client:
                        embed = discord.Embed(
                                title="Left the voice channel"
                                )
                        await ctx.voice_client.disconnect()
                        await ctx.respond(embed=embed)
                    else:
                        embed = discord.Embed(
                                title="I'm not in a voice channel"
                                )
                        await ctx.respond(embed=embed)

bot = MyBot()

bot.run(token)
