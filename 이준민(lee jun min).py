import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('안녕')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft"))

@client.event
async def on_message(message):
    content = message.content

    # !명령어를 입력할 시에 내가 지정해둔 명령어 알려주기
    if content.startswith("!명령어"):
        embed=discord.Embed(description="!안녕 \n!시간 \n!오피 \n!닥지지", color=0x00ff56)
        # embed=discord.Embed(description="", color=0x00ff56) => 부가설명(작은 글씨)
        embed.set_author(name="!명령어 종류")
        # embed.set_author(name="") => 타이틀(큰 글씨)
        await message.channel.send(embed=embed)
    
    # 특정한 단어 입력시 지정한 단어 출력
    if message.content.startswith('!안녕'):
        await message.channel.send('반가워!')

    # 임베드 및 임베드에 사진 추가
    if content.startswith("!성인겜"):
        embed=discord.Embed(description="성인겜 그 이름은 -MINECREAFT-", color=0x00ff56)
        embed.set_author(name="성인겜 마크 ㄷㄷ;;;" , url="https://s.pstatic.net/dbscthumb.phinf/5116_000_1/20171130231249674_30P9MUJ0Z.png/logo_4.png?type=m1500_q100")
        embed.set_thumbnail(url="https://s.pstatic.net/dbscthumb.phinf/5116_000_1/20171130231249674_30P9MUJ0Z.png/logo_4.png?type=m1500_q100")
        await message.channel.send(embed=embed)
    
    # 시간
    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))
    
    # 링크
    if content.startswith("!오피"):
        embed=discord.Embed(description="오피.지지", color=0x00ff56)
        embed.set_author(name="op.gg링크 => https://www.op.gg/" , url="https://www.op.gg/")
        embed.set_thumbnail(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA0MjRfMjYy%2FMDAxNTg3Njk0MzEyMDI1.jtJyQcnk1oL22EfoJZtGpIXiAV9GDh4TtL6jWulMmXMg.wf0ta1BVrJfZL1q8jFbqaL2ijbO92sh8Q-hZKQviKdEg.PNG.jypjin%2Freverse_rectangle.png&type=sc960_832")
        await message.channel.send(embed=embed)

    if content.startswith("!닥지지"):
        embed=discord.Embed(description="닥지지", color=0x00ff56)
        embed.set_author(name="dak.gg링크 => https://www.dak.gg/" , url="https://www.dak.gg/")
        embed.set_thumbnail(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fdak.gg%2F%3Fhl%3Dko-KR&psig=AOvVaw1hp5dBd_phD-8Ii2gkut28&ust=1628138300899000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCICm5PvFlvICFQAAAAAdAAAAABAD")
        await message.channel.send(embed=embed)

client.run('ODcyMDk4MjM1NzEwMzE2NTc0.YQk6xg.njG1JscurAgGHVHxflgio82kQUA')