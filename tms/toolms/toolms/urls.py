from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from tools.views import (
    ToolCreateView,
    ToolListView,
    ToolEditView,
    ToolDeleteView,
    ToolRequestView,
)
from users.views import (
    UserListView,
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('tools_new', ToolCreateView.as_view(), name='tools_new'),
    path('tools_list', ToolListView.as_view(), name='tools_list'),
    path('<int:pk>/tool/edit/', ToolEditView.as_view(), name='tools_edit'),
    path('<int:pk>/tool/delete/', ToolDeleteView.as_view(), name='tools_delete'),
    path('<int:pk>/tool/request/', ToolRequestView.as_view(), name='tools_request'),
    path('users_list', UserListView.as_view(), name='users_list'),
]
