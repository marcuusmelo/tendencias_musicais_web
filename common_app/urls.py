from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from common_app.views import home, registration

app = 'common_app'

urlpatterns = [
    path('', home, name='main_home_page'),
    path('login', LoginView.as_view(template_name='login.html')),
    path('logout', LogoutView.as_view(template_name='logout.html')),
    path('registration', registration, name='registration')
]
