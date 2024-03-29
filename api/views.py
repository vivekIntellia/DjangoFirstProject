from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import PostSerializer
from api.models import Post
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from django.shortcuts import render





# class ViewList(APIView):
#     def get(self,request):
#         blog=Post.objects.all()
#         serializer = PostSerializer(blog,many=True)
#         return Response({'status':201,'payload':serializer.data})
    
class ViewList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        # Serialize image URL to include full path
        data = []
        for post in serializer.data:
            post['image_url'] = request.build_absolute_uri(post['image_url'])
            data.append(post)

        return Response({'status': 201, 'payload': data})



class AddPost(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
        serializer.save()
        return Response({'payload':serializer.data,'status':201,'message':'Blog is created'})



class PostDetails(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            blog= Post.objects.get(id= pk)
            serializer = PostSerializer(blog)
            return Response({'payload':serializer.data, 'status':200})
        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})

    def patch(self,request,pk):
        try:
            blog = Post.objects.get(id=pk)
            serializer=PostSerializer(blog,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
            serializer.save()
            return Response({'payload':serializer.data,'status':201,'message':'Blog is successfully Updated'})
        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})

    def delete(self,request,pk):
        try:
            blog = Post.objects.get(id=pk)
            blog.delete()
            return Response({'message':'Blog successfully Deleted', 'status':200})

        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})






def postt(request):
    return render(request,'blog.html')



from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer
from rest_framework import status




class CommentList(APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(post=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post_id=post_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
