from django.shortcuts import render
from .serializers import*
from .models import*
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


# Create your views here.

#------------------League View---------------------

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
            uid=League.objects.all().order_by("-id")
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



#---------------Team View----------------------



class Team_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=Team.objects.get(id=id)
                serializer=Team_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=Team.objects.all()
            serializer=Team_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=Team_serializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=Team.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=Team_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
                
    def delete(self,request,id=None):
        if id:
            try:
                uid=Team.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
        

#---------------Player View----------------------

class Player_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=Player.objects.get(id=id)
                serializer=Player_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=Player.objects.all()
            serializer=Player_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=Player_serializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=Player.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=Player_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
           
    def delete(self,request,id=None):
        if id:
            try:
                uid=Player.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
        
#---------------Pool View----------------------        
class pool_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Pool.objects.get(id=id)
                serializer = PoolSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Pool.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Pool.objects.all()
            serializer = PoolSerializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = PoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Pool.objects.get(id=id)
        except Pool.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = PoolSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Pool.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Pool.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})






#---------------Pair View----------------------    


class Pair_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                pair = Pair.objects.get(id=id)
                serializer = PairSerializer(pair)
                return Response({'status': 'success', 'data': serializer.data})
            except Pair.DoesNotExist:
                return Response({'status': 'Invalid id'})
        else:
            pairs = Pair.objects.all()
            serializer = PairSerializer(pairs, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = PairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': 'invalid data', 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                pair = Pair.objects.get(id=id)
            except Pair.DoesNotExist:
                return Response({'status': 'invalid id'})

            serializer = PairSerializer(pair, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': 'invalid data', 'errors': serializer.errors})
        else:
            return Response({'status': 'id required'})

    def delete(self, request, id=None):
        if id:
            try:
                pair = Pair.objects.get(id=id)
                pair.delete()
                return Response({'status': 'Deleted data'})
            except Pair.DoesNotExist:
                return Response({'status': 'invalid id'})
        else:
            return Response({'status': 'id required'})
        
        
        
class new_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=new.objects.get(id=id)
                serializer=new_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=new.objects.all()
            serializer=new_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=new_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=new.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=new_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
              
    def delete(self,request,id=None):
        if id:
            try:
                uid=new.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})    