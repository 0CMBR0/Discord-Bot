import discord
from discord.ext import commands
import wavelink

class CustomPlayer(wavelink.Player):
    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.bot, host="127.0.0.1", port=2333, password="youshallnotpass")

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f'Node: <{node.identifier}> is ready!')

    @commands.command()
    async def connect(self, ctx):
        general = ctx.voice_client
        custom_player = CustomPlayer()
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            return await ctx.send("Get on the vc for the tunes.")

        if not general:
            await ctx.author.voice.channel.connect(cls=custom_player)
        else:
            await ctx.send("The tune cranker is already on the vc, what're you on about?")

    @commands.command()
    async def disconnect(self, ctx):
        general = ctx.voice_client
        if general:
            await general.disconnect()
        else:
            await ctx.send("The ultimate bot isn't on the vc.")

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        general = ctx.voice_client
        if not general:
            custom_player = CustomPlayer()
            general: CustomPlayer = await ctx.author.voice.channel.connect(cls=custom_player)

        if general.is_playing():
            general.queue.put(item=search)
            await ctx.send(embed = discord.Embed(
                title = search.title,
                url = search.uri,
                author = ctx.author,
                description = f"Queued {search.title} in {general.channel}"))
        else:
            await general.play(search)
            await ctx.send(embed=discord.Embed(
                title = search.title,
                url = search.uri,
                author = ctx.author,
                description = f"Queued {search.title} in {general.channel}"))

    @commands.command()
    async def skip(self, ctx):
        general = ctx.voice.client
        if general:
            if not general.is_playing():
                return await ctx.send("Nothing is being played.")
            elif general.queue_empty:
                return await general.stop()
            await general.seek(general.track.length * 1000)
            if general.is_paused():
                await general.resume()
        else:
            await ctx.send("The ultimate bot is not connected to the vc.")

    @commands.command()
    async def pause(self, ctx):
        general = ctx.voice.client
        if general:
            if general.is_playing() and not general.is_paused():
                await general.pause()
            else:
                await ctx.send("Nothing is being played.")
        else:
            await ctx.send('The everything bot is not connected to a vc.')

    @commands.command()
    async def resume(self, ctx):
        general = ctx.voice.client
        if general:
            if general.is_paused():
                await general.resume()
            else:
                await ctx.send("Nothing is paused.")
        else:
            await ctx.send("The everything bot is not connected")

def setup(client):
    client.add_cog(Music(client))
