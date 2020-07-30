from django.urls import path

from blog.views import user_view

urlpatterns = [
    path('user/', user_view.base),
    path('user/<int:user_id>', user_view.with_id),
]
