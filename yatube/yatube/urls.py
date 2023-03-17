from django.contrib import admin
from django.urls import include, path


handler404 = "posts.views.page_not_found_view"

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls)
]
