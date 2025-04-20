import sys
from database_loader import load_database
from checker import find_matches
import discord
import pandas as pd
import numpy as np
import os
import json

def main(query_ids):   
    database = load_database("./data/database.json")
    return_msg = []
    for query_id in query_ids:
        mm = []
        matches = find_matches(database, query_id)
        if matches:
            for match in matches:
                mm.append(match)
        else:
            return_msg.append(["No matches found."])
        return_msg.append(mm)
    return return_msg


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!check'):
        cont = message.content.split()[1:]
        # split content and handle each id to check separately
        return_msg = main(cont)[0]
        buffer_res = []
        for msg in return_msg:
            tmsg = "".join(msg)
            buffer_res.append(tmsg)
        out = "\n".join(buffer_res)
        first_msg = "Searching ID: {}\n".format(cont[0])
        final_msg = first_msg + out

        # how handle multiple ids passed?

        # the string writing is incorrect as the discord bot types 
        #V-> A-> F
        #G-> r-> a-> n-> d->  -> F-> i-> n-> a-> l-> s
        #N-> o-> M-> o-> d-> 2
        await message.channel.send(final_msg)

with open('./token.txt') as f:
    botToken=f.readlines()

client.run(botToken[0])