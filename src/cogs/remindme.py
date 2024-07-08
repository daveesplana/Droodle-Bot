import discord
import asyncio
from discord.ext import commands

class RemindMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Allows users to set reminders.")
    async def remindme(self, ctx, time: int, *, message: str):
        if not message:
            embed = discord.Embed(
                title="The message cannot be blank.",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed)
            return

        embed = discord.Embed(
            title=f"I will remind you in {time} seconds.",
            color=discord.Color.purple()
        )
        await ctx.respond(embed=embed)
        await asyncio.sleep(time)
        
        embed = discord.Embed(
            title=f"{ctx.author.name}, you wanted me to remind you:",
            description=message,
            color=discord.Color.purple()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(RemindMe(bot))
