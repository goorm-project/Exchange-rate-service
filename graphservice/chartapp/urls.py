from django.urls import path

from chartapp.views import ChartView, ERPredictAPIView

urlpatterns = [
    path('api/predict/', ERPredictAPIView.as_view(), name="predict_kospi_api"),
    path('chart', ChartView.as_view(), name="chart"),
]