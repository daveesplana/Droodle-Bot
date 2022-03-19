import discord

@bot.event
async def on_ready():
  print('Online')

bot.run(token)
