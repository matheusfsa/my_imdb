from django.conf.urls import url, include
from .views import MovieList, home, MovieDetail
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^movies/$', MovieList.as_view(), name='movie-list'),
    url(r'^movie/(?P<pk>[0-9]+)/$', MovieDetail.as_view(), name='movie-detail'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="app/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="app/home.html"), name="logout"),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$', home, name='home'),
]