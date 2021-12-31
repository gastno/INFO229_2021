# bot.py
import os
import random
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from discord_components import *
from discord.ext import commands
from dotenv import load_dotenv

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("LootBot")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
DiscordComponents(bot)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='BL', help='Responds with all the availables BIS Lists')
async def loot_bot(ctx):
    hoja=sheet.sheet1
    hoja.update_cell(1,1,"=sheetnames()")
    time.sleep(3)
    bis_lists = []
    i=2
    while (hoja.cell(i,1).value!='Pendientes'):
        bis_lists.append(hoja.cell(i,1).value)
        i=i+1

    msgBL = "```\n Selecciona la lista BIS que quieres ver: \n"

    opciones=[]
    for j in range(len(bis_lists)):
        msgBL = msgBL+str(j+1)+". "+bis_lists[j]+"\n"
        opciones.append(SelectOption(label=bis_lists[j],value=bis_lists[j]))
    msgBL = msgBL + "\n```"
    
    await ctx.reply(msgBL, components=[
        Select(placeholder='Selecciona una lista',options=opciones,custom_id='SelectBIS')
    ])
    interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'SelectBIS' and inter.user == ctx.author)
    itemPos = sheet.worksheet(interaction.values[0]).col_values(1)
    item = sheet.worksheet(interaction.values[0]).col_values(4)

    msgBIS = "```\nBIS "+interaction.values[0]+": \n"

    for x in range(1, 17):
        msgBIS=msgBIS+itemPos[x]+": "+item[x]+"\n"
    msgBIS=msgBIS + "\n```"
    await interaction.send(msgBIS)

bot.run(TOKEN)