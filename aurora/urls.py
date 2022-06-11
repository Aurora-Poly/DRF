from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('', include('portfolio.urls')),
    path('', include('activity.urls')),
    path('', include('contest.urls')),
    path('', include('club.urls')),
    #path('api-auth/', include("rest_framework.urls", namespace='rest')),
    #path('rest-auth/', include("rest_auth.urls")),

]