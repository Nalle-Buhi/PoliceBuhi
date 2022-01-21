import os
import discord
from discord.ext import commands
from creds import TOKEN
import bot_setup



bot = commands.Bot(command_prefix=["kb", "Kb"], case_insensitive=True)




@bot.event
async def on_ready():
    print(f"Logged in: {bot.user}")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Amogus hardbass"))



def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"loaded: {filename}")



if __name__ == "__main__":
    bot_setup.create_tables()
    load_cogs()
    bot.run(TOKEN)
