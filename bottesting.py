import discord

TOKEN = 'NDQ1MDgzOTgxODg1NDcyNzc4.DdlmZA.7R8n1IbPUvV4smtJQXhdCsEaJko'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('🆕'):
        emojis = ['👍', '👎']
        auth = message.author
        msg = await client.send_message(message.channel, 'Choose a reaction.')
        for emoji in emojis:
            await client.add_reaction(msg, emoji)
        res = await client.wait_for_reaction(['👍', '👎'], user=auth, message=msg)
        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))


async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
