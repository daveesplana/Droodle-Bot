import discord
from discord.ext import commands

class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Allows the bot to join a channel.")
    async def join(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="You must be in a voice channel.",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed)
            return

        channel = ctx.author.voice.channel
        await channel.connect()
        embed = discord.Embed(
            title=f"Joined {channel.name}",
            color=discord.Color.green()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Join(bot))
