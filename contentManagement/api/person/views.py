from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.person.serializers import PersonSerializer, RoleSerializer
from person.models import Person, Role

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    #metodo para buscar una persona por el apellido
    @action(methods=['get'], detail=False, url_path='searching/(?P<last_name>[^/]+)')
    def searching(self, request, *args, **kwargs):
        try:
            last_name = kwargs.get('last_name')
            person = Person.objects.get(last_name=last_name)
            serializer = PersonSerializer(person)
            return Response(serializer.data, status.HTTP_200_OK)
        except Person.DoesNotExist:
            message = {'error': 'Persona no encontrada'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para activar una persona      
    @action(methods=['get'], detail=False, url_path='activated/(?P<id>[^/]+)')
    def activated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            person = Person.objects.get(id=id)
            person.status = 1
            person.save()
            serializer = PersonSerializer(person)
            return Response(serializer.data, status.HTTP_200_OK)
        except Person.DoesNotExist:
            message = {'error': 'Persona no encontrada'}
            return Response(message, status.HTTP_404_NOT_FOUND)
    
    #metodo para desactivar una persona     
    @action(methods=['get'], detail=False, url_path='deactivated/(?P<id>[^/]+)')
    def deactivated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            person = Person.objects.get(id=id)
            person.status = 0
            person.save()
            serializer = PersonSerializer(person)
            return Response(serializer.data, status.HTTP_200_OK)
        except Person.DoesNotExist:
            message = {'error': 'Persona no encontrada'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar personas segun el rol
    @action(methods=['get'], detail=False, url_path='list_person_byRole/(?P<id_role>[^/]+)')
    def lista_person_byRole(self, request, *args, **kwargs):
        try:
            id_role = kwargs.get('id_role')
            people =  Person.objects.filter(role__id=id_role).all()
            serializer =  PersonSerializer(people, many=True)
            return Response(serializer.data)
        except Person.DoesNotExist:
            message = {'error': 'No hay Personas registradas'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar personas segun el estado
    @action(methods=['get'], detail=False, url_path='list_person_byState/(?P<status>[^/]+)')
    def lista_person_byState(self, request, *args, **kwargs):
        try:
            status = kwargs.get('status')
            people =  Person.objects.filter(status=status).all()
            serializer =  PersonSerializer(people, many=True)
            return Response(serializer.data)
        except Person.DoesNotExist:
            message = {'error': 'No hay Personas registradas'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar personas segun su genero
    @action(methods=['get'], detail=False, url_path='list_person_byGender/(?P<gender>[^/]+)')
    def lista_person_byGender(self, request, *args, **kwargs):
        try:
            gender = kwargs.get('gender')
            people =  Person.objects.filter(gender=gender).all()
            serializer =  PersonSerializer(people, many=True)
            return Response(serializer.data)
        except Person.DoesNotExist:
            message = {'error': 'No hay Personas registradas'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar personas segun el pais
    @action(methods=['get'], detail=False, url_path='list_person_byCountry/(?P<country>[^/]+)')
    def lista_person_byCountry(self, request, *args, **kwargs):
        try:
            country = kwargs.get('country')
            people =  Person.objects.filter(country=country).all()
            serializer =  PersonSerializer(people, many=True)
            return Response(serializer.data)
        except Person.DoesNotExist:
            message = {'error': 'No hay Personas registradas'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
    #metodo para activar un rol        
    @action(methods=['get'], detail=False, url_path='activated/(?P<id>[^/]+)')
    def activated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            role = Role.objects.get(id=id)
            role.status = 1
            role.save()
            serializer = RoleSerializer(role)
            return Response(serializer.data, status.HTTP_200_OK)
        except Role.DoesNotExist:
            message = {'error': 'No existe el rol'}
            return Response(message, status.HTTP_404_NOT_FOUND)
    
    #metodo para inactivar un rol        
    @action(methods=['get'], detail=False, url_path='deactivated/(?P<id>[^/]+)')
    def deactivated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            role = Role.objects.get(id=id)
            role.status = 0
            role.save()
            serializer = RoleSerializer(role)
            return Response(serializer.data, status.HTTP_200_OK)
        except Role.DoesNotExist:
            message = {'error': 'No existe el rol'}
            return Response(message, status.HTTP_404_NOT_FOUND)



