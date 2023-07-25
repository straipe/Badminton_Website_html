from django.urls import include, path
from . import views

app_name = 'badminton'

urlpatterns = [
    path('',views.index, name='index'),
    path('match/new/',views.match_new, name='match_new'),
    path('match/<int:pk>/', views.match_detail, name='match_detail'),
    path('review/new',views.review_new, name='review_new'),
]