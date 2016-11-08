from rest_framework import serializers
from .models import Post


# class PostSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     created_date = serializers.DateTimeField()
#     file = serializers.FileField()
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.file = validated_data.get('file', instance.file)
#         instance.save()
#         return instance

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'created_date', 'file',)