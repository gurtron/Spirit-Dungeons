import discord
import random

# List of invented data structures
#
#
#
#

class item:
    itemName = ""
    itemDescription = ""
    itemEquip = False


class inventory:
    items = {}

    def checkItem(self, itemType):
        return itemType in self.items

    def checkCount(self, itemType):
        if self.checkItem(itemType):
            return self.items[itemType]
        else:
            return 0

    def addItem(self, itemToAdd, itemNumber):
        if self.checkItem(itemToAdd):
            self.items[itemToAdd] += itemNumber
        else:
            self.items[itemToAdd] = itemNumber

    def removeItem(self, itemToRemove, itemNumber):
        if self.checkItem(itemToRemove) >= itemNumber:
            self.items[itemToRemove] -= itemNumber
        else:
            return False


  #  def countItems(self, items):

  #  def returnItems(self, items):





class character(inventory):
    charName = ""
    maxSpirit = 1
    spirit = 1
    charInventory = inventory()
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


class enemies(character):
    enemyDescription = ""
    combatAbilities = []


class menus:
    client = None
    messageDictionary = {}

    def __init__(self, client):
        self.client = client

    def addMessageToList(self,message,reactions):
        self.messageDictionary[message] = reactions

    @client.event
    async def on_message(self, message):
        if message.content.startswith("😉"):
            replyString = ' '.join(list(self.messageDictionary.keys())), " \n\n", self.messageDictionary
            botMessage = await self.client.send_message(message.channel,replyString)
            for message in self.messageDictionary:
                reactionList = self.messageDictionary[message]
                for emoji in reactionList:
                    await self.client.add_reaction(botMessage, emoji)


class dungeonInfo():
    difficulty = 1
    numRooms = random.randint(4,8)
    themes = []
    materialsTable = []
