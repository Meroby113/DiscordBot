import random
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests


load_dotenv()
token = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready to go!')
    print('---------------------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!recommend'):
        category = message.content.split('recommend ')[1]
        movie = get_movie_by_category(category)
        print (movie)
        if movie is not None:
            await message.channel.send("You should watch " + movie)
        else:
            await message.channel.send('No movie found for this category')


TMDB_API_KEY = "0f30e15dbbfaebb3046bf90261fea537"
def get_movie_by_category(category):
    url = 'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={category}'
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZjMwZTE1ZGJiZmFlYmIzMDQ2YmY5MDI2MWZlYTUzNyIsIm5iZiI6MTcyMjQyMDU4Ny4xMTg0OTIsInN1YiI6IjY2YTlmODRmYmZjOWIyYTE4MmVlZmNhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BFy5y9qZh44wSKPV7olin2v0D7BbeWxn35GXX1zLvac"
}
    response = requests.get(url, headers=headers)
    data = response.json()
    size = len(data.get('results'))
    random_index = random.randint(0, size-1)
    # print(data, random_index)
    # print(data.get('results')[random_index].get('title'))
    # movie_title = data.get('results')[random_index].get('title')
    # movie_title = movie_title.split(':', 1)[1].strip()
    # print(movie_title)
    # if ":" in movie_title:
    #     return movie_title
    # else:
    #     return data.get('results')[random_index].get('title')
    return data.get('results')[random_index].get('title')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

@client.command()
async def sad(ctx):
    await ctx.send("SAD")

client.run(token)