"""
This cog file is utilized to create a sort of "mod-mail" where the member is able to message a discord moderator by
directly messaging this bot. The moderator can see this message in the "mod-mail" channel in the server and can send
a message back to the member by mentioning themselves and typing their message in the channel.
"""
import discord
from discord.ext import commands
client=discord.Client()

class Modcommunication(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        empty_array = []
        modcomms_channel = discord.utils.get(client.get_all_channels(), name="mod-comms")
        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                await modcomms_channel.send("[" + message.author.display.name + "]")
                for file in files:
                    await modcomms_channel.send(file.url)
            else:
                await modcomms_channel.send("[" + message.author.display.name + "]" + message.content)

        """
        This if condition is required to allow the bot to send the message/file sent by the member to the mod communication 
        channel. In the channel it will display the username of the member and their message.
        """
        if str(message.channel) == "mod-comms" and message.content.startswith("<"):
            member_object = message.mentions[0]
            if message.attachments != empty_array:
                files = message.attachments
                await member_object.send("[" + message.author.display_name + "]")

                for file in files:
                    await member_object.send(file.url)
            else:
                index = message.content.index(" ")
                string = message.content
                mod_message = string[index:]
                await member_object.send("[" + message.author.display_name + "]" + mod_message)
"""
This elif statement is utilized to let the bot to transport the message/file sent by the moderator to the direct message 
section between the bot and the member. In the section it will display the username of the moderator and their reply.
"""
def setup(client):
    client.add_cog(Modcommunication(client))