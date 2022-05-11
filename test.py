import discord
from discord.ext import commands
import json
import os

for filename in os.listdir('./cmds'):
    print(filename[:-3])
