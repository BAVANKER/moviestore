from django.urls import path
from movieapp import views
app_name = 'movieapp'
# env name: movie, admin: movieadmin, pw: 1234, db: moviedatas

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
