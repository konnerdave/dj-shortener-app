from django.contrib import admin
from django.urls import path

from shortener.views import HomeView, IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<str:token>', HomeView.as_view(), name='home'),
]
