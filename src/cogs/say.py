import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Prompts the user to display a message.")
    async def say(self, ctx, *, message: str):
        embed = discord.Embed(
            description=message,
            color=discord.Color.blue()
        )
        await ctx.respond("Here's the message.", embed=embed)

def setup(bot):
    bot.add_cog(Say(bot))
