from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.index,name='home'),
    path('logout',views.logout,name= 'logout'), 
    # path(' ',views.sample,name= 'home')
 
]