from django.urls import path
from . import views

app_name = "reader"
urlpatterns = [
    path('', views.mecanicas, name='mecanica'),
    path('eletrica/', views.eletricas, name='eletrica'),
    path('eletronica/', views.eletronicas, name='eletronica'),
    path('add/', views.add, name='add'),
    path('save_qr_data/', views.save_qr_data, name='save_qr_data'),
    path('off_to_on/', views.off_to_on, name='off_to_on'),
    path('reset/<str:tabela>/', views.reset, name='reset'),
    path('delete_line/', views.delete_line, name='delete_line'),
    path('add_event/', views.add_event, name='add_event'),
    path('logout/', views.user_logout, name='logout'),
]