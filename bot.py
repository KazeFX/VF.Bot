import discord
import requests
import database_helper
from discord.ext import commands, tasks
from api_tokens import BOT_TOKEN, BOT_TRAP_CHANNEL_ID

intents = discord.Intents.default()
intents.members = True # Required to receive member join events
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("VF.Bot logged in!")


# Prints a welcome message to new members joining the sever; in a channel called welcome
@bot.event
async def on_member_join(member):
    channel_name = "väntrummet"  # replace with your channel name
    for ch in member.guild.text_channels:
        if ch.name == channel_name:
            await ch.send(f"Välkommen till Virtua Fighter SE, {member.mention} !")
            break


@bot.event
async def on_message(message):
    # Bot trap section
    if message.author.bot:
        return
    if message.channel.id == BOT_TRAP_CHANNEL_ID:
        try:
            await message.author.ban(reason="Posted in restricted channel, probably a bot.")
            await message.channel.send(f"{message.author} was probably a bot, banned!")
        except Exception as e:
            print(f"Failed to ban user: {e}")

    await bot.process_commands(message)


bot.run(BOT_TOKEN)