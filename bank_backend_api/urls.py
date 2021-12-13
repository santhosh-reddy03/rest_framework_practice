from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('userdetail/', views.userdetails),
    path('createcustomer/', views.CustomerList.as_view()),
    path('updatecustomer/<int:pk>', views.CustomerDetail.as_view()),
    path('createaccount/', views.AccountList.as_view()),
    path('delete_customer/', views.del_customer),
    path('update_customer/', views.update_customer),
    path('create_customer/', views.create_customer),
    path('customerstatus/', views.CustomerStatusList.as_view()),
    path('login/', views.success_login),
    # path('deposit/'),
    # path('withdraw/'),
    # path('transfer/')
]