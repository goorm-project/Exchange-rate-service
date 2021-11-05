from django.urls import path

from chartapp.views import KospiPredictAPIView, ChartView

urlpatterns = [
    path('api/predict/', KospiPredictAPIView.as_view(), name="predict_kospi_api"),
    path('chart', ChartView.as_view(), name="chart"),
]