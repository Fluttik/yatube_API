from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer, FollowSerializer)


class FollowMixinViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """Данный класс используется для настройки методов доступа для
    класса FollowViewSet."""

    pass


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для взаимодействия с постами.
    Возможности:
    - Получение списка публикаций (GET)
    - Создание публикации (POST)
    - Получение публикации (GET)
    - Обновление публикации (PUT)
    - Частичное обновление публикации (PATCH)
    - Удаление публикации (DELETE)"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для взаимодействия с комментариями.
    Возможности:
    - Получение списка комментариев (GET)
    - Добавление комментария (POST)
    - Получение комментария (GET)
    - Обновление комментария (PUT)
    - Частичное обновление комментария (PATCH)
    - Удаление комментария (DELETE)"""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для взаимодействия с группами.
    Возможности:
    - Получение списка сообществ (GET)
    - Получение информации о сообществе (GET)"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(FollowMixinViewSet):
    """Вьюсет для взаимодействия с подписками.
    Возможности:
    - Возвращает все подписки пользователя, сделавшего запрос.
    - Подписка пользователя от имени которого сделан запрос на пользователя
      переданного в теле запроса.
    - Анонимные запросы запрещены.
    """

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
