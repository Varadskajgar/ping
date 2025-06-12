import discord
from discord.ext import commands

ROLE_MAP = {
    "admin": 123456789012345678,    # Replace with your actual role IDs
    "member": 234567890123456789,
    "player": 345678901234567890
}

class RoleManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, role_key: str):
        """Assign a role to a member by role key."""
        role_id = ROLE_MAP.get(role_key.lower())
        if not role_id:
            await ctx.send("❌ Role key not found.")
            return

        role = ctx.guild.get_role(role_id)
        if not role:
            await ctx.send("❌ Role not found on this server.")
            return

        await member.add_roles(role)
        await ctx.send(f"✅ {member.mention} has been given the role **{role.name}**.")

def setup(bot):
    bot.add_cog(RoleManager(bot))
