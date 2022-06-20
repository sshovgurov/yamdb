from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions, mixins, filters

from . import serializers
from .permissions import IsOwnerOrReadOnly
from reviews.models import Category, Genre, Title, Review, Comment


class CustomMixin(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    pass


class GenreView(CustomMixin):
    serializer_class = serializers.GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug' 
    filter_backends = (filters.SearchFilter,) 
    search_fields = ('name',) 


class CategoryView(CustomMixin):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug' 
    filter_backends = (filters.SearchFilter,) 
    search_fields = ('name',)
    

class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TitleSerializer
    queryset = Title.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get['title_id'])
        return serializer.save(author=self.request.user, title_id=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])
        return serializer.save(author=self.request.user, review_id=review)
