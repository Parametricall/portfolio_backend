from django.urls import path
from user import views
from rest_framework import routers

app_name = "user"

router = routers.SimpleRouter()
router.register("users", views.UserViewSet)
urlpatterns = router.urls
