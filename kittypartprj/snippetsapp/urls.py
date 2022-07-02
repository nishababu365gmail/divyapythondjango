from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'vava', views.h)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('achan/',views.snippet_list),
    path('amma/',views.snippet_save),
    path('vava/',views.flower_list),
    path('abhay/',views.flower_save),
    path('divya/<str:flowerid>',views.editflower),
    # path('kittu/<str:name>',views.update_items),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]