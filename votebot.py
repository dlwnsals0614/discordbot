import discord
import datetime
import os

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 터미널에서 출력된다
    print("실행되었습니다")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("열심히 투표"))
    
@client.event
async def on_message(message):
    if message.content.startswith("!투표"):
        vote = message.content[4:].split("/")
        await message.channel.send("투표 " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('👍')
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
