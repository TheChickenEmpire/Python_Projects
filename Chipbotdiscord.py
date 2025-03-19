import discord
from discord.ext import commands
token = "MTMxODg0NTcwNjU5MjcxNDc5Mg.G-kvob.Tm6xQ-EZ91V4jRC0yv0xnmMuzoG7W0iDwCMrNo"
client = commands.Bot(command_prefix="!", intents='')
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
client.run(token)