import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, question: str):
        """Create a simple yes/no poll."""
        embed = discord.Embed(title="📊 Poll", description=question, color=discord.Color.blue())
        message = await ctx.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

def setup(bot):
    bot.add_cog(Poll(bot))
