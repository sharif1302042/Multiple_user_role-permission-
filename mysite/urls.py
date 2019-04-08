from django.contrib import admin
from django.urls import path
from M_USER import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/', views.AccountList.as_view()),
    path('topup/', views.TopUp.as_view()),

]
