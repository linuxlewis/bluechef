from rest_framework import routers

from recipes import views

router = routers.SimpleRouter()
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = router.urls
