from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('', include('portfolio.urls')),
    path('', include('resume.urls')),
    path('', include('activity.urls')),
    path('', include('contest.urls')),
    path('', include('club.urls')),
]