from django.urls import path
from animals_app.views import AnimalDetail, AnimalList, CategoryDetail, CategoryList, CreateAnimal, CreateCategory

urlpatterns = [
    path("", CreateAnimal.as_view()),
    path('list/', AnimalList.as_view()),
    path('<int:pk>', AnimalDetail.as_view()),
    path("category", CreateCategory.as_view()),
    path('category/list/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view())
]


