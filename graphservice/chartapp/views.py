import psycopg2
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render

from time import mktime, strptime


class ERPredictAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    conn = psycopg2.connect(
        host="database-1.ck9mt4aiy0zp.ap-northeast-2.rds.amazonaws.com",
        database="test",
        user="goorm",
        password="test123qwe",
        port="5432"
    )

    def get(self, request):
        cur = ERPredictAPIView.conn.cursor()
        cur.execute("SELECT * FROM usd")
        result_list_usd = cur.fetchall()
        cur.execute("SELECT * FROM eur")
        result_list_eur = cur.fetchall()
        cur.execute("SELECT * FROM jpy_100")
        result_list_jpy = cur.fetchall()
        #print(result_list_1[0][0])
        #stocks = KospiPredict.objects.all().order_by('date')

        usd_list = []
        eur_list = []
        jpy_list = []

        for stock in result_list_usd:
            time_tuple = strptime(str(stock[0]), '%Y-%m-%d')
            utc_now = mktime(time_tuple) * 1000

            usd_list.append([utc_now, stock[1]])

        for stock in result_list_eur:
            time_tuple = strptime(str(stock[0]), '%Y-%m-%d')
            utc_now = mktime(time_tuple) * 1000

            eur_list.append([utc_now, stock[1]])

        for stock in result_list_jpy:
            time_tuple = strptime(str(stock[0]), '%Y-%m-%d')
            utc_now = mktime(time_tuple) * 1000

            jpy_list.append([utc_now, stock[1]])

        data = {
            'usd': usd_list,
            'eur': eur_list,
            'jpy': jpy_list
        }

        return Response(data)


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartapp/chart.html')