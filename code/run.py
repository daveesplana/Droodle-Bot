import discord

@bot.event
async def on_ready():
    print(f'Logging in as {bot.id}.')
    print('Online!')
    
@slash.slash(
  name="ping",
  description="pong!"
)
async def ping(self, ctx):
  await ctx.send('Pong!')
    
bot.run(token)
