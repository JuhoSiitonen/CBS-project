from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("like/<int:posting_id>/", views.like, name="like"),
    path("posting/<int:posting_id>/", views.posting, name="posting"),
]