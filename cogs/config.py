from discord.commands import slash_command, Option
from discord.commands import SlashCommandGroup, CommandPermission
from discord.ext import commands
import tools.dbtools as dbtools
from tools.embedtools import embed_builder

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # config = SlashCommandGroup("config", "Config komennot, vain adminien käytettävissä")
    
    @slash_command()
    async def log_delete(self, ctx,
    enabled: Option(int, "Onko loggaus käytössä, 0 = ei, 1 = Kyllä"),
    channel_id: Option(str, "Kanava jonne poistetut viestit lähetetään")):
        """Käytetään login conffaamiseen poistettujen viestien osalta"""
        if ctx.author.guild_permissions.administrator:
            await dbtools.insert_log_db(ctx.guild.id, channel_id, enabled, table = "del_log_config")
            em = await embed_builder(ctx, "Päivitetty", "On", fields=[["Logi kanava:", channel_id, False], ["Logi päällä:", enabled, False]])
            await ctx.respond(embed=em)
        else:
            await ctx.respond("Sinulla ei ole tarvittavia oikeuksia")



    @slash_command()
    async def log_edit(self, ctx,
    enabled: Option(int, "Onko loggaus käytössä, 0 = ei, 1 = Kyllä"),
    channel_id: Option(str, "Kanava jonne muokatut viestit lähetetään")):
        """Käytetään login conffaamiseen muokattujen viestien osalta"""
        if ctx.author.guild_permissions.administrator:
            await dbtools.insert_log_db(ctx.guild.id, channel_id, enabled, table = "edit_log_config")
            em = await embed_builder(ctx, "Päivitetty", "On", fields=[["Logi kanava:", channel_id, False], ["Logi päällä:", enabled, False]])
            await ctx.respond(embed=em)
        else:
            await ctx.respond("Sinulla ei ole tarvittavia oikeuksia")



def setup(bot):
    bot.add_cog(Config(bot))