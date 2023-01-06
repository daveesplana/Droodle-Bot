import discord

bot = discord.Bot()

@bot.event
async def on_ready():
       print(f"Logged in as {bot.user} ID: {bot.user.id}")
       print("Bot Online!")

bot.run(token)
