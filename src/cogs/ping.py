import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Sends bot Latency.")
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Pong!",
            description=f"Latency is {self.bot.latency:.2f} ms.",
            color=discord.Colour.blurple()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))
