import discord
from discord.ext import commands
import random

class Minorcommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hey, I am the everything discord bot!')

    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send('Wow leaving me alone like this...')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot has arrived.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Welcome {member} to the {member.guild} server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server :(')

    @commands.command()
    async def val(self, ctx):
        await ctx.send('Damn you are a sweat, go touch some goddamn grass')

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send("boing yoing yoing!")

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send("I mean you saw this coming...right?")

    @commands.command()
    async def future(self, ctx, *, question):
        responses = ["Guaranteeeeeed!",
                     "Seems like it.",
                     "Ofc my guy",
                     "Oh most definitely.",
                     "Very probable.",
                     "The possibility is up there.",
                     "Yeah?",
                     "Don't count on it.",
                     "Areeb says no.",
                     "Statistics say no.",
                     "I doubt it.",
                     "Outlook not really great."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        await ctx.send("What other probabilities are you dying to know?"

        @commands

def setup(client):
    client.add_cog(Minorcommands(client))
