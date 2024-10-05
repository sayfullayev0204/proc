from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.tashkilot_view, name='home'),
    path('tuman/<int:tuman_id>/', views.tuman_view, name='tuman'),
    path('mahalla/<int:mahalla_id>/', views.mahalla_view, name='mahalla'),
    path('xizmat/<int:xizmat_id>/', views.xizmatlar_view, name='xizmat'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('axoli/<int:axoli_id>/', views.axoli_detail_view, name='axoli_detail'),
    # Other URLs
]
