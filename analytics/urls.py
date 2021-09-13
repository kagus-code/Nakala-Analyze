from django.urls import path,re_path
from django.urls.resolvers import URLPattern
from . import views





urlpatterns = [

  path('users/login/',views.MyTokenObtainPairView.as_view(),name='token_obtain_pair')
]
