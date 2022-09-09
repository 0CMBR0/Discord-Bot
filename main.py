import discord
from discord.ext import commands
import os
token = 'MTAwMzM2MzgyNDQ5OTQzNzc4MA.GApgIF.f1YkiPaZ2jqT3N4LwVD3so2XqSuAufJLyjeF2A'
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


"""
@client.command()
async def load (ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def reload (ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload (ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('.\cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

"""
"""
@client.event
async def on_member_join(member):
  print (f'{member} has joined a sever.')

@client.event
async def on_member_remove(member):
  print (f'{member} has boi yoing yoing off the server fam.')
"""