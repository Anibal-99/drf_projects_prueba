from .models import Projects
from rest_framework import viewsets, permissions
from .serializers import ProjectsSerializer

class ProjectsViewSets(viewsets.ModelViewSet): # con este viewset podemos decir quien puede hacer consusltas y que tipo de consultas podra realizar
    queryset=Projects.objects.all() # esto consulta todos los datos de una tabla
    permission_classes=[permissions.AllowAny] # esto dice que cualquier aplicacion cliente va a poder solicitar datos al servidor
    # pero esto se puede cambiar para que en un futuro verificar la sesion
    serializer_class= ProjectsSerializer
