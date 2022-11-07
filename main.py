import discord
import os
from discord.ext import commands
from rockscissorspaper import *
from db import *



intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_member_join(member):
    joindate = str(member.joined_at.date())
    role = member.roles
    data = {'userID':member.id,
            'money':0,
            'role':str(role[0]),
            'joinDate':joindate}
    insertDB('discord',data)

@bot.event
async def on_member_remove(member):
    userid = member.id
    deleteDB('discord', userid)

@bot.command()
async def 랭킹(ctx):
    data = sortDB('discord', 'money')
    embed = discord.Embed(title='랭킹')
    for index, db in enumerate(data):
        embed.add_field(name=f'{index + 1}.{await bot.fetch_user(db["userID"])}', value=f'소지금 : `{db["money"]}`',inline=False)
    await ctx.channel.send(embed=embed)

@bot.command()
async def 가위바위보(ctx, _user):
    user = switch(_user)
    print(user)
    result, bot = rsp(user)
    if(result == '승리'):
        current_money = findDB('discord',ctx.author.id)
        updateDB('discord', ctx.author.id, 'money', current_money["money"] + 10)
        result = '승리 +10POINT'
    embed = discord.Embed(title= f'{result}', description=f'**`{ctx.author}: {_user}\n'
                                                   f'로봇: {bot}`**')

    await ctx.channel.send(embed=embed)

@bot.command()
async def 내정보(ctx):
    data = findDB('discord', ctx.author.id)
    embed = discord.Embed(title='내정보',description=f'**소지금:`{data["money"]}`** \n'
                                                  f'**가입일자:`{data["joinDate"]}`** \n'
                                                  f'**역할:`{data["role"]}`**\n ')
    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
    await ctx.channel.send(embed=embed)

@bot.command()
async def 돈(ctx, arg1, arg2):
    try:
        id = ctx.guild.get_member_named(arg1).id
        updateDB('discord', id, 'money', int(arg2))
        await ctx.channel.send('수정완료')
    except:
        await ctx.channel.send('수정실패')
bot.run(os.environ['token'])