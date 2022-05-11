import discord
from discord.ext import commands 

class React(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def food(self, ctx , * , question):
        #[int(s) for s in question.split() if s.isdigit()]
        s = question.split()
        for s_int in s:
            if(s_int.isdigit()):
                n = int(s_int)
        await ctx.send(':hamburger:' * n)
    
    #:poop:
    @commands.command()
    async def poo(self, ctx , * , question):
        #[int(s) for s in question.split() if s.isdigit()]
        s = question.split()
        for s_int in s:
            if(s_int.isdigit()):
                n = int(s_int)
        await ctx.send(':poop:' * n)

    

def setup(bot):
    bot.add_cog(React(bot))