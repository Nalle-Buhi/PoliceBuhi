from discord.commands import slash_command, Option
from discord.commands import SlashCommandGroup, CommandPermission
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    test = SlashCommandGroup("test", "Testi komennot")


    @test.command()
    async def ping(self, ctx):
        await ctx.respond("Pongia vaa")

    @test.command()
    async def admin_ping(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            await ctx.respond("Eipä ollu admin roolia:DDD")
        else:
            await ctx.respond("Pongia vaa admini")


def setup(bot):
    bot.add_cog(Misc(bot))