from django.urls import path, re_path
from apps.esite import views

urlpatterns = [
    path("", views.view_landing, name="landing_page"),
    # Matches any unknown urls
    #re_path(r'^.*\.*', views.pages, name='pages'),
]