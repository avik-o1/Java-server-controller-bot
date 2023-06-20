#!/usr/bin/python
import time
import discord
import os

from mcstatus import JavaServer

from discord.ext import commands

server = JavaServer.lookup("your server's ip address or if you are hosting from own pc then '127.0.0.1:25565'")

try:
    status = server.status()
    print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
except:
    print("Server offline")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = ".", intents=intents)

@client.event
async def on_ready():
    print("Ready")
    
@client.command()
async def start(ctx):
    print("Starting server")
    try:
        status = server.status()
        print("```css\nThe server is already running")
        await ctx.send("```css\nThe server is already running\n```")
    except:
        await ctx.send('Starting minecraft server. Please wait a few seconds...')
        os.system("your server.bat's location")
        time.sleep(27)
        await ctx.send("```css\nServer started\n```")
        time.sleep(2)
        await ctx.send("Here is the IP address. It starts after the 'tcp://' part.")
        os.system("the additional webhook's location")
       
@client.command()
async def status(ctx):
    print("Server status requested.")
    try:
        status = server.status()
        print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
        await ctx.send("**Server status**\n```diff\n+ Players: {0} \n+ Latency: {1} ms```".format(status.players.online, status.latency))
    except:
        await ctx.send("**Server status**\n```diff\n- Server is offline\n```")
 
@client.command()
async def players(ctx):
    print("Server player list requested.")
    try:
        status = server.status()
        usersConnected = [ user['name'] for user in status.raw['players']['sample'] ]
        await ctx.send(usersConnected)
    except:
        await ctx.send("**Server status**\n```diff\n No players to show.\n```")

@client.command()
async def stop(ctx):
    print("Server shutdown requested.")
    try:
        status = server.status()
        if status.players.online !=0:
            await ctx.send("**Server shutdown requested:**\n```diff\n- Sorry. server can only be shutdown if no one is playing.\nPlayers: {0}```".format(status.players.online))
        else:
            await ctx.send("**Server shutdown requested:**\n```diff\n+ Server sucessfully shut down.```")
            os.system("taskkill /im java.exe")
    except:
        await ctx.send('```diff\n- Server is not running\n```')
        status = server.status()
 
@client.command()
async def ip(ctx):
    print("Server IP requested.")
    await ctx.send("Getting server IP. It starts after the 'tcp://' part.")
    os.system("the additional webhook's location")
    
@client.command()
async def server_help(ctx):
    print("Server help requested.")
    await ctx.send("```css\nJava Server Controller\n```\n```\n.server_help : Show this message.\n\n.start : Starts the minecraft server, playable after 25 to 30 seconds.\n\n.status : Shows player numbers & latency or whether the server is offline.\n\n.stop : Stops the server only when no one is playing.\n\n.ip : Shows the IP address of the server. \n\n.players : Show the players currently playing on the server. \n```")    
   

client.run('your bot's token')
