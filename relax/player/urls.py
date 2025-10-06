from .views import register, user_login, user_logout, home, video_gallery, pagina1, pagina2, pagina3, pagina4, pagina5, pagina6
from django.urls import path

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),
    path('home/', home, name='home-explicit'),
    path('pagina1/', pagina1, name='pagina1'),
    path('pagina2/', pagina2, name='pagina2'),
    path('pagina3/', pagina3, name='pagina3'),
    path('pagina4/', pagina4, name='pagina4'),
    path('pagina5/', pagina5, name='pagina5'),
    path('pagina6/', pagina6, name='pagina6'),
    # videos gallery
    path('videos/', video_gallery, name='videos'),
]