from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from django.urls.resolvers import URLPattern
from . import views





urlpatterns = [
  path('users/register/', views.RegisterApiView.as_view(), name="register"),
  path('users/login/',views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
  path('users/profile/',views.UserProfileApiView.as_view(),name='user-profile'),
  path('users/activate/<int:id>/',views.ActivateUserApiView.as_view(),name='activate-user'),
  path('data/upload/', views.UploadDataApiView.as_view(), name="upload-data"),
 path('data/query/<int:pk>/', views.CovidDataAPIView.as_view(), name="query-data-byId"),
 path('data/query/<str:iso>/', views.CovidDataByIsoAPIView.as_view(), name="query-data-byIso")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)