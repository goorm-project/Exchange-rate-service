import time
import datetime

import db_readwrite
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler

my_token = '2062972523:AAESW7NCkamXMNfDCmwx3pNfZSo73_3D7MY'
updater = Updater(my_token, use_context=True)


def start(update, context):
    db_readwrite.user_list(update.message.chat)
    reply_text = "💡💡봇이 잠에서 깨어납니다💡💡" + "\n" + "\n" \
                 + "💱 환율 정보를 알고 싶으신가요?💱" + "\n" + "\n" \
                 + "◾ 반갑습니다 🙌 " + "\n" \
                 + "◾ 저에게 아무말이나 해보세요 ‼" + "\n" \
                 + "◾ 놀라운 일이 벌어진답니다 😎"
    update.message.reply_text(reply_text)
    reply_text2 = "혹은 여기를 클릭 👉 '/help'"
    update.message.reply_text(reply_text2)


# 명령어 help가 들어올 때 불리어지는 함수
def help_command(update, context):
    reply_text = "<실행가능한 명령어>" + "\n" + "\n" \
                 + "◾ 도움말 제공 👉 '/help'(클릭)" + "\n" \
                 + "◾ 원터치 환율 확인 👉 '/touch'(클릭)" + "\n" \
                 + "◾ 환율 확인 가능 국가 👉 '/nation'(클릭)"
    update.message.reply_text(reply_text)  # 실행 가능 명령어 목록 사용자에게 전송.


# 명령어 nation 들어올 때 불리어지는 함수
def nation_command(update, context):
    reply_text = "<현재 환율 조회 가능 국가 및 지역>" + "\n" + "\n" \
                 + "1) 아랍에미리트" + "\n" \
                 + "2) 호주" + "\n" \
                 + "3) 캐나다" + "\n" \
                 + "4) 중국" + "\n" \
                 + "5) 유럽" + "\n" \
                 + "6) 영국" + "\n" \
                 + "7) 홍콩" + "\n" \
                 + "8) 일본" + "\n" \
                 + "9) 한국" + "\n" \
                 + "10) 미국" + "\n" + "\n" \
                 + "나라 및 지역 이름을 입력해주세요!" + "\n" + "(숫자도 가능합니다)"
    update.message.reply_text(reply_text)
    reply_text2 = "다시 명령어 항목을 보고싶다면?" + "\n" + "👉 '/help'(클릭)"
    update.message.reply_text(reply_text2)


# 명령어 touch 들어올 때 불리어지는 함수 (키패드)
def touch_command(update, context):
    touch_buttons = [
        [
            InlineKeyboardButton('1. 아랍에미리트', callback_data=1),
            InlineKeyboardButton('2. 호주', callback_data=2)
        ],
        [
            InlineKeyboardButton('3. 캐나다', callback_data=3),
            InlineKeyboardButton('4. 중국', callback_data=4)
        ],
        [
            InlineKeyboardButton('5. 유럽', callback_data=5),
            InlineKeyboardButton('6. 영국', callback_data=6)
        ],
        [
            InlineKeyboardButton('7. 홍콩', callback_data=7),
            InlineKeyboardButton('8. 일본', callback_data=8)
        ],
        [
            InlineKeyboardButton('9. 한국', callback_data=9),
            InlineKeyboardButton('10. 미국', callback_data=10)
        ],
        [
            InlineKeyboardButton('취소', callback_data=11)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(touch_buttons)

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text='나라 및 지역을 터치해주세요',
        reply_markup=reply_markup
    )


# 터치 키패드 콜백 처리
def cb_button(update, context):
    query = update.callback_query
    data = query.data  # callback_data 와 동일한 값 출력

    context.bot.send_chat_action(
        chat_id=update.effective_user.id,
        action=ChatAction.TYPING
    )
    if 1 <= int(data) <= 10:
        context.bot.edit_message_text(
            text='{}번 작업이 진행중입니다...⏳'.format(data),
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        time.sleep(0.5)
        context.bot.edit_message_text(
            text='{}번 작업 완료💡'.format(data),
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        get_message(update, context)

    elif data == '11':
        context.bot.edit_message_text(
            text='작업이 취소되었습니다❕' + "\n" + "\n"
                 + "◾ 도움말 제공 👉 '/help'(클릭)" + "\n"
                 + "◾ 원터치 환율 확인 👉 '/touch'(클릭)" + "\n"
                 + "◾ 환율 확인 가능 국가 👉 '/nation'(클릭)",
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )


# 명령어 price가 들어올 때 불리어지는 함수
def price_command(update, context):
    code = context.args[0]  # args[0]에 첫번째 인자, 복수개 인자를 사용한 경우에는 [1], [2] 이런식으로 구분
    price = 11000  # 보내줄 현재가, xing api로 값을 얻는다.
    reply_text = '현재가 : ' + code + ' ' + str(price)  # 돌려줄 full text, 알아서 만든다.
    update.message.reply_text(reply_text)  # 만든 text를 caller에게 돌려준다.


# 일반 메세지를 입력할 때 불리어지는 함수
def get_message(update, context):
    if update.message is None:  # touch 명령어 처리
        print(update.callback_query.data)
        received_message = update.callback_query.data
    else:  # 일반 메시지 처리
        print(update.message.text)  # 받은 메세지 콘솔 출력
        received_message = update.message.text

    today_time = str(datetime.datetime.now().replace(microsecond=0))

    aws_data = db_readwrite.now_data_list(received_message)
    added_res = "기준 날짜: " + str(aws_data[0][0]) + "\n" \
                + "매매 기준율: " + str(aws_data[0][4]) + "\n" \
                + "송금 받으실 때: " + str(aws_data[0][1]) + "\n" \
                + "송금 보내실 때: " + str(aws_data[0][2]) + "\n" \
                + "-----------------------------" + "\n" \
                + today_time

    if received_message == '아랍에미리트' or received_message == "1":
        res = "<아랍에미리트 디나르(AED) 환율 정보>" + "\n" + "\n"
        if update.message is None:  # touch 명령어 응대
            context.bot.send_message(chat_id=update.effective_chat.id, text=res+added_res)
        else:  # 일반 메시지 응대
            update.message.reply_text(res+added_res)

    elif received_message == '호주' or received_message == "2":
        res = "<호주 달러(AUD) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '캐나다' or received_message == "3":
        res = "<캐나다 달러(CAD) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '중국' or received_message == "4":
        res = "<중국 위안(CNY) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '유럽' or received_message == "5":
        res = "<유럽 연합 유로(EUR) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '영국' or received_message == "6":
        res = "<영국 파운드(GBP) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '홍콩' or received_message == "7":
        res = "<홍콩 달러(HKD) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '일본' or received_message == "8":
        res = "<일본 100엔(JPY) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '한국' or received_message == "9":
        res = "<한국 원(KRW) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    elif received_message == '미국' or received_message == "10":
        res = "<미국 달러(USD) 환율 정보>" + "\n" + "\n"
        if update.message is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=res + added_res)
        else:
            update.message.reply_text(res + added_res)

    else:
        res = '보내주신 메세지: ' + update.message.text + "\n" \
              + "------------------------------" + "\n" \
              + "나라 및 지역 이름을 입력해주세요!" + "\n" + "(숫자도 가능합니다)" + "\n" + "\n" \
              + "1) 아랍에미리트" + "\n" \
              + "2) 호주" + "\n" \
              + "3) 캐나다" + "\n" \
              + "4) 중국" + "\n" \
              + "5) 유럽" + "\n" \
              + "6) 영국" + "\n" \
              + "7) 홍콩" + "\n" \
              + "8) 일본" + "\n" \
              + "9) 한국" + "\n" \
              + "10) 미국"  # 응대 메시지 생성
        update.message.reply_text(res)  # 응대 메시지 전송

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="다시 명령어 항목을 보고싶다면?" + "\n" + "👉 '/help'(클릭)"
    )


# 등록되지 않은 /명령어 대응
def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="죄송합니다. 아직 그 명령어는 준비되지 않았아요 😥" + "\n" + "\n"
             + "◾ 도움말 제공 👉 '/help'(클릭)" + "\n"
             + "◾ 원터치 환율 확인 👉 '/touch'(클릭)" + "\n"
             + "◾ 환율 확인 가능 국가 👉 '/nation'(클릭)"
    )


# /help 명령어를 위한 handler 등록
updater.dispatcher.add_handler(CommandHandler('help', help_command))

# /start 명령어를 위한 handler 등록
updater.dispatcher.add_handler(CommandHandler('start', start))

# /nation 명령어를 위한 handler 등록
updater.dispatcher.add_handler(CommandHandler('nation', nation_command))

# /touch 명령어를 위한 handler 등록
updater.dispatcher.add_handler(CommandHandler('touch', touch_command))
updater.dispatcher.add_handler(CallbackQueryHandler(cb_button))

# /prise 명령어를 위한 handler 등록, 코드를 입력을 받아야하므로 pass_args를 True로 설정
updater.dispatcher.add_handler(CommandHandler('prise', price_command, pass_args=True))

# 알 수 없는 명령어가 왔을 때 대응
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# 일반 메세지를 처리하기 위한 handler 등록 (일반 메세지: / 없이 입력하는 문자열)
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), get_message))

# 3초마다 새 명령어 왔는지 확인하도록 설정
updater.start_polling(timeout=10, clean=True)

# 새 명령어가 올때까지 waiting
print('bot start')
updater.idle()
