import discord
import os
from oauth2client import file as oauth_file, client, tools
from discord.ext import commands, tasks
################ Channel, Server, and User IDs ###########################
sphinx_id = 108381986166431744
sk_server = 401186250335322113
bk_server = 691130488483741756
c_server = 800129405350707200
servers = [sk_server, bk_server, c_server]

sk_bot = 401212001239564288
bk_bot = 691205255664500757
bk_ann = 695801936095740024 #BK #announcement
c_bot = 800129405350707200
botinit_id = [sk_bot, bk_bot, c_bot]


prefix = ["/"]
description = "A bot for refine simulation."
intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, description = description, intents = intents)

client.remove_command('help')

@client.event
async def on_ready():
    for server in client.guilds:
        if server.id == sk_server:
            sphinx = server
            break

    for channel in sphinx.channels:
        if channel.id == sk_bot:
            botinitsk = channel
            break
    for channel in cresence.channels:
        if channel.id == c_bot:
            botinitc = channel
            break
    print('Bot is online.')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Getting scolded by Cai'))


@client.event
async def on_member_join(member):
    try:
        role = discord.utils.get(member.guild.roles, id=703643328406880287)
    except AttributeError as e:
        print(f'autorole returned as {e}')
        role = discord.utils.get(member.guild.roles, name="new recruit")
    await member.add_roles(role)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog: {extension}.py loaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog: {extension}.py unloaded')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog: {extension}.py reloaded')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'{filename[:-3]}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

client.run(os.environ['token'], reconnect = True)