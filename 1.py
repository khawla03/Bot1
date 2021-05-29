import discord
import os
import random
import asyncio
from discord import reaction


client = discord.Client()
lst = []
#creds = None
#service = build('docs', 'v1', credentials=creds)
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content
 
  if msg.startswith('$create'):
    date = msg[8:18]
    time = msg[19:]
    str=date+time
    await message.channel.send(str)
    if str not in lst: 
      lst.append(str)
      print(lst)
      await message.channel.send('!create meeting on ' + date + ' at ' + time)
    else:
      await message.channel.send('a meeting on that timing already exists') 
  else:
   if msg.startswith('$pv'):
     title = 'pv'
     body = {
      'title': title
     }
    
     #doc = service.documents() \
     #.create(body=body).execute()
     # print('Created document with title: {0}'.format(
     # doc.get('title')))
     await message.channel.send('pv created')
   else:
     if msg.startswith('$meet'):
       await message.channel.send('pv created')
       

@client.event
async def on_message(message):
    if message.content.startswith('$meet'):
        msg = message.content 
        i = msg.find('/')
        j = msg.find('at')
        print(i)
        embedVar = discord.Embed(title="Meeting", description= message.channel.name + ' meeting , react with ✅' , color=0x00ff00)
        embedVar.add_field(name="Date", value=msg[i-2:i+8], inline=False)
        embedVar.add_field(name="time", value=msg[j:], inline=False)
        await message.channel.send(embed=embedVar)

        #insert_field_at(index, *, name, value, inline=True)
        channel = message.channel
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '✅'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('personne ne peux faire le pv ?')
        else:
            users = await reaction.users().flatten()
            rapporteur = random.choice(users)
            await message.channel.send('le rapporteur : '+rapporteur.mention)

        #await message.channel.send('{} has won the raffle.'.format(winner))
    

client.run(os.getenv('TOKEN'))

#$create 12/12/2020 8pm