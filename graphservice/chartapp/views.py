import psycopg2
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render

from time import mktime, strptime

import graphservice


class KospiPredictAPIView(APIView):

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
        cur = KospiPredictAPIView.conn.cursor()
        cur.execute("SELECT * FROM aed")
        result_list_1 = cur.fetchall()
        #print(result_list_1[0][0])
        #stocks = KospiPredict.objects.all().order_by('date')

        close_list = []
        open_list = []

        for stock in result_list_1:
            print(stock[0])
            time_tuple = strptime(str(stock[0]), '%Y-%m-%d')
            utc_now = mktime(time_tuple) * 1000

            close_list.append([utc_now, stock[1]])
            open_list.append([utc_now, stock[2]])

        data = {
            'close': close_list,
            'open': open_list
        }

        return Response(data)


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartapp/chart.html')