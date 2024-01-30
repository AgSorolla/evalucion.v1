from django.urls import path
from . import views 
  # Importa la vista 'index'


app_name = 'appnoticias'

urlpatterns=[
    path('index/',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('mas_noticias/',views.mas_noticias,name='mas_noticias'),
    path('noticia/',views.noticia,name='noticia'),
    path('register/',views.register,name='register'),
    path('sobre_nosotros/',views.sobre_nosotros,name='sobre_nosotros'),
    
]