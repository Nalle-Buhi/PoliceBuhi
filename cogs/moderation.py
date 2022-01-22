from discord.commands import slash_command, Option
from discord.commands import SlashCommandGroup, CommandPermission
from discord.ext import commands
import discord
from datetime import timedelta
from tools.embedtools import embed_builder



class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command()
    async def timeout(self, ctx, member: Option(discord.Member, "Mutetettava käyttäjä", required=True),
                    minutes: Option(int, "Miten pitkään käyttäjä on mutetettu minuuteissa", required=True),
                    days: Option(int, "Miten pitkään käyttäjä on mutetettu päivissä (ei pakollinen)", required=False, default=0),
                    reason: Option(str, "Syy miksi käyttäjä sai mutet", required=False)):
        if ctx.author.guild_permissions.moderate_members:
            await member.timeout_for(duration = timedelta(days=days, minutes=minutes), reason=reason)
            em = await embed_builder(ctx, "Mutetettu", f"{member} on mutetettu ajaksi {timedelta(days=days, minutes=minutes)}", image="https://i.kym-cdn.com/photos/images/newsfeed/002/012/359/610.jpg")
            await ctx.respond(embed=em)
        else:
            await ctx.respond("Sinulla ei ole oikeuksia tehdä tätä")

    @slash_command()
    async def remove_timeout(self, ctx, member: Option(discord.Member, "Käyttäjä jolta mute otetaan pois", required=True),
                            reason: Option(str, "Miksi mute otetaan pois", required=False, default="Mute poistettu botilla")):
        if ctx.author.guild_permissions.moderate_members:
            if member.timed_out:
                await member.remove_timeout(reason=reason)
                em = await embed_builder(ctx, "Mute otettu pois", f"{member}:n mute otettu pois.", image="https://i.kym-cdn.com/photos/images/newsfeed/001/370/061/095.jpg")
                await ctx.respond(embed=em)
            else:
                await ctx.respond("Kyseisellä käyttäjällä ei ole mutea :DD")
        else:
            await ctx.respond("Sinulla ei ole oikeksia tehdä tätä")


def setup(bot):
    bot.add_cog(Moderation(bot))