from django.urls import path
from . import views

app_name = 'user_data'


urlpatterns = [
    path('post_upload/',views.BasicUploadView.as_view(),name='data'),
    path('post_data/',views.DisplayImages.as_view(),name='pic'),
    path('detail/<int:pk>',views.UserDataDet.as_view(template_name='details.html'),name='getid'),
    path('edit/<int:pk>',views.UserDetailUpdate.as_view(template_name='userdetailedit.html'),name='edit'),
    path('delete/<int:pk>',views.UserDetailDelete.as_view(template_name='userdelete.html'),name='delete'),

]