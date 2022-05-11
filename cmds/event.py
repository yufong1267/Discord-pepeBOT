import discord
from discord.ext import commands


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,msg):
        content = msg.content
        if("good night" in content or "Good night" in content):
            await msg.channel.send("晚安")
            await msg.channel.send(msg.author.mention)
        if("pepe good job" in content or "bot good job" in content):
            await msg.channel.send("thank you小意思")
            await msg.channel.send(msg.author.mention)
        #if(msg.author.name == "Yufong1267"):
        #    await msg.delete()


    
    @commands.command()
    async def readpic(self, ctx , * , question):
        s = question.split()
        for s_int in s:
            if(s_int.isdigit()):
                n = int(s_int)
        await ctx.send(type(question))


    
    


def setup(bot):
    bot.add_cog(Event(bot))