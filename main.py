import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
DISCORD_TOKEN =
os.getenv("DISCORD_TOKEN")
bot =
commands.Bot(command_prefix="$")
@bot.event
async def on_message(message):
 if messsage.content ==
 "hello":
   await
message.channel.send("Mommy is better than loli. changed my mind.")
await
bot.process_commands(message)
@bot.command(
  help="Uses come crazy logic to determine if pong is actually the correct value or not.",
  brief="Prints pong back to the channel."
)
async def ping(ctx):
  await 
  ctx.channel.send("pong")
  @bot.command(
    help="Looks like you need some help.",

brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
await
 ctx.channel.send(response)
 bot.run(DISCORD_TOKEN)
 bot.run(DISCORD_TOKEN)