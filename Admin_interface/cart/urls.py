from django.urls import path
from cart import views

app_name='cart'

urlpatterns=[
    path('show/',views.show,name='show'),
    path('add/<int:id>/',views.add,name='add'),
    path('remove/<int:id>/',views.remove,name='remove'),
]
