# from rest_framework import serializers
# from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     image_url = serializers.ImageField(source='image.url', read_only=True)
#     class Meta:
#         model= Post
#         fields= '__all__'


from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image.url', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'



