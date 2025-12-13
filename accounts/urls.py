from django.urls import path
from accounts.views import *

app_name = 'accounts_app'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name="signup"),
]
