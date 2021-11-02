import datetime
import db_readwrite
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

my_token = '2062972523:AAESW7NCkamXMNfDCmwx3pNfZSo73_3D7MY'
updater = Updater(my_token, use_context=True)


def start(self):
    self.sendMessage('치이 봇이 잠에서 깨어납니다.')
    self.updater.start_polling()
    self.updater.idle()


# 명령어 help가 들어올 때 불리어지는 함수
def help_command(update, context):
    reply_text = "실행가능한 명령어" + "\n" \
                 + "/help: 도움말 제공" + "\n" \
                 + "/price: 가격 출력" + "\n" \
                 + "/nation: 환율 확인 가능 국가"
    update.message.reply_text(reply_text)
    reply_text = "실행가능한 명령어" + "\n" + "/sise : 현재가를 알려줌"  # 실행 가능 명령어 설명.
    update.message.reply_text(reply_text)  # 실행 가능 명령어 목록 사용자에게 전송.


# 명령어 sise가 들어올 때 불리어지는 함수
def sise_command(update, context):
    code = context.args[0]  # args[0]에 첫번째 인자, 복수개 인자를 사용한 경우에는 [1], [2] 이런식으로 구분
    price = 11000  # 보내줄 현재가, xing api로 값을 얻는다.
    reply_text = '현재가 : ' + code + ' ' + str(price)  # 돌려줄 full text, 알아서 만든다.
    update.message.reply_text(reply_text)  # 만든 text를 caller에게 돌려준다.


# 일반 메세지를 입력할 때 불리어지는 함수
def get_message(update, context):
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
        res = "<아랍에미리트 디나르(AED) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '호주' or received_message == "2":
        res = "<호주 달러(AUD) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '캐나다' or received_message == "3":
        res = "<캐나다 달러(CAD) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '중국' or received_message == "4":
        res = "<중국 위안(CNY) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '유럽' or received_message == "5":
        res = "<유럽 연합 유로(EUR) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '영국' or received_message == "6":
        res = "<영국 파운드(GBP) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '홍콩' or received_message == "7":
        res = "<홍콩 달러(HKD) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '일본' or received_message == "8":
        res = "<일본 100엔(JPY) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '한국' or received_message == "9":
        res = "<한국 원(KRW) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

    elif received_message == '미국' or received_message == "10":
        res = "<미국 달러(USD) 환율 정보>" + "\n"
        update.message.reply_text(res+added_res)  # 응대 메시지 전송

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


# 등록되지 않은 명령어 대응
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


# /help 명령어를 위한 handler 등록
updater.dispatcher.add_handler(CommandHandler('help', help_command))

# /sise 명령어를 위한 handler 등록
# /sise 명령어는 코드를 입력을 받아야하므로, pass_args를 Ture로 설정
updater.dispatcher.add_handler(CommandHandler('sise', sise_command, pass_args=True))

# 알 수 없는 명령어가 왔을 때 대응
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# 일반 메세지를 처리하기 위한 handler 등록
#   일반 메세지는 / 없이 입력하는 문자열
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), get_message))

# 3초마다 새 명령어 왔는지 확인하도록 설정
updater.start_polling(timeout=10, clean=True)

# 새 명령어가 올때까지 waiting
print('bot start')
updater.idle()
