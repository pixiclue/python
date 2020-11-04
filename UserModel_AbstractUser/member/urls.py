from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import include, path, re_path
from . import views

app_name = 'member'


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="signUp"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


