import discord
import asyncio

TOKEN = "PASTE_YOUR_TOKEN_HERE"
CHANNEL_ID = 123456789012345678  # no quotes
ROLE_ID = 123456789012345678     # no quotes

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    channel = client.get_channel(CHANNEL_ID)

    while True:
        if channel:
            await channel.send(
                f"🔼 <@&{ROLE_ID}> bump time, who’s up? type /bump",
                allowed_mentions=discord.AllowedMentions(roles=True)
            )
        await asyncio.sleep(7200)  # 2 hours


client.run(TOKEN)
