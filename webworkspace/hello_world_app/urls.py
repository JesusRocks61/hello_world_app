from django.urls import path
from hello_world_app import views

urlpatterns = [
    path('score', views.score_view, name='score_view'), 

    path('score/edit/<int:score_id>/', views.edit_score, name='edit_score'), 

    path('score/delete/<int:score_id>/', views.delete_score, name='delete_score'),
]