import psycopg2
from datetime import datetime

today_date = datetime.today().strftime("%Y-%m-%d")  # WHERE 문에서 현재 시각 조건 입력위함

conn = psycopg2.connect(
    host="database-1.ck9mt4aiy0zp.ap-northeast-2.rds.amazonaws.com",
    database="test",
    user="goorm",
    password="test123qwe",
    port="5432"
)

cur_check = conn.cursor()
cur_check.excute("SELECT ")


def now_data_list(nation):
    cur = conn.cursor()

    if nation == "아랍에미리트" or nation == "1":
        cur.execute("SELECT * FROM aed WHERE date=CURRENT_DATE")
        result_list_1 = cur.fetchall()
        return result_list_1

    elif nation == "호주" or nation == "2":
        cur.execute("SELECT * FROM aud WHERE date=CURRENT_DATE")
        result_list_2 = cur.fetchall()
        return result_list_2

    elif nation == "캐나다" or nation == "3":
        cur.execute("SELECT * FROM cad WHERE date=CURRENT_DATE")
        result_list_3 = cur.fetchall()
        return result_list_3

    elif nation == "중국" or nation == "4":
        cur.execute("SELECT * FROM cnh WHERE date=CURRENT_DATE")
        result_list_4 = cur.fetchall()
        return result_list_4

    elif nation == "유럽" or nation == "5":
        cur.execute("SELECT * FROM eur WHERE date=CURRENT_DATE")
        result_list_5 = cur.fetchall()
        return result_list_5

    elif nation == "영국" or nation == "6":
        cur.execute("SELECT * FROM gbp WHERE date=CURRENT_DATE")
        result_list_6 = cur.fetchall()
        return result_list_6

    elif nation == "홍콩" or nation == "7":
        cur.execute("SELECT * FROM hkd WHERE date=CURRENT_DATE")
        result_list_7 = cur.fetchall()
        return result_list_7

    elif nation == "일본" or nation == "8":
        cur.execute("SELECT * FROM jpy_100 WHERE date=CURRENT_DATE")
        result_list_8 = cur.fetchall()
        return result_list_8

    elif nation == "한국" or nation == "9":
        cur.execute("SELECT * FROM krw WHERE date=CURRENT_DATE")
        result_list_9 = cur.fetchall()
        return result_list_9

    elif nation == "미국" or nation == "10":
        cur.execute("SELECT * FROM usd WHERE date=CURRENT_DATE")
        result_list_10 = cur.fetchall()
        return result_list_10

    else:
        cur.execute("SELECT * FROM krw WHERE date=CURRENT_DATE")
        result_list_9 = cur.fetchall()
        return result_list_9


'''
cur1 = conn.cursor()
cur1.execute("SELECT * FROM aed WHERE date=CURRENT_DATE")
result_list = cur1.fetchall()

for r in result_list:
    print(r)
'''
