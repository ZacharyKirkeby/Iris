import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

# Establishes connection 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))
intents = discord.Intents.all()

client = discord.Client(intents=intents)
print(GUILD, type(GUILD))
guild = await client.get_guild(GUILD)

@client.event
async def on_ready():
    # load information in iris_config.json
    print(f'{client.user} has arrived')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    


members = '\n - '.join([member.name for member in guild.members])
print(f'Guild Members:\n - {members}')

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
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    if message.content.startswint('$hello'):
        await message.channel.send('Hello!')

@commands.Cog.listener()
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    member = payload.member
    message_id = payload.message_id
    reaction = payload.emoji
    if message_id == 'role id here!!!!!':
        #assign role
        pass

@commands.Cog.listener()
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    member = payload.member
    message_id = payload.message_id
    reaction = payload.emoji
    if message_id == 'role id here!!!!!':
        #remove role
        pass
client.run(TOKEN)