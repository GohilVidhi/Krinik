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
# pair_1


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
        





#---------------Pair with captain View----------------------    
# pair_2
class Pair_with_captain_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                pair = Pair_with_captain.objects.get(id=id)
                serializer = Pair_with_captain_Serializer(pair)
                return Response({'status': 'success', 'data': serializer.data})
            except Pair_with_captain.DoesNotExist:
                return Response({'status': 'Invalid id'})
        else:
            pairs = Pair_with_captain.objects.all()
            serializer = Pair_with_captain_Serializer(pairs, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = Pair_with_captain_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': 'invalid data', 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                pair = Pair_with_captain.objects.get(id=id)
            except Pair_with_captain.DoesNotExist:
                return Response({'status': 'invalid id'})

            serializer = Pair_with_captain_Serializer(pair, data=request.data, partial=True)
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
                pair = Pair_with_captain.objects.get(id=id)
                pair.delete()
                return Response({'status': 'Deleted data'})
            except Pair_with_captain.DoesNotExist:
                return Response({'status': 'invalid id'})
        else:
            return Response({'status': 'id required'})
                
                
                
#---------------Pair with captain and vice captain View----------------    
# pair_3

class Pair_with_captain_v_captain_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                pair = Pair_with_captain_and_v_captain.objects.get(id=id)
                serializer = Pair_with_captain_and_v_captain_Serializer(pair)
                return Response({'status': 'success', 'data': serializer.data})
            except Pair_with_captain_and_v_captain.DoesNotExist:
                return Response({'status': 'Invalid id'})
        else:
            pairs = Pair_with_captain_and_v_captain.objects.all()
            serializer = Pair_with_captain_and_v_captain_Serializer(pairs, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = Pair_with_captain_and_v_captain_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': 'invalid data', 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                pair = Pair_with_captain_and_v_captain.objects.get(id=id)
            except Pair_with_captain_and_v_captain.DoesNotExist:
                return Response({'status': 'invalid id'})

            serializer = Pair_with_captain_and_v_captain_Serializer(pair, data=request.data, partial=True)
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
                pair = Pair_with_captain_and_v_captain.objects.get(id=id)
                pair.delete()
                return Response({'status': 'Deleted data'})
            except Pair_with_captain_and_v_captain.DoesNotExist:
                return Response({'status': 'invalid id'})
        else:
            return Response({'status': 'id required'})
                



#======
        
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
        
        
        
        
        
#==========Match Views==================



class match_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Match.objects.get(id=id)
                serializer = MatchSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Match.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Match.objects.all()
            serializer = MatchSerializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Match.objects.get(id=id)
        except Match.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = MatchSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Match.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Match.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})





#=============  Add_pool views  =======================
class Add_pool_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Add_Pool.objects.get(id=id)
                serializer = AddPoolSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Add_Pool.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Add_Pool.objects.all()
            serializer = AddPoolSerializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = AddPoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Add_Pool.objects.get(id=id)
        except Add_Pool.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = AddPoolSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Add_Pool.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Add_Pool.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

#======================  Captain Add Pool View ==========================
class Captain_Add_Pool_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Captain_Add_Pool.objects.get(id=id)
                serializer = Captain_Add_PoolSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Match.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Captain_Add_Pool.objects.all()
            serializer = Captain_Add_PoolSerializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = Captain_Add_PoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Captain_Add_Pool.objects.get(id=id)
        except Captain_Add_Pool.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = Captain_Add_PoolSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Captain_Add_Pool.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Captain_Add_Pool.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


#========================Vice Captain Add Pool View==========================
class Vice_Captain_Add_Pool_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Vice_Captain_Add_Pool.objects.get(id=id)
                serializer = Vice_Captain_Add_PoolSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Match.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Vice_Captain_Add_Pool.objects.all()
            serializer = Vice_Captain_Add_PoolSerializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = Vice_Captain_Add_PoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Vice_Captain_Add_Pool.objects.get(id=id)
        except Vice_Captain_Add_Pool.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = Vice_Captain_Add_PoolSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Vice_Captain_Add_Pool.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Vice_Captain_Add_Pool.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})




#===========Pool declare views------------------
class Pool_Declare_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Pool_Declare.objects.get(id=id)
                serializer = Pool_Declare_Serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Match.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Pool_Declare.objects.all()
            serializer = Pool_Declare_Serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = Pool_Declare_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Pool_Declare.objects.get(id=id)
        except Pool_Declare.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = Pool_Declare_Serializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Pool_Declare.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Pool_Declare_Serializer.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})




class user_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=user.objects.get(id=id)
                serializer=user_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=user.objects.all().order_by("-id")
            for i in uid:
                print(i.date_time)
            serializer=user_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=user_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=user.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=user_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
              
    def delete(self,request,id=None):
        if id:
            try:
                uid=user.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})        
        

class login_view(APIView):
    def get(self,request,id=None , email=None):  

        if id:
        
            try:
                uid=login_user.objects.get(id=id)
                serializer=login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        elif email:
        
            try:
                uid=login_user.objects.get(email=email)
                serializer=login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})    
        else:
            uid=login_user.objects.all().order_by("-id")
            serializer=login_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=login_serializers(data=request.data)
        if serializer.is_valid():
            user1=serializer.save()
            print(user1)
            request.session["email"]=user1.email
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=login_user.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=login_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"}) 
    def delete(self,request,id=None,email=None):
        if id:
            try:
                uid=login_user.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        elif email:
            del request.session['email']
            return Response({'status': 'Logged out successfully'})

        else:
            return Response({'status':"invalid data"})        
    def logout(self, request):
        try:
            del request.session['email']
        except KeyError:
            pass
        return Response({'status': 'Logged out successfully'})