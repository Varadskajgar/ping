import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx, seconds: int):
    if seconds > 30:
        await ctx.send("❌ Please enter 30 seconds or less to avoid spam.")
        return

    for i in range(1, seconds + 1):
        await ctx.send(f'Pong! ({i})')
        await asyncio.sleep(1)

# Start the web server to keep the bot alive
keep_alive()

# Run the bot
bot.run(TOKEN)
