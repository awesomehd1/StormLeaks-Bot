import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def tomorrow(ctx):
    await ctx.send("tomorrow's shop https://stormleaks.tk/shopimage/screenshot-fnbr.co-2018-09-08-20-05-59-330.png")

bot.run('<YOUR_TOKEN_HERE>')
