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

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = context.args
    telegram_id = update.message.chat.id
    async with aiohttp.ClientSession() as session:
        data = {"telegram_id": telegram_id, "query": ''.join(query)}
        response = await session.post('http://127.0.0.1:8000/api/music/download/', json=data)
        if response.status == 200:
            from anyio import open_file
            async with await open_file('audio_file.mp3', 'wb') as file:
                content = await response.read()
                await file.write(content)
                await context.bot.send_audio(chat_id=telegram_id, audio='audio_file.mp3')

async def req_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/') as reponse:
            text = await reponse.text()
            await update.message.reply_text(text=text)


def main() -> None:
    application = Application.builder().token('7185505813:AAHgGv4-8iZWJewc9V6Sgi-JrwHbK8CcD-Q').build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('register', register_user))
    application.add_handler(CommandHandler('m', music))
    #application.add_handler(CommandHandler('download', youtube_download))


    application.run_polling(allowed_updates=Update.ALL_TYPES)




if __name__ == '__main__':
    print('Start bot . . .')
    main()
    print('Stopped bot . . .')

