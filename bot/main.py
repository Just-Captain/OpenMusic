# Token = 7185505813:AAH-weBAQahUgo1sLNbTl2zxpsyfyfV_7xo
import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, CallbackContext
import os
import aiohttp
import json

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Доброе пожаловать пользователь в сервис <b>OPEN MUSIC</b>', parse_mode='html')

async def register_user(update: Update, context: CallbackContext):
    if len(context.args) == 2:
            username, password = context.args
            telegram_id = update.message.chat.id
            async with aiohttp.ClientSession() as session:
                data = {"username": username, "password": password, "telegram_id": telegram_id}
                response = await session.post('http://127.0.0.1:8000/api/users/user/create/', json=data)
                if response.status == 200:
                    await update.message.reply_text(text=f'Вы успешно зарегистрировались в системе <b>OPEN MUSIC</b>\n Ваш login: {username}\nPassword: {password}', parse_mode='html')
                else:
                    await update.message.reply_text(text=f"Что то пошло не так . . .")
    else:   
        await update.message.reply_text('Не корректая форма для регистрации')


"""
def donwload_music(search): 
    s = Search(search) 
    if len(s.results) > 0: 
        print(s.results[0].video_id) 
        url = 'https://www.youtube.com/watch?v=' + s.results[0].video_id 
        yt = YouTube(url)
        output_path = 'media/' + 'stat'
        os.mkdir(output_path)
        video = yt.streams.filter(only_audio=True).first() 
        downloaded_file = video.download(output_path=output_path) 
        base, ext = os.path.splitext(downloaded_file) 
        new_file = base + '.mp3' 
        os.rename(downloaded_file, new_file)

"""
"""
async def youtube_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = await get_username(update.message.chat.id)
    await context.bot.send_audio(chat_id=254451024, audio='media/stat/Numb.mp3')
    #search_user = context.args
   # print(f'ЗАПРОС: {search_user}, ЮЗЕР:{username}')
"""

async def req_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/') as reponse:
            text = await reponse.text()
            await update.message.reply_text(text=text)


def main() -> None:
    application = Application.builder().token('7185505813:AAH-weBAQahUgo1sLNbTl2zxpsyfyfV_7xo').build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('register', register_user))
    #application.add_handler(CommandHandler('download', youtube_download))


    application.run_polling(allowed_updates=Update.ALL_TYPES)




if __name__ == '__main__':
    print('Start bot . . .')
    main()
    print('Stopped bot . . .')

