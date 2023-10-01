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

def get_iris_data():
    global data_dict
    with open('iris_config.json','r') as iris_config:
        iris_dict = json.load(iris_config)
    return iris_dict

data_dict = get_iris_data()

def save_iris_data():
    global data_dict
    with open('iris_config.json', 'w') as iris_config:
        iris_config.write(json.dumps(data_dict))

bot = commands.Bot(intents=intents,command_prefix='!',activity = discord.Game(name="Not Showering"))

@bot.command(name = 'test', help = 'test method')
async def _test(ctx):
    await ctx.send("response") 

@bot.command(name='rats',help='lists all who are certified rat ticklers')
async def _rat(ctx):
    await ctx.send("The following are our Certified Rat Ticklers (CRT): \n Holden \n Zach \n Idk")

@bot.command(name='sexism',help='The bot is also a cs major')
async def _sexism(ctx):
    await ctx.send("I hate women \n -Unknown CS major")

@bot.command(name='tiddy',help='tiddy')
async def _tiddy(ctx):
    await ctx.send("What do men like?: \n TIDDY")

# gen format of a command, 
@bot.command(name = 'command')
async def _command(ctx, arg):
  await ctx.send(arg)

@bot.command(name='quote')
async def _quote(ctx, quote, person):
    global data_dict
    print(data_dict)
    print(globals()["data_dict"])
    quote_channel_id = data_dict['quote_channel_id']
    print(quote_channel_id)
    quote_channel = bot.get_channel(quote_channel_id)
    await quote_channel.send(f"\"{quote}\" - {person}")

@bot.command(name='set_quote')
async def _set_quote(ctx: commands.Context):
    global data_dict
    quote_channel_id = ctx.channel.id
    
    data_dict.update({'quote_channel_id':quote_channel_id})
    save_iris_data()

@bot.event
async def on_ready():
    # load information in iris_config.json
    global data_dict

    print(f'{bot.user} has arrived')

@bot.event
async def on_ready():
    guild = bot.get_guild(GUILD)
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
# this function will 

intents = discord.Intents.default()
intents.message_content = True  
@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('I touch rats')
    await bot.process_commands(message)    
    
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

bot.run(TOKEN)