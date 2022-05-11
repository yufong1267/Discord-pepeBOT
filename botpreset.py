import discord
from discord.ext import commands
import json
import os

##開啟setting.json
with open('setting.json','r' , encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = '.')  #啟用command的呼叫 .command

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_member_join(member):
    print(f'{member} 加入頻道')

@bot.event
async def on_member_remove(member):
    print(f'{member} 離開頻道')  

@bot.command()
async def rename(ctx, name):
    await bot.user.edit(username=name)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'unloaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'reloaded {extension} done.')


for filename in os.listdir('./cmds'):
    if(filename.endswith('.py')):
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(jdata['TOKEN'])







