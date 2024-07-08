import discord
from discord.ext import commands
from translate import Translator  # Ensure you have the correct import for the translation library you're using

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Translates a message to a different language.")
    async def translate(self, ctx, language: str, *, text: str):
        translator = Translator(to_lang=language)
        try:
            translation = translator.translate(text)
            embed = discord.Embed(
                title="Translated to:",
                description=translation,
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
