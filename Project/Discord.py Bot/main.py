import discord


token = "MTAyOTQ5NTk5MzI4MjA4NDg3NA.GR2Hee.lekXLtemYo6-F3_QO60TFxO0K5qr3A_0yUG_NY"

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

client.run(token)