from discord.commands import slash_command, Option
from discord.commands import SlashCommandGroup, CommandPermission
from discord.ext import commands
import tools.dbtools as dbtools
from datetime import datetime
import discord
from tools.embedtools import embed_builder



class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def warn(self, ctx, member: Option(discord.Member, "Mutetettava käyttäjä", required=True),
    reason: Option(str, "Miksi kyseistä käyttäjää varoitetaan")):
        if ctx.author.guild_permissions.manage_roles: # i should prob change this to something other
            await dbtools.insert_warn(ctx.guild.id, member.id, ctx.author.id, reason, datetime.today().strftime('%d/%m/%Y'))
            await member.send(f"Hei! olet saanut varoituksen serverillä {ctx.guild} syyllä:\n`{reason}`. \nKäyttäydy kunnolla")
            await ctx.respond("Varitus annettu")
        else:
            await ctx.respond("Sinulla ei ole oikeksia")
            
    @slash_command()
    async def warns(self, ctx, member: Option(discord.Member, "Käyttäjä jonka kaikki varoitukset listataan", required=True)):
        if ctx.author.guild_permissions.manage_roles:
            user_warns = await dbtools.list_warns(ctx.guild_id, member.id)
            fields = []
            for i in user_warns:
                warn_giver = await self.bot.fetch_user(i[3])
                fields.append([f"id: {i[0]}", f"{i[4]} \n -{warn_giver.name} - {i[5]}", False])

            em = await embed_builder(ctx, " ", f"Varoitukset käyttäjälle <@{member.id}>", fields=fields)
            await ctx.respond(embed=em)




def setup(bot):
    bot.add_cog(Warn(bot))