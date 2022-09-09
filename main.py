import discord
from discord.ext import commands
import os
client = commands.Bot(command_prefix= '.', intents = discord.Intents.default())

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Game("Detroit Become Human"))

initial_extensions = []

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    initial_extensions.append('cogs.' + filename[:-3])

if __name__ == '__main__':
  for extension in initial_extensions:
    client.load_extension(extension)

client.run('MTAwMzM2MzgyNDQ5OTQzNzc4MA.GApgIF.f1YkiPaZ2jqT3N4LwVD3so2XqSuAufJLyjeF2A')
