from django.urls import path,re_path
from django.urls.resolvers import URLPattern




urlpatterns = [

  path('users/login/',TokenObtainPairView.as_view(),name='token_obtain_pair')
]
