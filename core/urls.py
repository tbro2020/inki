from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('report/<int:pk>', Report.as_view(), name='report'),
    path('campaign/<int:pk>', Campaign.as_view(), name='campaign')
]