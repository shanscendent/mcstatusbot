from mcstatus import MinecraftServer
import discord
from discord.ext import commands
import configparser
import subprocess
import shlex
from random import randint
import time, os

# Initialize configuration
# Configuration contains server IP and discord bot token
config = configparser.ConfigParser()
config.read('mcbot.conf')
user = 'shan'

# Attach mcstatus to server IP
server = MinecraftServer.lookup(config[user]['IP'])

# Helper functions
def sanitize(arg):
    pass

# Initialize discord bot
bot = commands.Bot(command_prefix='~~')

@bot.command()
async def ping(ctx, arg):
    """Ping an IP FROM the server. Suggested usage: ~~ping tarun.ddns.net"""
    await ctx.send("Pinging server...")
    await ctx.trigger_typing()
    # Argument sanitization
    command = 'ping {} -c 4'.format(shlex.quote(arg))
    command = shlex.split(command)
    res = subprocess.check_output(command)
    line = res.splitlines()[-1]
    #await ctx.delete_message()
    await ctx.send(line.decode().split("/")[4] + "ms average to " + arg)

@bot.command(name='list')
async def _list(ctx):
    """Lists players currently online"""
    query = server.query()
    await ctx.send("The server has {0} players online: {1}".format(str(len(query.players.names)), ", ".join(query.players.names)))

@bot.command()
async def say(ctx, arg):
    """Broadcast message to players on the server. Suggested usage: ~~say ""text"""""
    # Requires rework with libtmux
    subprocess.run(["tmux", "send-keys", "-t", "minecraft.0", "/say " + arg, "ENTER"])
    #await ctx.delete_message()
    await ctx.send("Message broadcasted.")

# Not working
"""
@bot.command()
async def toggle(ctx, arg):
    """"""Relay server chat to discord. Suggested usage: ~~toggle on or off""""""

    if arg == "on":
        tog = True

    elif arg == "off":
        tog = False
    else:
        return

    def follow(thefile):
        thefile.seek(0,2)
        while True and tog:
            line = thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

    logfile = open("/home/shan/Minecraft/Enigmatica2Server-1.65a/logs/latest.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        if not tog:
            break
        if "[Client thread/INFO]: [CHAT]" in line:
            await ctx.send(line)
"""

@bot.command()
async def rps(ctx, arg1, arg2):
    """Rock paper scissors. Suggested usage: ~~rps <name1> <name2>"""
    t = ["Rock", "Paper", "Scissors"]

    p1 = t[randint(0,2)]
    p2 = t[randint(0,2)]

    trumped_by = {
        'Rock': ['Paper'],
        'Paper': ['Scissors'],
        'Scissors': ['Rock']
    }

    if p1 == p2:
        out = "{1} plays {0}. {2} plays {0}. Tie!".format(p1, arg1, arg2)
    else:
        if p2 in trumped_by[p1]:
            out = "{2} plays {0}. {3} plays {1}. {3} wins!".format(p1, p2, arg1, arg2)
        else:
            out = "{2} plays {0}. {3} plays {1}. {2} wins!".format(p1, p2, arg1, arg2)

    await ctx.send(out)

bot.run(config[user]['Token'])