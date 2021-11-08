import requests
from urllib.parse import urlparse
import pandas as pd
from pandas import json_normalize
import psycopg2



#오늘 날짜 출력 함수
def getTodayDate():
    year = pd.Timestamp.now().year
    month = pd.Timestamp.now().month
    day = pd.Timestamp.now().day
    
    if day < 10:
        day = '0'+ str(day)
    todayDate = str(year)+str(month) + str(day)

    return todayDate


#target_date의 환율 정보 불러오기

def getData(target_date):
    #type your AUTHKEY
    AUTHKEY = ''
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey='+AUTHKEY+'&searchdate='+target_date+'&data=AP01'
    response = requests.get(urlparse(url).geturl())
    result = response.json()

    data = pd.DataFrame(columns= ['date','ttb','tts',	'deal_bas_r',	'bkpr',	'yy_efee_r',	'ten_dd_efee_r',	'kftc_bkpr',	'kftc_deal_bas_r',	'cur_nm'])

    for res in result:
        res['date'] = target_date
        temp = json_normalize(res)
        data = data.append(temp)

    return data



#connect 함수 define
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



#dataframe insert 위한 execute_many 함수 define
def execute_many(conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    # SQL
    query  = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)" % (table, cols)
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
    print("success")
    cursor.close()
    



#통화별 dataframe 생성
target_date = getTodayDate()
data = getData(target_date)

AED =  data[data['cur_unit'] == 'AED'].iloc[:,:-3]
AUD =  data[data['cur_unit'] == 'AUD'].iloc[:,:-3]
CAD =  data[data['cur_unit'] == 'CAD'].iloc[:,:-3]
CNH =  data[data['cur_unit'] == 'CNH'].iloc[:,:-3]
EUR =  data[data['cur_unit'] == 'EUR'].iloc[:,:-3]
GBP =  data[data['cur_unit'] == 'GBP'].iloc[:,:-3]
HKD =  data[data['cur_unit'] == 'HKD'].iloc[:,:-3]
JPY_100 =  data[data['cur_unit'] == 'JPY(100)'].iloc[:,:-3]
KRW =  data[data['cur_unit'] == 'KRW'].iloc[:,:-3]
USD = data[data['cur_unit'] == 'USD'].iloc[:,:-3]


#특정 통화에서 자리수를 나타내는 ',' 때문에 insert 안되는 문제 => , 제거
for col in GBP.columns:
  GBP[col] = GBP[col].apply(lambda x : x.replace(',',''))

for col in JPY_100.columns:
  JPY_100[col] = JPY_100[col].apply(lambda x : x.replace(',',''))

for col in USD.columns:
  USD[col] = USD[col].apply(lambda x : x.replace(',',''))

for col in EUR.columns:
  EUR[col] = EUR[col].apply(lambda x : x.replace(',',''))



#aws rds connect 위한 인증 정보    
param_dic = {
    "host": 
    "dbname": 
    "user": 
    "password": 
    "port": 
}
    
#rds와 connect
conn = connect(param_dic)



#db 에 insert
execute_many(conn,AED,'public.aedhttps://www.researchgate.net › ... › Python
2021. 1. 18. — The paper describes the PyChart module (aimed at analysis and visual')
execute_many(conn,AUD,'public.aud')
execute_many(conn,CAD,'public.cad')
execute_many(conn,CNH,'public.cny')
execute_many(conn,EUR,'public.eur')
execute_many(conn,GBP,'public.gbp')
execute_many(conn,HKD,'public.hkd')
execute_many(conn,JPY_100,'public.jpy_100')
execute_many(conn,KRW,'public.krw')
execute_many(conn,USD,'public.usd')

conn.commit()
print('insert into database has finished')
