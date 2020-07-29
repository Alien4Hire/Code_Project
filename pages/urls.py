from django.urls import path

from pages.views import about, index, charts

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('charts/', charts, name='charts'),

]
