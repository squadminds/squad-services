from django. urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


# we will use router + viewset combination to handle the GET,POST,DELETE,PATCH request in just one view
router = routers.DefaultRouter()
router.register('choices', views.ChoiceViewSet)


urlpatterns = [
    path('polls/list/', views.PollList.as_view(), name='poll_list_api'),
    path('polls/<int:pk>/', views.PollDetail.as_view(), name='poll_detail_api'),
    path('rest-auth/', include('rest_auth.urls')),
    # include authentications. Login/Logout
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='obtain_token_auth'),
    # Include Login link at the interface
    path('users/list/', views.UserList.as_view(), name='user_list_api_view'),
    path('', include(router.urls)),
    # Includes all the choices/list, choices/2 in a single view and makes url dynamically
]