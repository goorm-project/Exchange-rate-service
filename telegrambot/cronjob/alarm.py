import datetime
import psycopg2
import telegram
import update_db


conn = psycopg2.connect(
    host="",
    database="",
    user="",
    password="",
    port=""
)


def alert():
    now = datetime.datetime.now().replace(microsecond=0)
    today_time = str(now)

    if now.hour >= 23 or now.hour <= 6:
        return

    message = '환율 정보가 갱신되었습니다❕' + "\n" + "\n" \
              + "일시: " + today_time + "\n" + "\n" \
              + "◾ 도움말 제공 👉 '/help'(클릭)" + "\n" \
              + "◾ 원터치 환율 확인 👉 '/touch'(클릭)" + "\n" \
              + "◾ 환율 확인 가능 국가 👉 '/nation'(클릭)"

    my_token = "2062972523:AAESW7NCkamXMNfDCmwx3pNfZSo73_3D7MY"
    bot = telegram.Bot(token=my_token)

    cur = conn.cursor()
    cur.execute("SELECT id FROM public.user")
    uid_list = cur.fetchall()

    for i in range(0, len(uid_list)):
        bot.send_message(chat_id=uid_list[i][0], text=message)


alert()
