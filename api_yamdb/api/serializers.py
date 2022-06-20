from rest_framework import serializers, validators

from reviews.models import Category, Genre, Title, Review, Comment


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField( 
        slug_field='username', read_only=True 
    ) 
    title_id = TitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField( 
        slug_field='username', read_only=True 
    ) 
    review_id = ReviewSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"
