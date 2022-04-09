import discord
from discord.ext import commands
import os
import asyncio
import random


intents = discord.Intents.default()
intents.members = True

testing = False
lista = ["Vai se foder", "Olá", "Tá carente?", "Não estou afim de conversar", "Você acaba de ganhar 1 biscoito"]
cli = discord.Client()

client = commands.Bot(command_prefix = "$", case_insensitive = True, intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="$help"))


@client.command(name="ola", help="Responde com seu nome incluido",aliases=['oi'])
async def ola(ctx):
    await ctx.send(f'{random.choice(lista)} {ctx.author.name}')

@client.event
async def on_member_join(member):
    bemvindo = client.get_channel(908896921052135484)
    mensagem = await bemvindo.send(f"Bem vindo {member.mention}!")

    await asyncio.sleep(20)
    await mensagem.delete()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')




client.run('OTYxMDY0MjMxODMzMzM3ODg2.Ykzi0A.DAPCmk_b7QXGp8YOC66b-kCBt7g')






