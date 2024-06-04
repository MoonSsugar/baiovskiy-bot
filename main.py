import uuid
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import (InlineQuery, FSInputFile,
                           InputTextMessageContent,
                           InlineQueryResultCachedVoice)
from aiogram.exceptions import TelegramBadRequest

from config import settings

dp = Dispatcher()
bot = Bot(token=settings.bot_token)
VOICE_MAP = {"Поле навчись дивиться": "",
             "Тарас той блять": "",
             "Жоско грає": "",
             "А фола то нема": "",
             "А фола то нема v2(хуйня)": "",
             "Покажи...": ""}

FILES_MAP = {"Жоско грає": "contractova.ogg",
             "Поле навчись дивиться": "rozvod.ogg",
             "Тарас той блять": "taras.ogg",
             "А фола то нема": "fol.ogg",
             "А фола то нема v2(хуйня)": "fol2.ogg",
             "Покажи...": "show.ogg"}


stadium = InputTextMessageContent(message_text="123")


@dp.inline_query()
async def inline_query_handler(inline_query: InlineQuery):
    while True:
        results = []
        for i in VOICE_MAP:
            file_id = VOICE_MAP.get(i)
            results.append(InlineQueryResultCachedVoice(
                title=i,
                id=str(uuid.uuid4()),
                voice_file_id=file_id,
            ))
        try:
            await inline_query.answer(results=results,
                                      is_personal=False,
                                      cache_time=1)
            return
        except TelegramBadRequest as e:
            print(e)
            for file in FILES_MAP:
                file_path = FILES_MAP.get(file)
                msg = await bot.send_voice(chat_id=5198857407,
                                           voice=FSInputFile(file_path))
                VOICE_MAP[file] = msg.voice.file_id

if __name__ == "__main__":
    logging.basicConfig(filemode='a', level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
