from django.urls import path
from . import views
# urlpatterns = [
#     path('',views.home),
    
#     path("list/",views.list_todo_items),
#     path("insert/",views.insert_item,name='insert_todo_item'),
#     path("delete/<int:todo_id>",views.delete_todo,name='delete_todo_item'),
    
# ]



########## urls for views with rest_api integration  ############
urlpatterns = [
    path('',views.view_items),
    path('create/',views.adduser),
    #for getting the single user
    path('read/<str:pk>', views.getuser),
    path('update/<int:pk>',views.updateuser),
    path('delete/<str:pk>',views.deleteuser),
    
]


