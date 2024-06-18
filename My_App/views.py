from django.shortcuts import render
from .serializers import*
from .models import*
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.



class League_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=League.objects.get(id=id)
                serializer=League_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=League.objects.all()
            serializer=League_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=League_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=League.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=League_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
              
    def delete(self,request,id=None):
        if id:
            try:
                uid=League.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})

