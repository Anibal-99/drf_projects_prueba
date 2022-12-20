from rest_framework import routers
from .api import ProjectsViewSets

router =    routers.DefaultRouter()

router.register('api/projects', ProjectsViewSets, 'projects') # se creo una ruta con los tipicos cruds

urlpatterns = router.urls # para que se generen las urls
