from discord.commands import slash_command
from discord.commands import SlashCommandGroup, CommandPermission
from discord.ext import commands
import tools.dbtools as dbtools
import discord.utils
from tools.embedtools import embed_builder


class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel_id = await dbtools.log_config_reader(message.guild.id, "del_log_config")
        if channel_id:
            channel = self.bot.get_channel(channel_id)
            if message.attachments:
                attachment = message.attachments[0] #<@{message.author.id}>:n viesti poistettiin kanavalla <#{message.channel.id}>"
                em = await embed_builder(message, "PAska vbotit", f"<@{message.author.id}>:n viesti poistettiin kanavalla <#{message.channel.id}>", fields = [[" :", attachment.url, False]], image=attachment.url)
                await channel.send(embed=em)
            
            if message.content:
                em = await embed_builder(message, "PAska vbotit", f"<@{message.author.id}>:n viesti poistettiin kanavalla <#{message.channel.id}>", fields = [["Sisältö:", message.content, False]])
                await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel_id = await dbtools.log_config_reader(before.guild.id, "edit_log_config")
        if channel_id:
            channel = self.bot.get_channel(channel_id)
            if before.attachments:
                attachment = before.attachments[0] #<@{message.author.id}>:n viesti poistettiin kanavalla <#{message.channel.id}>"
                em = await embed_builder(before, "PAska vbotit", f"<@{before.author.id}>:n viesti muokattiin kanavalla <#{before.channel.id}>", fields = [[" :", attachment.url, False]], image=attachment.url)
                await channel.send(embed=em)
            
            if before.content:
                em = await embed_builder(before, "PAska vbotit", f"<@{before.author.id}>:n viesti muokattiin kanavalla <#{before.channel.id}>", fields = [["Ennen:", before.content, False], ["Jälkeen:", after.content, False]])
                await channel.send(embed=em)
            
        

def setup(bot):
    bot.add_cog(Template(bot))