import discord

from main import sifreolusturucu
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('bana fikirler sun'):
        await message.channel.send("çöpleri çöpe atın")
    elif message.content.startswith('fikirler ver'):
        await message.channel.send("geri dönüşümlü poşetleri deneyebilirsin")
    else:
        await message.channel.send(message.content)

client.run("tokeniniz")