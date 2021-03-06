import time
import datetime

import db_readwrite
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler

my_token = '2062972523:AAESW7NCkamXMNfDCmwx3pNfZSo73_3D7MY'
updater = Updater(my_token, use_context=True)


def start(update, context):
    db_readwrite.user_list(update.message.chat)
    reply_text = "๐ก๐ก๋ด์ด ์ ์์ ๊นจ์ด๋ฉ๋๋ค๐ก๐ก" + "\n" + "\n" \
                 + "๐ฑ ํ์จ ์ ๋ณด๋ฅผ ์๊ณ  ์ถ์ผ์ ๊ฐ์?๐ฑ" + "\n" + "\n" \
                 + "โพ ๋ฐ๊ฐ์ต๋๋ค ๐ " + "\n" \
                 + "โพ ์ ์๊ฒ ์๋ฌด๋ง์ด๋ ํด๋ณด์ธ์ โผ" + "\n" \
                 + "โพ ๋๋ผ์ด ์ผ์ด ๋ฒ์ด์ง๋ต๋๋ค ๐"
    update.message.reply_text(reply_text)
    reply_text2 = "ํน์ ์ฌ๊ธฐ๋ฅผ ํด๋ฆญ ๐ '/help'"
    update.message.reply_text(reply_text2)


# ๋ช๋ น์ด help๊ฐ ๋ค์ด์ฌ ๋ ๋ถ๋ฆฌ์ด์ง๋ ํจ์
def help_command(update, context):
    reply_text = "<์คํ๊ฐ๋ฅํ ๋ช๋ น์ด>" + "\n" + "\n" \
                 + "โพ ๋์๋ง ์ ๊ณต ๐ '/help'(ํด๋ฆญ)" + "\n" \
                 + "โพ ์ํฐ์น ํ์จ ํ์ธ ๐ '/touch'(ํด๋ฆญ)" + "\n" \
                 + "โพ ํ์จ ํ์ธ ๊ฐ๋ฅ ๊ตญ๊ฐ ๐ '/nation'(ํด๋ฆญ)"
    update.message.reply_text(reply_text)  # ์คํ ๊ฐ๋ฅ ๋ช๋ น์ด ๋ชฉ๋ก ์ฌ์ฉ์์๊ฒ ์ ์ก.


# ๋ช๋ น์ด nation ๋ค์ด์ฌ ๋ ๋ถ๋ฆฌ์ด์ง๋ ํจ์
def nation_command(update, context):
    reply_text = "<ํ์ฌ ํ์จ ์กฐํ ๊ฐ๋ฅ ๊ตญ๊ฐ ๋ฐ ์ง์ญ>" + "\n" + "\n" \
                 + "1) ์๋์๋ฏธ๋ฆฌํธ" + "\n" \
                 + "2) ํธ์ฃผ" + "\n" \
                 + "3) ์บ๋๋ค" + "\n" \
                 + "4) ์ค๊ตญ" + "\n" \
                 + "5) ์ ๋ฝ" + "\n" \
                 + "6) ์๊ตญ" + "\n" \
                 + "7) ํ์ฝฉ" + "\n" \
                 + "8) ์ผ๋ณธ" + "\n" \
                 + "9) ํ๊ตญ" + "\n" \
                 + "10) ๋ฏธ๊ตญ" + "\n" + "\n" \
                 + "๋๋ผ ๋ฐ ์ง์ญ ์ด๋ฆ์ ์๋ ฅํด์ฃผ์ธ์!" + "\n" + "(์ซ์๋ ๊ฐ๋ฅํฉ๋๋ค)"
    update.message.reply_text(reply_text)
    reply_text2 = "๋ค์ ๋ช๋ น์ด ํญ๋ชฉ์ ๋ณด๊ณ ์ถ๋ค๋ฉด?" + "\n" + "๐ '/help'(ํด๋ฆญ)"
    update.message.reply_text(reply_text2)


# ๋ช๋ น์ด touch ๋ค์ด์ฌ ๋ ๋ถ๋ฆฌ์ด์ง๋ ํจ์ (ํคํจ๋)
def touch_command(update, context):
    touch_buttons = [
        [
            InlineKeyboardButton('1. ์๋์๋ฏธ๋ฆฌํธ', callback_data=1),
            InlineKeyboardButton('2. ํธ์ฃผ', callback_data=2)
        ],
        [
            InlineKeyboardButton('3. ์บ๋๋ค', callback_data=3),
            InlineKeyboardButton('4. ์ค๊ตญ', callback_data=4)
        ],
        [
            InlineKeyboardButton('5. ์ ๋ฝ', callback_data=5),
            InlineKeyboardButton('6. ์๊ตญ', callback_data=6)
        ],
        [
            InlineKeyboardButton('7. ํ์ฝฉ', callback_data=7),
            InlineKeyboardButton('8. ์ผ๋ณธ', callback_data=8)
        ],
        [
            InlineKeyboardButton('9. ํ๊ตญ', callback_data=9),
            InlineKeyboardButton('10. ๋ฏธ๊ตญ', callback_data=10)
        ],
        [
            InlineKeyboardButton('์ทจ์', callback_data=11)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(touch_buttons)

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text='๋๋ผ ๋ฐ ์ง์ญ์ ํฐ์นํด์ฃผ์ธ์',
        reply_markup=reply_markup
    )


# ํฐ์น ํคํจ๋ ์ฝ๋ฐฑ ์ฒ๋ฆฌ
def cb_button(update, context):
    query = update.callback_query
    data = query.data  # callback_data ์ ๋์ผํ ๊ฐ ์ถ๋ ฅ

    context.bot.send_chat_action(
        chat_id=update.effective_user.id,
        action=ChatAction.TYPING
    )
    if 1 <= int(data) <= 10:
        context.bot.edit_message_text(
            text='{}๋ฒ ์์์ด ์งํ์ค์๋๋ค...โณ'.format(data),
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        time.sleep(0.5)
        context.bot.edit_message_text(
            text='{}๋ฒ ์์ ์๋ฃ๐ก'.format(data),
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        get_message(update, context)

    elif data == '11':
        context.bot.edit_message_text(
            text='์์์ด ์ทจ์๋์์ต๋๋คโ' + "\n" + "\n"
                 + "โพ ๋์๋ง ์ ๊ณต ๐ '/help'(ํด๋ฆญ)" + "\n"
                 + "โพ ์ํฐ์น ํ์จ ํ์ธ ๐ '/touch'(ํด๋ฆญ)" + "\n"
                 + "โพ ํ์จ ํ์ธ ๊ฐ๋ฅ ๊ตญ๊ฐ ๐ '/nation'(ํด๋ฆญ)",
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )


# ๋ช๋ น์ด price๊ฐ ๋ค์ด์ฌ ๋ ๋ถ๋ฆฌ์ด์ง๋ ํจ์
def price_command(update, context):
    code = context.args[0]  # args[0]์ ์ฒซ๋ฒ์งธ ์ธ์, ๋ณต์๊ฐ ์ธ์๋ฅผ ์ฌ์ฉํ ๊ฒฝ์ฐ์๋ [1], [2] ์ด๋ฐ์์ผ๋ก ๊ตฌ๋ถ
    price = 11000  # ๋ณด๋ด์ค ํ์ฌ๊ฐ, xing api๋ก ๊ฐ์ ์ป๋๋ค.
    reply_text = 'ํ์ฌ๊ฐ : ' + code + ' ' + str(price)  # ๋๋ ค์ค full text, ์์์ ๋ง๋ ๋ค.
    update.message.reply_text(reply_text)  # ๋ง๋  text๋ฅผ caller์๊ฒ ๋๋ ค์ค๋ค.


# ์ผ๋ฐ ๋ฉ์ธ์ง๋ฅผ ์๋ ฅํ  ๋ ๋ถ๋ฆฌ์ด์ง๋ ํจ์
def get_message(update, context):
    if update.message is None:  # touch ๋ช๋ น์ด ์ฒ๋ฆฌ
        print(update.callback_query.data)
        received_message = update.callback_query.data
    else:  # ์ผ๋ฐ ๋ฉ์์ง ์ฒ๋ฆฌ
        print(update.message.text)  # ๋ฐ์ ๋ฉ์ธ์ง ์ฝ์ ์ถ๋ ฅ
        received_message = update.message.text

    today_time = str(datetime.datetime.now().replace(microsecond=0))

    aws_data = db_readwrite.now_data_list(received_message)
    added_res = "๊ธฐ์ค ๋ ์ง: " + str(aws_data[0][0]) + "\n" \
                + "๋งค๋งค ๊ธฐ์ค์จ: " + str(aws_data[0][4]) + "\n" \
                + "์ก๊ธ ๋ฐ์ผ์ค ๋: " + str(aws_data[0][1]) + "\n" \
                + "์ก๊ธ ๋ณด๋ด์ค ๋: " + str(aws_data[0][2]) + "\n" \
                + "-----------------------------" + "\n" \
                + today_time

    if received_message == '์๋์๋ฏธ๋ฆฌํธ' or received_message == "1":
        res = "<์๋์๋ฏธ๋ฆฌํธ ๋๋๋ฅด(AED) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:  # touch ๋ช๋ น์ด ์๋
            context.bot.send_message(chat_id=update.effective_chat.id, text=res+added_res)
        else:  # ์ผ๋ฐ ๋ฉ์์ง ์๋
            update.message.reply_text(res+added_res)

    elif received_message == 'ํธ์ฃผ' or received_message == "2":
        res = "<ํธ์ฃผ ๋ฌ๋ฌ(AUD) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '์บ๋๋ค' or received_message == "3":
        res = "<์บ๋๋ค ๋ฌ๋ฌ(CAD) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '์ค๊ตญ' or received_message == "4":
        res = "<์ค๊ตญ ์์(CNY) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '์ ๋ฝ' or received_message == "5":
        res = "<์ ๋ฝ ์ฐํฉ ์ ๋ก(EUR) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '์๊ตญ' or received_message == "6":
        res = "<์๊ตญ ํ์ด๋(GBP) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == 'ํ์ฝฉ' or received_message == "7":
        res = "<ํ์ฝฉ ๋ฌ๋ฌ(HKD) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '์ผ๋ณธ' or received_message == "8":
        res = "<์ผ๋ณธ 100์(JPY) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == 'ํ๊ตญ' or received_message == "9":
        res = "<ํ๊ตญ ์(KRW) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '๋ฏธ๊ตญ' or received_message == "10":
        res = "<๋ฏธ๊ตญ ๋ฌ๋ฌ(USD) ํ์จ ์ ๋ณด>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    else:
        res = '๋ณด๋ด์ฃผ์  ๋ฉ์ธ์ง: ' + update.message.text + "\n" \
              + "------------------------------" + "\n" \
              + "๋๋ผ ๋ฐ ์ง์ญ ์ด๋ฆ์ ์๋ ฅํด์ฃผ์ธ์!" + "\n" + "(์ซ์๋ ๊ฐ๋ฅํฉ๋๋ค)" + "\n" + "\n" \
              + "1) ์๋์๋ฏธ๋ฆฌํธ" + "\n" \
              + "2) ํธ์ฃผ" + "\n" \
              + "3) ์บ๋๋ค" + "\n" \
              + "4) ์ค๊ตญ" + "\n" \
              + "5) ์ ๋ฝ" + "\n" \
              + "6) ์๊ตญ" + "\n" \
              + "7) ํ์ฝฉ" + "\n" \
              + "8) ์ผ๋ณธ" + "\n" \
              + "9) ํ๊ตญ" + "\n" \
              + "10) ๋ฏธ๊ตญ"  # ์๋ ๋ฉ์์ง ์์ฑ
        update.message.reply_text(res)  # ์๋ ๋ฉ์์ง ์ ์ก

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="๋ค์ ๋ช๋ น์ด ํญ๋ชฉ์ ๋ณด๊ณ ์ถ๋ค๋ฉด?" + "\n" + "๐ '/help'(ํด๋ฆญ)"
    )


# ๋ฑ๋ก๋์ง ์์ /๋ช๋ น์ด ๋์
def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="์ฃ์กํด์. ์์ง ํด๋น ๋ช๋ น์ด๋ ์ค๋น๋์ง ์์์์ ๐ฅ" + "\n" + "\n"
             + "โพ ๋์๋ง ์ ๊ณต ๐ '/help'(ํด๋ฆญ)" + "\n"
             + "โพ ์ํฐ์น ํ์จ ํ์ธ ๐ '/touch'(ํด๋ฆญ)" + "\n"
             + "โพ ํ์จ ํ์ธ ๊ฐ๋ฅ ๊ตญ๊ฐ ๐ '/nation'(ํด๋ฆญ)"
    )


# /help ๋ช๋ น์ด๋ฅผ ์ํ handler ๋ฑ๋ก
updater.dispatcher.add_handler(CommandHandler('help', help_command))

# /start ๋ช๋ น์ด๋ฅผ ์ํ handler ๋ฑ๋ก
updater.dispatcher.add_handler(CommandHandler('start', start))

# /nation ๋ช๋ น์ด๋ฅผ ์ํ handler ๋ฑ๋ก
updater.dispatcher.add_handler(CommandHandler('nation', nation_command))

# /touch ๋ช๋ น์ด๋ฅผ ์ํ handler ๋ฑ๋ก
updater.dispatcher.add_handler(CommandHandler('touch', touch_command))
updater.dispatcher.add_handler(CallbackQueryHandler(cb_button))

# /prise ๋ช๋ น์ด๋ฅผ ์ํ handler ๋ฑ๋ก, ์ฝ๋๋ฅผ ์๋ ฅ์ ๋ฐ์์ผํ๋ฏ๋ก pass_args๋ฅผ True๋ก ์ค์ 
updater.dispatcher.add_handler(CommandHandler('prise', price_command, pass_args=True))

# ์ ์ ์๋ ๋ช๋ น์ด๊ฐ ์์ ๋ ๋์
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# ์ผ๋ฐ ๋ฉ์ธ์ง๋ฅผ ์ฒ๋ฆฌํ๊ธฐ ์ํ handler ๋ฑ๋ก (์ผ๋ฐ ๋ฉ์ธ์ง: / ์์ด ์๋ ฅํ๋ ๋ฌธ์์ด)
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), get_message))

# 3์ด๋ง๋ค ์ ๋ช๋ น์ด ์๋์ง ํ์ธํ๋๋ก ์ค์ 
updater.start_polling(timeout=10, clean=True)

# ์ ๋ช๋ น์ด๊ฐ ์ฌ๋๊น์ง waiting
print('bot start')
updater.idle()
