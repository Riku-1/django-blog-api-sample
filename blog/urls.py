from django.urls import path

from blog.views import user_view

urlpatterns = [
    path('users/', user_view.base),
    path('users/<int:user_id>', user_view.with_id),
]
