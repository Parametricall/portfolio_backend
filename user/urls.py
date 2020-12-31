from django.urls import path
from user import views

app_name = "user"
urlpatterns = [
    path("token/", views.CreateTokenView.as_view(), name="token"),
    path("user/create_user/", views.CreateView.as_view(), name="create"),
    path("user/users/", views.ListView.as_view(), name="list"),
    path("user/retrieve/<int:pk>/", views.RetrieveView.as_view(),
         name="retrieve"),
    path("user/update/<int:pk>/", views.UpdateView.as_view(),
         name="update"),
    path("user/destroy/<int:pk>/", views.DestroyView.as_view(),
         name="destroy"),
]
