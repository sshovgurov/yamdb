from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from users.views import SignUpView, TokenView


router = DefaultRouter()

router.register('categories', views.CategoryView, basename='categories')
router.register('genres', views.GenreView, basename='genres')
router.register('titles', views.TitleViewSet, basename='titles')
router.register( 
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet, 
    basename='reviews' 
)
router.register( 
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet, 
    basename='comments' 
)
#router.register('users', views.UserViewSet, basename='users')


urlpatterns = [
    path('v1/', include(router.urls)),
    #path('v1/auth/create/', .as_view(), name='sign_up'), 
    #path('v1/auth/token/', .as_view(), name='token'),
]
