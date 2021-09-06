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
            
    if message.content.startswith ("!프필 "):
        #await message.delete()
        profile = message.mentions[0]
    
        embed = discord.Embed(title=f"{message.author.name}님께서 요청하신 {profile}님의 프로필 입니다.")
        embed.set_image(url=profile.avatar_url)
    
        await message.channel.send(embed=embed)
        
@client.event
async def on_message(message):
    if message.content.startswith("!계산기"):
        m = await message.channel.send("계산기 로딩중...")
        expression = "None"
        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
        e = Embed(title = f"{message.author.name}님의 계산기 ",description = expression,timestamp = (delta))
        msg_name = message.author
        buttons = [
            [
                Button(style=ButtonStyle.black,label="1",disabled=0),
                Button(style=ButtonStyle.black,label="2",disabled=0),
                Button(style=ButtonStyle.black,label="3",disabled=0),
                Button(style=ButtonStyle.blue,label="x",disabled=0),
                Button(style=ButtonStyle.red,label="ㅤ나가기ㅤ",disabled=0), 
            ],
            [
                Button(style=ButtonStyle.black,label="4",disabled=0),
                Button(style=ButtonStyle.black,label="5",disabled=0),
                Button(style=ButtonStyle.black,label="6",disabled=0),
                Button(style=ButtonStyle.blue,label="÷",disabled=0),
                Button(style=ButtonStyle.red,label="ㅤ지우기ㅤ",disabled=0), 
            ],
            [
                Button(style=ButtonStyle.black,label="7",disabled=0),
                Button(style=ButtonStyle.black,label="8",disabled=0),
                Button(style=ButtonStyle.black,label="9",disabled=0),
                Button(style=ButtonStyle.blue,label="+",disabled=0),
                Button(style=ButtonStyle.red,label="모두지우기",disabled=0), 
            ],
            [
                Button(style=ButtonStyle.black,label="00",disabled=0),
                Button(style=ButtonStyle.black,label="0",disabled=0),
                Button(style=ButtonStyle.black,label=".",disabled=0),
                Button(style=ButtonStyle.blue,label="-",disabled=0),
                Button(style=ButtonStyle.green,label="ㅤㅤ=ㅤㅤ",disabled=0), 
            ],
            [
                Button(style=ButtonStyle.black,label="(",disabled=0),
                Button(style=ButtonStyle.black,label=")",disabled=0),
                Button(style=ButtonStyle.black,label="x²",disabled=0),
                Button(style=ButtonStyle.black,label="√",disabled=0),
                Button(style=ButtonStyle.black,label="ㅤㅤ𝝅ㅤㅤ",disabled=0), 
            ]
        ]
        def calculator(exp):
            o = exp.replace("x","*")
            o = o.replace("÷","/")
            o = o.replace("²","**2")
            o = o.replace("√","**(1/2)")
            o = o.replace("𝝅","")
            result = ""
            try:
                result=str(eval(o))
            except:
                result = "오류가 났어요(┬┬﹏┬┬)"
            return result
        made_at = datetime.timedelta(minutes=2)
        await m.edit(components = buttons,embed = e)
        while m.created_at < delta:
            res = await client.wait_for("button_click")
            if res.author == msg_name:
                if datetime.datetime.utcnow() + datetime.timedelta(minutes=2) > datetime.datetime.utcnow():
                    expression = res.message.embeds[0].description
                    if expression == "None" or expression == "오류가 났어요(┬┬﹏┬┬)":
                        expression = ""
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    if res.component.label == "ㅤ나가기ㅤ":
                        await res.respond(content = "계산기를 종료하였습니다",type = 7)
                        break
                    elif res.component.label == "ㅤ지우기ㅤ":
                        expression = expression[:-1]
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    elif res.component.label == "ㅤㅤ=ㅤㅤ":
                        expression = calculator(expression)
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    elif res.component.label == "모두지우기":
                        expression = "None"
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    elif res.component.label == "x²":
                        expression += "²"
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    elif res.component.label == "√":
                        expression += res.component.label
                        expression = calculator(expression)
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    elif res.component.label == "ㅤㅤ𝝅ㅤㅤ":
                        expression += "𝝅"
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    else:
                        expression += res.component.label
                        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    if expression == "":
                        expression = "None"
                    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
                    msg_name = message.author
                    f = Embed(title = f"{message.author.name}님의 계산기 ",description = expression,timestamp = (delta))
                    await res.respond(content = "",embed = f,components = buttons,type = 7)
                else:
                    await res.respond(content = "오래된 계산기에요......")
                    break
            else:
                await res.respond(content = "남의것을 사용하려하지말고 자신의것을 사용하세요!")
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
