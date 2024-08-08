import logging
from aiogram import Bot, Dispatcher, executor, types
import requests




API_TOKEN = '6880048659:AAElCbun5bKBmiOfSkFGIozhABxUljo3OnU'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Hi!\nI'm Spotify!\nPowered by aiogram.
        /artist
        /albom
        /song
    """)


@dp.message_handler(commands=['song'])
async def send_welcome(message: types.Message):
    song = requests.get(f'http://127.0.0.1:8000/api/song/')
    for song in song.json():
        await message.reply(f"""
        Title:{song['title']}\n
        Artist:{song['albom']['artist']}\n
        Albom:{song['albom']}
        """)


@dp.message_handler(commands=['albom'])
async def send_welcome(message: types.Message):
    albom = requests.get(f'http://127.0.0.1:8000/api/album/')
    for albom in albom.json():
        await message.reply(f"""
        Title:{albom['title']}\n
        Artist:{albom['artist']}
        """)


@dp.message_handler(commands=['artist'])
async def send_welcome(message: types.Message):
    artist = requests.get(f'http://127.0.0.1:8000/api/artist/')
    for artist in artist.json():
        await message.reply(f"""
        Name:{artist['first_name']}\n
        Last_name:{artist['last_name']}
        """)


@dp.message_handler()
async def send_welcome(message: types.Message):
    search_data = message.text
    song = requests.get(f'http://127.0.0.1:8000/api/song?search={search_data}')
    if song.json():
        for song in song.json():
            await message.reply(f"""
            Albom:{song['album']['title']}\n
            Artist:
            First name:{song['albom']['artist']['first_name']}\n
            Last name:{song['albom']['artist']['last_name']}
            Title:{song['title'].title()}
            """)
    else:
        await message.reply("qoshiq mavjut emas")




@dp.message_handler()
async def echo(message: types.Message):


    await message.answer(message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)