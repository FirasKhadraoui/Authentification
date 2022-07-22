from django.urls import re_path as url, path
from App import views
from .views import RegisterView, LoginView, UserView, logoutView

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns=[
    url(r'^project$',views.projectApi),
    url(r'^project/([0-9]+)$',views.projectApi),
    path('import_csv/', views.Import_csv,name="Import_csv"),  
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout',logoutView.as_view())
]