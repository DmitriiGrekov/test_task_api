from django.db.models.query import Prefetch
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PostModel, CommentModel
from .serializers import PostSerializer, CommentAddSerializer
from rest_framework import status


@api_view(['GET', "POST"])
def api_post(request):
    """Вывод всех постов"""

    if request.method == 'GET':

        posts = PostModel.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_post_detail(request, pk):
    """Вывод одного поста"""

    if request.method == "GET":
        post = PostModel.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(["GET", 'POST'])
def api_comment_add(request, post_pk):
    """Вывод поста с комментариями и добавление комментариев к посту"""

    if request.method == 'GET':
        post = PostModel.objects.get(pk=post_pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    if request.method == "POST":
        post = PostModel.objects.get(pk=post_pk)
        serializer = CommentAddSerializer(data=request.data)

        if serializer.is_valid():
            parent_id = request.data.get('parent_id')
            if parent_id:
                parent = CommentModel.objects.get(pk=parent_id)
                if serializer.save(post=post, parent=parent):
                    pass
                else:
                    return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(post=post)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
