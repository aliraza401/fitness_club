from django.urls import path, include
from manager import views
from django.contrib.auth import views as authviews

app_name = 'manager'

urlpatterns = [
    path('', views.AdminDash.as_view(), name='adminDash'),
    path('create/', views.CreateAdmin.as_view(), name='adminC'),
    path('login/', authviews.LoginView.as_view(template_name='admin_login.html'),
         name='adminLogin'),
    path('logout/', authviews.LogoutView.as_view(), name='adminLogout'),

    path('member/search/', views.SearchMember, name='memberSearch'),
    path('member/create/', views.CreateMember.as_view(), name='memberC'),
    path('member/', views.ViewAllMembers.as_view(), name='memberlist'),
    path('member/<int:pk>', views.ViewsDetailMember.as_view(), name='memberDetail'),
    path('member/update/<int:pk>',
         views.UpdateMemberDetails.as_view(), name='memberUpdate'),
    path('member/delete/<int:pk>',
         views.DeleteMemberDetails.as_view(), name='memberDelete'),

    path('trainer/search/', views.SearchTrainer, name='trainerSearch'),
    path('trainer/create/', views.CreateTrainer.as_view(), name='trainerC'),
    path('trainer/', views.ViewAllTrainers.as_view(), name='trainerlist'),
    path('trainer/<int:pk>', views.ViewsDetailTrainer.as_view(), name='trainerDetail'),
    path('trainer/update/<int:pk>', views.UpdateTrainerDetails.as_view(),
         name='trainerUpdate'),
    path('trainer/delete/<int:pk>', views.DeleteTrainerDetails.as_view(),
         name='trainerDelete'),

     path('member/add/fee' , views.CreateFee.as_view() , name='memberFee'),
     path('member/add/fee/<int:pk>' , views.CreateFee.as_view() , name='memberFeeById'),

]
