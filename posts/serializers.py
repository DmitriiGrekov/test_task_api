from rest_framework import serializers
from .models import CommentModel, PostModel
from drf_writable_nested.serializers import WritableNestedModelSerializer


class FilterCommentListSerializer(serializers.ListSerializer):
    """Филтрация комментариев"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveCommentSerializer(serializers.Serializer):
    """Вывод древовидной структуры комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    """Вывод комментариев к посту"""

    children = RecursiveCommentSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = CommentModel
        fields = ('id',
                  'post',
                  'author_name',
                  'text',
                  'pub_date',
                  'level',
                  'children',
                  )


class PostSerializer(WritableNestedModelSerializer,
                     serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    """Вывод всех постов"""

    class Meta:
        model = PostModel
        fields = ("id",
                  "title",
                  "content",
                  "created",
                  "author",
                  "comments")


class CommentAddSerializer(WritableNestedModelSerializer,
                           serializers.ModelSerializer):
    """Добавление комментариев"""

    class Meta:
        model = CommentModel
        fields = ('author_name',
                  'text')
