import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Establishes connection 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

members = '\n - '.join([member.name for member in guild.members])
print(f'Guild Members:\n - {members}')

complaint_channel = ""

role_post_id = ""
role_refrence = {
    # emoji : role
}

client = commands.Bot(command_prefix='~')
# gen format of a command, 
@client.command()
async def commandCall(ctx):
  await ctx.send('output')

# this function will be used to config the bot to set input and output channels for certin features
@client.command()
async def setup(ctx):
      pass

# this function will 

intents = discord.Intents.default()
intents.message_content = True

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswint('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)