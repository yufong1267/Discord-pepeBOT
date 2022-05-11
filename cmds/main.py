import discord
import os
from discord.ext import commands
from .libs.weather import Get_Weather
from .libs.translate import Get_transResult
from .libs.wiki import wiki
from .libs.sendemail import send_email
from .libs.bbcnews import GetBBCNews
from .libs.sadfacedb import Sadfacedb_operation
from .libs.dreamlistdb import Dreamlist_operation
from .libs.alarm import Alarm
import asyncio, json , datetime
import math
from discord import FFmpegPCMAudio
import youtube_dl
from discord.utils import get
from os import system

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shittyTag(self,ctx):
        await ctx.send(':poop:'*3)

    @commands.command()
    async def 召喚(self,ctx):
        #response = f"hey {mention}, you're great!"
        await ctx.send('我來了')
        await ctx.send(ctx.message.author.mention)

        #await ctx.send(<@!502919267193454614>)
    
    @commands.command()
    async def show_sfdb(self,ctx):
        mention = ctx.message.author.id
        await ctx.send(ctx.message.author.mention)
        reg = Sadfacedb_operation().get_all_data()
        await ctx.send(':o: \n' + reg)
        
    @commands.command()
    async def add_sfdb(self , ctx , * , msg):
        reg = Sadfacedb_operation().sfdb_insert(msg)
        await ctx.send(':o: \n' + reg)     

    @commands.command()
    async def delete_sfdb(self , ctx , * , msg):
        reg = Sadfacedb_operation().sfdb_delete(msg)
        await ctx.send(':o: \n' + reg)    
    
    @commands.command()
    async def show_Dreamlist(self,ctx):
        mention = ctx.message.author.id
        await ctx.send(ctx.message.author.mention)
        reg = Dreamlist_operation().get_all_data()
        await ctx.send(':o: \n' + reg)
        
    @commands.command()
    async def add_Dreamlist(self , ctx , * , msg):
        reg = Dreamlist_operation().sfdb_insert(msg)
        await ctx.send(':o: \n' + reg)     

    @commands.command()
    async def delete_Dreamlist(self , ctx , * , msg):
        reg = Dreamlist_operation().sfdb_delete(msg)
        await ctx.send(':o: \n' + reg)

    @commands.command()
    async def alarm(self, ctx , * , msg):
        #transfer msg to seconds
        para = Alarm().seperate_msg_to_time_and_msg(msg)
        # print(para)

        seconds = Alarm().transfer_to_sec(para[0])
        # print(seconds)

        try:
            #turn number again make sure type
            secondint = int(seconds)
            if secondint <= 0:
                await ctx.send("請輸入正的時:分:秒")
                raise BaseException
            message = await ctx.send("Timer: {seconds}")
            while True:
                secondint -= 1
                print(secondint)
                if secondint == 0:
                    await message.edit(content="Ended!")
                    break
                await message.edit(content=f"Timer: {secondint}")
                await asyncio.sleep(0.7)
            await ctx.send(f"{ctx.message.author.mention}" + para[0] + "時間到了\n" + para[1])
        except ValueError:
            await ctx.send(":o:used: .alarm hr:min:sec msg:content")


    @commands.command()
    async def BBC新聞(self,ctx):
        mention = ctx.message.author.id
        #response = f"hey {mention}, you're great!"
        result = GetBBCNews().NewsFromBBC()
        #get own api key from  https://newsapi.org/
        await ctx.send(':o: \n' + result)
        

    @commands.command()
    async def 天氣(self, ctx , * , city):
        if('-help' in city):
            reg = 'used: .天氣 city \n eg.  .天氣 tainan'
            await ctx.send(':o:' + reg)
        else:
            result = Get_Weather().get_weather(city)
            await ctx.send(result)
    
    @commands.command()
    async def translator(self, ctx , * , words):
        if('-chinese' in words):
            words = words.replace('-chinese' , '')
            result = Get_transResult().get_transResult(sentence = words , dst='zh-TW')
        else:
            result = Get_transResult().get_transResult(sentence = words)
        await ctx.send(':o:' + result)

    @commands.command()
    async def whatis(self , ctx , * , question):
        if('-help' in question):
            reg = 'used: .whatis title \n if you wanna read chinese version you can add -chinese in the end. \n eg.   .whatis discord -chinese'
            await ctx.send(':o:' + reg)
        else:
            trans = False
            if('-trans' in question):
                trans = True #translate
            
            question = question.replace('-trans' , '')
            result = wiki().get_summary(question)
            
            if(trans):
                result = Get_transResult().get_transResult(sentence = result , dst='zh-TW')    
            
            await ctx.send(':o:' + result)

    @commands.command()
    async def 寄信(self , ctx , * , msg):
        if('-help' in msg):
            reg = 'used: .寄信 #toaddr#subject#content \n eg. .寄信 #a2583669@gmail.com#HELLO#Dear. how are you?'
            await ctx.send(':o:' + reg)
        else:
            msg = msg.split('#')
            #msg[1] : toaddr [2]:subject [3]:text
            send_email.send(msg[1] , msg[2] , msg[3])
            
            await ctx.send(':o:信件已送出')

    @commands.command()
    async def calc(self, ctx , * , formula):
        if('rm -rf' in formula):
            await ctx.send('do not do that with rm - rf')
        else:
            ans = eval(formula)
            await ctx.send(str(ans))

    @commands.command()
    async def yt(self, ctx, url):
        channel = ctx.author.voice.channel
        await channel.connect()

        player = await vc.create_ytdl_player(url)
        player.start()

    @commands.command()
    async def leave(self , ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Main(bot))