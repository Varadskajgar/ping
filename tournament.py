import discord
from discord.ext import commands

class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joiners = set()

    @commands.command()
    async def announce(self, ctx, *, message: str):
        """Announce a tournament message with join info."""
        embed = discord.Embed(title="🏆 Tournament Announcement", description=message, color=discord.Color.gold())
        embed.set_footer(text="Type ?join to participate!")
        await ctx.send(embed=embed)

    @commands.command()
    async def join(self, ctx):
        """Join the tournament."""
        user = ctx.author
        if user.id in self.joiners:
            await ctx.send(f"{user.mention}, you have already joined the tournament.")
        else:
            self.joiners.add(user.id)
            await ctx.send(f"{user.mention} joined the tournament!")

    @commands.command()
    async def joiners(self, ctx):
        """List all joiners."""
        if not self.joiners:
            await ctx.send("No one has joined the tournament yet.")
            return
        mentions = [f"<@{uid}>" for uid in self.joiners]
        await ctx.send("Tournament Joiners:\n" + "\n".join(mentions))

    @commands.command()
    async def clearjoiners(self, ctx):
        """Clear the joiners list."""
        self.joiners.clear()
        await ctx.send("Tournament joiners list has been cleared.")

    @commands.command()
    async def dmjoiners(self, ctx, *, message: str):
        """Send DM message to all joiners."""
        failed = []
        for uid in self.joiners:
            user = self.bot.get_user(uid)
            if user:
                try:
                    await user.send(message)
                except:
                    failed.append(user.name)
        if failed:
            await ctx.send(f"Failed to DM: {', '.join(failed)}")
        else:
            await ctx.send("✅ Message sent to all joiners.")

def setup(bot):
    bot.add_cog(Tournament(bot))
