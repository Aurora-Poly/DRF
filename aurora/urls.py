from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('', include('portfolio.urls')),
    path('activity/', include('activity.urls')),
    path('contest/', include('contest.urls')),
]
