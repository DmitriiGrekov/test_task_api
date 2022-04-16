from rest_framework import serializers
from .models import CommentModel, PostModel
from drf_writable_nested.serializers import WritableNestedModelSerializer
from mptt.utils import previous_current_next


class FilterCommentListSerializer(serializers.ListSerializer):
    """Филтрация комментариев"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveCommentSerializer(serializers.Serializer):
    """Вывод древовидной структуры комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        # serializer = RecursiveCommentSerializer(value, context=self.context)
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

    # my_field = serializers.SerializerMethodField('is_named_bar')

    # def is_named_bar(self, instance):
        # comments = instance.comments.all()

        # cm = []

        # comment_count = len(comments)
        # iter_count = 0

        # for i in range(len(comments)-1, -1, -1) :

            # if not comments[i].is_child_node():
                # iter_count += 1
                # print(comments[i].get_children())
                
                # cm.append({
                    # 'id': comments[i].id,
                    # 'post': comments[i].post.id,
                    # 'author_name': comments[i].author_name,
                    # 'text':comments[i].text,
                    # 'pub_date': comments[i].pub_date,
                    # 'level': comments[i].level,
                    # 'children': []})

                # for children in comments[i].get_children():
                    # print(children)
        
        # return instance.title



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
