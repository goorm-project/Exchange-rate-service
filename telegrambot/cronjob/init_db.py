import sys

import requests
from urllib.parse import urlparse
import pandas as pd
from pandas import json_normalize
import psycopg2

AUTHKEY = 'tGie8HCpUdR4N2nMnRK38O5bouWatQHX'

# psycopg2
# API 테스트
# url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey='+AUTHKEY+'&searchdate=20211025&data=AP01'
# response = requests.get(urlparse(url).geturl())
# result = response.json()
# json_normalize(result)


# 10월 데이터 입력

october = pd.DataFrame(
    columns=['date', 'ttb', 'tts', 'deal_bas_r', 'bkpr', 'yy_efee_r', 'ten_dd_efee_r', 'kftc_bkpr', 'kftc_deal_bas_r',
             'cur_nm'])

for day in range(1, 28):

    if day < 10:
        day = '0' + str(day)
    target_date = str(202110) + str(day)

    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=' + AUTHKEY + '&searchdate=' + target_date + '&data=AP01'
    response = requests.get(urlparse(url).geturl())
    result = response.json()

    for i in result:
        i['date'] = target_date

    for res in result:
        temp = json_normalize(res)
        october = october.append(temp)

# 통화별 dataframe 생성
AED = october[october['cur_unit'] == 'AED'].iloc[:, :-3]
AUD = october[october['cur_unit'] == 'AUD'].iloc[:, :-3]
CAD = october[october['cur_unit'] == 'CAD'].iloc[:, :-3]
CNH = october[october['cur_unit'] == 'CNH'].iloc[:, :-3]
EUR = october[october['cur_unit'] == 'EUR'].iloc[:, :-3]
GBP = october[october['cur_unit'] == 'GBP'].iloc[:, :-3]
HKD = october[october['cur_unit'] == 'HKD'].iloc[:, :-3]
JPY_100 = october[october['cur_unit'] == 'JPY(100)'].iloc[:, :-3]
KRW = october[october['cur_unit'] == 'KRW'].iloc[:, :-3]
USD = october[october['cur_unit'] == 'USD'].iloc[:, :-3]

# aws rds connect 위한 인증 정보
param_dic = {
    "host": "",
    "dbname": "",
    "user": "",
    "password": "",
    "port": 
}

# connect 함수 define
def connect(params_dic):
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn


# rds와 connect
conn = connect(param_dic)

# table 생성
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE public.AED (date date,ttb float,tts float, bkpr float, deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.AUD (date date,ttb float,tts float, bkpr float, deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.CAD (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.CNH (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.EUR (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.GBP (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.HKD (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.JPY_100 (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.KRW (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")
cursor.execute(
    "CREATE TABLE public.USD (date date,ttb float,tts float,bkpr float,deal_bas_r float,yy_efee_r float,ten_dd_efee_r float,kftc_bkpr float,kftc_deal_bas_r float);")

conn.commit()


# dataframe insert 위한 execute_many 함수 define
def execute_many(conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    # SQL
    query = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)" % (table, cols)
    print(query)
    cursor = conn.cursor()
    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_many() done")
    cursor.close()


# 특정 통화에서 자리수를 나타내는 ',' 때문에 insert 안되는 문제 => , 제거
for col in GBP.columns:
    GBP[col] = GBP[col].apply(lambda x: x.replace(',', ''))

for col in JPY_100.columns:
    JPY_100[col] = JPY_100[col].apply(lambda x: x.replace(',', ''))

for col in USD.columns:
    USD[col] = USD[col].apply(lambda x: x.replace(',', ''))

for col in EUR.columns:
    EUR[col] = EUR[col].apply(lambda x: x.replace(',', ''))

# db 에 insert
execute_many(conn, AED, 'public.aed')
execute_many(conn, AUD, 'public.aud')
execute_many(conn, CAD, 'public.cad')
execute_many(conn, CNH, 'public.cnh')
execute_many(conn, EUR, 'public.eur')
execute_many(conn, GBP, 'public.gbp')
execute_many(conn, HKD, 'public.hkd')
execute_many(conn, JPY_100, 'public.jpy_100')
execute_many(conn, KRW, 'public.krw')
execute_many(conn, USD, 'public.usd')

conn.commit()