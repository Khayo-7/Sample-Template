from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from django.http import JsonResponse

# ￼
from .models import from .serializers import serializers
instance = serializers 

@api_view(['GET'])
def getRoutes(request):

    api_urls = {
        'List All s' : '/s/',
        'Search an ' : '/search/<str:key>/',
        'View an ' : '/view-:key>/',
        'Create an ' : '/create-:key>/',
        'Update an ' : '/update-:key>/',
        'Delete an ' : '/delete-:key>/',

    }
    return Response(api_urls)

@api_view(['GET'])
def search(request):
    try:
        items1 = instance.objects.get(__icontains=request.GET['key'])
        items2 = instance.objects.get(__icontains=request.GET['key'])
        items = items1.union(items2)
        # count = t()
        serializer = serializers(items, many = False)
        return Response(serializer.data)

    except:

        return Response("The search returned empty")

@api_view(['GET'])
def view_all(request):

    items = instance.objects.all()
    serializer = serializers(items, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def view(request, key):
    try:
        item = instance.objects.get(id=key)
        serializer = serializers(item, many = False)
        return Response(serializer.data)

    except:

        return Response("The Item is not found")

@api_view(['POST'])
def add(request):

    serializer = serializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def update(request, key):
    try:
        item = instance.objects.get(id=key)
        serializer = serializers(instance=item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)
    except:
        return Response("The Item is deleted Successfully")

@api_view(['DELETE'])
def delete(request, key):
    try:
        item = instance.objects.get(id=key)
        item.delete()
            
        return Response("The Item is deleted Successfully")
    except:

        return Response("The Item is not found")











# from django.shortcuts import render
# from django.views.generic import View
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # Create your views here.


# from Template.arguments import *
# from myapp.arguments import *
# from users.arguments import *



# class General(View):
#     def __init__(self, arguments):   
#         self.instance = arguments['instance']
#         self.instance_type = arguments['instance_type']
#         self.form = arguments['form']  
#         self.serializer = arguments['serializer']  
#         self.filter = arguments['filter']  
#         print(self.instance, self.instance_type, self.form, self.serializer, self.filter)

#     @api_view(['GET'])
#     def getRoutes(self, request):

#         print("heeeer")
#         api_urls = {
#             'List All' : '/all/',
#             'Search an ' : '/search/<str:key>/',
#             'View an ' : '/view-:key>/',
#             'Create an ' : '/create-:key>/',
#             'Update an ' : '/update-:key>/',
#             'Delete an ' : '/delete-:key>/',

#         }
#         return render(request, 'success.html', context={})
#         return Response(api_urls)              
      
#     @api_view(['GET'])
#     def search(self, request):
#         try:
#             instance = self.instance.objects.annotate(search=SearchVector(*field_names),).filter(search__icontains=key)

#             # fields = [f for f in self.instance._meta.fields if isinstance(f, CharField) or isinstance(f, DateField)]
#             # queries = [Q(**{f.name + "icontains": key}) for f in fields]
#             # qs = Q()
#             # for query in queries:
#             #     qs = qs | query

#             # instance = self.instance.objects.filter(qs).values()
#             # count = t()
#             serializer = self.serializer(instance, many = False)
#             return Response(serializer.data)

#         except:

#             return Response("The search returned empty")           
        
#     @api_view(['GET'])
#     def view_all(self, request):

#         instance = self.instance.objects.all()

#         if instance.count() > 0:
#             serializer = self.serializer(instance, many = True)
#             return Response(serializer.data)
        
#         return Response("There are 0 items found")

#     @api_view(['GET'])
#     def view(self, request, key):
#         try:
#             instance = self.instance.objects.get(pk=key)
#             serializer = self.serializer(instance, many = False)
#             return Response(serializer.data)

#         except:

#             return Response("The instance is not found")

#     @api_view(['POST'])
#     def add(self, request):

#         serializer = self.serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
            
#         return Response(serializer.data)

#     @api_view(['POST'])
#     def update(self, request, key):
#         try:
#             instance = self.instance.objects.get(pk=key)
#             serializer = self.serializer(instance=instance, data=request.data)

#             if serializer.is_valid():
#                 serializer.save()
                
#             return Response(serializer.data)
#         except:
#             return Response("The " + self.instance_type + " is updated Successfully")

#     @api_view(['DELETE'])
#     def delete(self, request, key):

#         instance = self.instance.objects.get(pk=key)
#         form = self.form(request.POST or None, instance=instance)

#         try:
#             instance = self.instance.objects.get(pk=key)
#             instance.delete()
                
#             return Response("The " + self.instance_type + " is deleted Successfully")
#         except:

#             return Response("The instance is not found")


#     @api_view(['PUT'])
#     def approve_deny(self, request, key):
#         try:
#             instance = self.instance.objects.get(pk=key)
#             serializer = self.serializer(instance=instance, data=request.data)

#             if serializer.is_valid():
#                 serializer.save()
                
#             return Response(serializer.data)
#         except:
#             return Response("The " + self.instance_type + " is approved Successfully")

#     def approve_deny(self, request, key):


#             instance = self.instance.objects.get(pk=key)

#             if form.is_valid():
#                 form = form.save(commit=False)
#                 usr = user.objects.get(pk=1)
#                 form.approved_by = None
#                 # form.created_by = request.user
#                 # if not first:
#                 #     form.updated_by = request.user
#                 form.save()
#                 messages.add_message(self, request, messages.INFO, self.instance_type + " is Approved Successfully")
#                 return redirect(self.success_url)
#             else:
#                 messages.add_message(self, request, messages.INFO, self.instance_type + " cannot be approved")
    
#     @api_view(['POST'])
#     def upload(self, request):

#         serializer = self.serializer(data=request.data)
#         # form = self.form(self, request.POST or None, request.FILES or None) 

#         if serializer.is_valid():
#             serializer.save()
#             upload = serializer.save(commit=False)
#             upload.image_data = serializer.cleaned_data['attached_image'].file.read()
        
#             usr = user.objects.get(pk=1)
#             upload.created_by = None
#             upload.updated_by = None
#             upload.save()
#         return Response(serializer.data)
