import os
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # needed for role management

bot = commands.Bot(command_prefix='?', intents=intents)

# Load all cogs
initial_extensions = [
    'tournament',
    'role_manager',
    'poll',
    'dm_manager'
]

if __name__ == '__main__':
    for ext in initial_extensions:
        bot.load_extension(ext)

@bot.event
async def on_ready():
    print(f'✅ Bot is ready! Logged in as {bot.user}.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("❌ Command not found. Use `?help` to see available commands.")
    else:
        raise error

# Custom help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())
    embed.add_field(name="?help", value="Show this help message", inline=False)
    embed.add_field(name="?announce <message>", value="Announce tournament info", inline=False)
    embed.add_field(name="?joiners", value="List users joined the tournament", inline=False)
    embed.add_field(name="?clearjoiners", value="Clear joiners list", inline=False)
    embed.add_field(name="?join", value="Join the current tournament", inline=False)
    embed.add_field(name="?role @user <role>", value="Assign role to user", inline=False)
    embed.add_field(name="?poll <question>", value="Create a poll", inline=False)
    embed.add_field(name="?dm <user/all> <message>", value="Send DM to user or all", inline=False)
    await ctx.send(embed=embed)

# Run bot
bot.run(os.getenv('DISCORD_TOKEN'))
