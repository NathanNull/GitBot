#Import packages
import discord
from discord.ext import commands
import os
import datetime
import pytz

#Define variables to make the rest run
token = os.environ['TOKEN'] 

class Bot(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_connect(self):
        print("hi3")
        
    #Triggers when anyone sends a message
    async def on_message(self, message):
        #If the person sending the message is this bot, it ignores it
        if message.author == self.user:
            return
        #If someone sends something starting with $hello, it sends "Hello!"
        if message.content.startswith('$hello'):
              await message.channel.send('Hello!')
          
        #Gets the time from the getTime function
        if message.content.startswith('$time'):
          await message.channel.send(getTime())

    @commands.command()
    async def ping2(self, ctx):
        ctx.channel.send("pong 2")

#A basic slash command
      
#@discord.slash_command(guild_ids=[977331948890521620])
#async def hello(ctx):
  #await ctx.respond("Hello!")



def getTime():
  #set time zone
  t = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Los_Angeles"))
  
  #Converts the day of the week from integer to day
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Thursday", "Friday", "Saturday", "Sunday"]
  weekday = days[t.weekday()]
  
  #Convert the time to am or pm
  if t.hour < 12:
    hour = t.hour
    ampm = 'am'
  elif t.hour == 12:
    hour = t.hour
    ampm = 'pm'
  elif t.hour > 12:
    hour = t.hour - 12
    ampm = 'pm'
  else:
    hour = 'ERR'
    ampm = 'OR'

  #gets the month, day, and time from datetime
  return t.strftime(f'{weekday}, %B %d, {hour}:%M{ampm}')
  
print("hi")
#Runs the bot
self = Bot(command_prefix="$")
self.load_extension("cogs.ping")
print("hi 2")

self.run(token)
