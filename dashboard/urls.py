from django.urls import path, include
from . import views
from accounts.views import logout
from dian.views import CancelorderHistory,orderHistory
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('addpkg/',views.add_package,name='addpkg'),
    path('profile/',views.profile,name='profile'),
    path('package_list/',views.package_list,name='package_list'),
    path('user_list/',views.user_list,name='user_list'),
    path('delete_user/<int:pk>/',views.deleteUser,name='delete_user'),
    path('myorders/',orderHistory,name='myorders'),
    path('cancelorders/',CancelorderHistory,name='cancelorder'),
    path('logout/',logout,name='logout'),
    path('delete_package/<int:pk>/',views.deletePackage,name='delete_package'),
]


