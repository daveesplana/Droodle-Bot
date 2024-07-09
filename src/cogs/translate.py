import discord
from discord.ext import commands
from deep_translator import GoogleTranslator

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Translates a message to a different language.")
    async def translate(self, ctx, language: str, *, text: str):
        translate = GoogleTranslator(source='auto', target=language).translate(text)
        try:
            embed = discord.Embed(
                title="Translated to:",
                description=translate,
                color=discord.Color.blue()
            )
            await ctx.respond(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="Error:",
                description=str(e),
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Translate(bot))
