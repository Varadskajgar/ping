import discord
from discord.ext import commands

class DMManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def dm(self, ctx, target: str, *, message: str):
        """Send DM to a user by mention or 'all' for all server members."""
        if target.lower() == "all":
            failed = []
            for member in ctx.guild.members:
                if member.bot:
                    continue
                try:
                    await member.send(message)
                except:
                    failed.append(member.name)
            if failed:
                await ctx.send(f"Failed to DM: {', '.join(failed)}")
            else:
                await ctx.send("✅ Message sent to all members.")
        else:
            user = None
            if ctx.message.mentions:
                user = ctx.message.mentions[0]
            if not user:
                await ctx.send("❌ Please mention a user to DM.")
                return
            try:
                await user.send(message)
                await ctx.send(f"✅ Message sent to {user.name}.")
            except:
                await ctx.send(f"❌ Failed to DM {user.name}.")

def setup(bot):
    bot.add_cog(DMManager(bot))
