import discord

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="you"))
    print(f'Logging in as {bot.id}')
    print('Online!')
    
@slash.slash(
  title="ping",
  description="pong!"
)
async def ping(self, ctx):
  await ctx.send('Pong!')
    
bot.run(token)
