import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Gives users information.")
    async def userinfo(self, ctx, user: discord.User):
        user_id = user.id
        username = user.name
        discriminator = user.discriminator
        created_at = user.created_at.strftime('%B %d, %Y')
        joined_at = user.joined_at.strftime('%B %d, %Y') if hasattr(user, 'joined_at') else 'N/A'
        
        embed = discord.Embed(
            title=f"{username}#{discriminator}",
            description=f"ID: {user_id}",
            color=discord.Color.green()
        )
        embed.add_field(
            name="Account Created",
            value=created_at,
            inline=True
        )
        embed.add_field(
            name="Date Joined",
            value=joined_at,
            inline=True
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(UserInfo(bot))
