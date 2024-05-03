# from django.shortcuts import render ,redirect
# from django.http import HttpResponse ,HttpRequest
# from .models import Todo
# from .forms import todo_forms
# # importing formset_factory 
# from django.forms import formset_factory 
# # Create your views here.

# from .forms import todo_forms


# def home(request):
#     return HttpResponse('home page')

    
# def insert_item(request):
#     if  request.method=='POST':
#         form=todo_forms(request.POST)
#         if form.is_valid():
#             content=form.cleaned_data['content']
#             Todo.objects.create(content=content)
#             return redirect('/todos/list/')
#     else:
#         form = todo_forms()
#     return render(request, 'todos/todo_list.html', {'form': form})
            
        


# def list_todo_items(request):
#     x = { 'todo_list' : Todo.objects.all()}
#     return render(request,'todos/todo_list.html',x)
    
    
# # def insert_item(request:HttpRequest):
# #     #create instance of the model class for this import the model class first
# #     todo=Todo(content=request.POST['content'])
# #     todo.save()
# #     return redirect('/todos/list/')

# def delete_todo(request,todo_id):
#     item_to_delete=Todo.objects.get(id=todo_id)
#     item_to_delete.delete()
#     return redirect('/todos/list/')


#########################################

# using rest_frame work the imports be like 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import User
from .serializers import Userserializer
### to get user
@api_view(['GET'])
def view_items(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = User.objects.filter(**request.query_params.dict())
    else:
        items = User.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = Userserializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response("status.HTTP_404_NOT_FOUND")
 
#to get single   user 
@api_view(['POST'])
def getuser(request,pk):
    users=User.objects.get(id=pk)
    serializer=Userserializer(users,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def adduser(request):
    serializer=Userserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# PUT requests that will replace the information in the database with the data in the request payload.
@api_view(['POST'])
def updateuser(request,pk):
    user=User.objects.get(id=pk)
    serializer=Userserializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteuser(request,pk):
    item=User.objects.get(id=pk)
    item.delete()
    return Response("item deleted successfully")
    
    
        