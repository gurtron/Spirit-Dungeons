import discord
from main import *

TOKEN = 'NDQ1MDgzOTgxODg1NDcyNzc4.DdlmZA.7R8n1IbPUvV4smtJQXhdCsEaJko'

client = discord.Client()


sampleMenuObject = menus(client)

sampleMenuObject.addMessageToList("There is a door.",{"🚪":"Open Door", "😬":"Listen at door"})


async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
