from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from myapp import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('uttej', admin.site.urls),
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact_us,name="contact"),
    path('about/',views.about,name="about"),
    path('team/',views.team_members,name="team"),
    path('dishes/',views.all_dishes,name="all_dishes"),
    path('dishes/payment',views.payment,name="payment"),
    path('register/',views.register,name="register"),
    path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    path('login/', views.signin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('dish/<int:id>/', views.single_dish, name='dish'),
    path('dish/<int:id>/payment', views.payment , name='payment'),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('payment_done/', views.payment_done, name='payment_done'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
