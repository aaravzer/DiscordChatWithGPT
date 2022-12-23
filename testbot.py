import openai
import discord
import asyncio

openai.api_key = "YOUR_API_KEY"

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!gpt3"):
        prompt = message.content[6:]

        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completions.choices[0].text
        await message.channel.send(response)

client.run("TOKEN")
