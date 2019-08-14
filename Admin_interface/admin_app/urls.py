from django.urls import path
from admin_app import views


app_name = 'admin'

urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
    path('password/change', views.change_password, name='change_password'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('user/add/', views.UserAdd.as_view(), name='add_user'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user'),
    path('user/delete/', views.delete_user, name='delete_selected_user'),
    path('group/<slug:group>/', views.GroupListView.as_view(), name='group_list'),
    path('user/update/<int:pk>/', views.UserUpdate.as_view(), name='update_user'),
    path('services/list/', views.CategoryListView.as_view(), name='category_list'),
    path('service/add/', views.CategoryAdd.as_view(), name='category_add'),
    path('service/update/<int:pk>/', views.CategoryDetailUpdate.as_view(), name='category_update'),
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('product/add/', views.ProductAdd.as_view(), name='product_add'),
    path('product/update/<int:pk>/', views.ProductDetailUpdate.as_view(), name='product_update'),
]
