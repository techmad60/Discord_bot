import discord;
from discord.ext import commands

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

# Event to print a message when the bot is ready
@bot.event
async def on_ready():
    print('Bot is ready!')

# Command to greet the user
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot
bot.run('YOUR_TOKEN_HERE')
