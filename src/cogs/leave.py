import discord
from discord.ext import commands

class Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Allows the bot to leave a voice channel.")
    async def leave(self, ctx):
        if ctx.voice_client:
            embed = discord.Embed(
                title="Left the voice channel",
                color=discord.Color.green()
            )
            await ctx.voice_client.disconnect()
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                title="I'm not in a voice channel",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Leave(bot))
