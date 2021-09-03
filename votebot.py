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
            
@client.event
async def on_message(message):
    if message.content.startswith("!계산기"):
        m = await message.channel.send("계산기 로딩중...")
        expression = "None"
        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        e = Embed(title = f"{message.author.name}님의 계산기 | {message.author.id}",description = expression,timestamp = delta)
        buttons = [
            [
                Button(style=ButtonStyle.gray,label="1",disabled=0),
                Button(style=ButtonStyle.gray,label="2",disabled=0),
                Button(style=ButtonStyle.gray,label="3",disabled=0),
                Button(style=ButtonStyle.blue,label="x",disabled=0),
                Button(style=ButtonStyle.red,label="ㅤ나가기ㅤ",disabled=0), 
            ],
            [
                Button(style=ButtonStyle.gray,label="4",disabled=0),
                Button(style=ButtonStyle.gray,label="5",disabled=0),
                Button(style=ButtonStyle.gray,label="6",disabled=0),
                Button(style=ButtonStyle.blue,label="÷",disabled=0),
                Button(style=ButtonStyle.red,label="ㅤ지우기ㅤ",disabled=0), 
            ],
            [
                Button(style=ButtonStyle.gray,label="7",disabled=0),
                Button(style=ButtonStyle.gray,label="8",disabled=0),
                Button(style=ButtonStyle.gray,label="9",disabled=0),
                Button(style=ButtonStyle.blue,label="+",disabled=0),
                Button(style=ButtonStyle.red,label="모두지우기",disabled=0), 
            ],
            [
                Button(style=ButtonStyle.gray,label="00",disabled=0),
                Button(style=ButtonStyle.gray,label="0",disabled=0),
                Button(style=ButtonStyle.gray,label=".",disabled=0),
                Button(style=ButtonStyle.blue,label="-",disabled=0),
                Button(style=ButtonStyle.green,label="ㅤㅤ=ㅤㅤ",disabled=0), 
            ]
        ]
        def calculator(exp):
            o = exp.replace("x","*")
            o = o.replace("÷","/")
            result = ""
            try:
                result=str(eval(o))
            except:
                result = "An error Occoured"
            return result

        await m.edit(components = buttons,embed = e)
        while m.created_at < delta:
            res = await client.wait_for("button_click")
            if res.author.id == int(res.message.embeds[0].title.split("|")[1]) and res.message.embeds[0].timestamp < delta:
                expression = res.message.embeds[0].description
                if expression == "None" or expression == "An error Occoured":
                    expression = ""
                if res.component.label == "ㅤ나가기ㅤ":
                    await res.respond(content = "계산기를 종료하였습니다",type = 7)
                    break
                elif res.component.label == "ㅤ지우기ㅤ":
                    expression = expression[:-1]
                elif res.component.label == "ㅤㅤ=ㅤㅤ":
                    expression = calculator(expression)
                elif res.component.label == "모두지우기":
                    expression = None
                else:
                    expression += res.component.label
                f = Embed(title = f"{message.author.name}님의 계산기 | {message.author.id}",description = expression,timestamp = delta)
                await res.respond(content = "",embed = f,components = buttons,type = 7)
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
