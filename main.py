import discord
import random


class character():
    name = ""
    maxSpirit = 1
    spirit = 1
    inventory = []
    location = ""
    emblem = ""
    charType = ""


class town():
    buildings = []
    townspeople = []
    partyName = ""
    partyMembers = []
    partyEmblem = ""


class players(character):
    equipment = []
    materials = []
    party = ""


class enemies(character):
    enemyDescription = ""
    combatAbilities = []


class menus():
    textPrompt = []
    reactions = []
    parentMenu = None
    childMenus = []


class dungeonInfo():
    difficulty = 1
    numRooms = random.randint(4,8)
    themes = []
    materialsTable = []


def prw(botprint):
    client.send_message(message.channel, botprint)


TOKEN = 'NDQ1MDgzOTgxODg1NDcyNzc4.DdlmZA.7R8n1IbPUvV4smtJQXhdCsEaJko'

client = discord.Client()


@client.event
#async def newplayer():
#    newplayerinfo = players()
#
#    prw('''As you walk, the forest grows denser.  What little light shines through the canopy is muted by the dull grey bark on the gnarled trees.  The cold clings to your skin and gives you pause.  The stench of wet moss emanates from above.  You follow a blue glowing circuit embedded in the rocks at your feet.  At times you lose it in the bushes and have to wade through thorns to keep on your path.  Where this circuit leads, you do not know.
#
#You have followed the circuit for so long, you lost track of time.  Has it been hours or days?  As you consider giving up and turning back, you come upon a boulder with a figure sitting on it.  The figure appears to be a statue, but has subtle, organic movements.  Its shoulders appear relaxed, and its feet sway to and fro.  Its eye stalks track you, scanning you up and down.
#
#"You, too, follow the circuit? And what is your name?"''')

#    newplayerinfo.name = await


async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('🖐'):
        emojis = ['👍', '👎']
        auth = message.author
        msg = await client.send_message(message.channel, 'Choose a reaction.')
        for emoji in emojis:
            await client.add_reaction(msg, emoji)
        res = await client.wait_for_reaction(['👍', '👎'], user=auth, message=msg)
        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))

    if message.content.startswith('*⃣'):
        emojis = ['📖', 'ℹ']
        msg = await client.send_message(message.channel, 'You have accessed the menu.  Choose an option.')
        for option in emojis:
            await client.add_reaction(msg, option)


async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
