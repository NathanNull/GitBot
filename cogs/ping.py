from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(ctx, self):
        await ctx.send('Pong!')
print("hi45")
def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Ping(bot)) # add the cog to the bot