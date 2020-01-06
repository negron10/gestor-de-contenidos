from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.content.serializers import CategorySerializer, ContentSerializer, CommentSerializer, FileSerializer
from content.models import Category, Content, Comment, File

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
            
    #metodo para activar categorias     
    @action(methods=['get'], detail=False, url_path='activated/(?P<id>[^/]+)')
    def activated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            category = Category.objects.get(id=id)
            category.status = 1
            category.save()
            serializer = CategorySerializer(category)
            return Response(serializer.data, status.HTTP_200_OK)
        except Category.DoesNotExist:
            message = {'error': 'Categoria no encontrada'}
            return Response(message, status.HTTP_404_NOT_FOUND)
    
    #metodo para inactivar categorias   
    @action(methods=['get'], detail=False, url_path='deactivated/(?P<id>[^/]+)')
    def deactivated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            category = Category.objects.get(id=id)
            category.status = 0
            category.save()
            serializer = CategorySerializer(category)
            return Response(serializer.data, status.HTTP_200_OK)
        except Category.DoesNotExist:
            message = {'error': 'Categoria no encontrada'}
            return Response(message, status.HTTP_404_NOT_FOUND)

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
    #metodo para listar contenido por fecha           
    @action(methods=['get'], detail=False, url_path='list_content_byDate/(?P<createDates>[^/]+)')
    def lista_content_byDate(self, request, *args, **kwargs):
        try:
            createDates = kwargs.get('createDates')
            content =  Content.objects.filter(createDates=createDates).all()
            serializer =  ContentSerializer(content, many=True)
            return Response(serializer.data)
        except Content.DoesNotExist:
            message = {'error': 'No existe archivos para esta fecha'}
            return Response(message, status.HTTP_404_NOT_FOUND)
    
    #metodo para buscar contenido por titulo
    @action(methods=['get'], detail=False, url_path='searching/(?P<title>[^/]+)')
    def searching(self, request, *args, **kwargs):
        try:
            title = kwargs.get('title')
            content = Content.objects.get(title=title)
            serializer = ContentSerializer(content)
            return Response(serializer.data, status.HTTP_200_OK)
        except Content.DoesNotExist:
            message = {'error': 'No existe el contenido'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para buscar contenido por subtitulo
    @action(methods=['get'], detail=False, url_path='searching_subtitle/(?P<subtitle>[^/]+)')
    def searching_subtitle(self, request, *args, **kwargs):
        try:
            subtitle = kwargs.get('subtitle')
            content = Content.objects.get(subtitle=subtitle)
            serializer = ContentSerializer(content)
            return Response(serializer.data, status.HTTP_200_OK)
        except Content.DoesNotExist:
            message = {'error': 'No existe el contenido'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para activar contenido      
    @action(methods=['get'], detail=False, url_path='activated/(?P<id>[^/]+)')
    def activated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            content = Content.objects.get(id=id)
            content.status = 1
            content.save()
            serializer = ContentSerializer(content)
            return Response(serializer.data, status.HTTP_200_OK)
        except Content.DoesNotExist:
            message = {'error': 'Contenido no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)
    
    #metodo para bloquear contenido    
    @action(methods=['get'], detail=False, url_path='deactivated/(?P<id>[^/]+)')
    def deactivated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            content = Content.objects.get(id=id)
            content.status = 0
            content.save()
            serializer = ContentSerializer(content)
            return Response(serializer.data, status.HTTP_200_OK)
        except Content.DoesNotExist:
            message = {'error': 'Contenido no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar contenido segun el estado
    @action(methods=['get'], detail=False, url_path='list_content_byState/(?P<status>[^/]+)')
    def lista_content_byState(self, request, *args, **kwargs):
        try:
            status = kwargs.get('status')
            content =  Content.objects.filter(status=status).all()
            serializer =  ContentSerializer(content, many=True)
            return Response(serializer.data)
        except Content.DoesNotExist:
            message = {'error': 'Contenido no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)
           
    #metodo para listar contenido por persona
    @action(methods=['get'], detail=False, url_path='list_content_byPerson/(?P<id_person>[^/]+)')
    def lista_content_byPerson(self, request, *args, **kwargs):
        try:
            id_person = kwargs.get('id_person')
            content =  Content.objects.filter(person__id=id_person).all()
            serializer =  ContentSerializer(content, many=True)
            return Response(serializer.data)
        except Content.DoesNotExist:
            message = {'error': 'Contenido no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar contenido por categoria
    @action(methods=['get'], detail=False, url_path='list_content_byCategory/(?P<id_category>[^/]+)')
    def lista_content_byCategory(self, request, *args, **kwargs):
        try:
            id_category = kwargs.get('id_category')
            content =  Content.objects.filter(category__id=id_category).all()
            serializer =  ContentSerializer(content, many=True)
            return Response(serializer.data)
        except Content.DoesNotExist:
            message = {'error': 'Contenido no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    #metodo para listar comentarios por fecha           
    @action(methods=['get'], detail=False, url_path='list_comment_byDate/(?P<createDates>[^/]+)')
    def lista_comment_byDate(self, request, *args, **kwargs):
        try:
            createDates = kwargs.get('createDates')
            comment =  Comment.objects.filter(createDates=createDates).all()
            serializer =  CommentSerializer(comment, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            message = {'error': 'No existe archivos para esta fecha'}
            return Response(message, status.HTTP_404_NOT_FOUND)
    
    #metodo para activar comentarios   
    @action(methods=['get'], detail=False, url_path='activated/(?P<id>[^/]+)')
    def activated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            comment = Comment.objects.get(id=id)
            comment.status = 1
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status.HTTP_200_OK)
        except Comment.DoesNotExist:
            message = {'error': 'No existe el comentario'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para bloquear comentarios
    @action(methods=['get'], detail=False, url_path='deactivated/(?P<id>[^/]+)')
    def deactivated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            comment = Comment.objects.get(id=id)
            comment.status = 0
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status.HTTP_200_OK)
        except Comment.DoesNotExist:
            message = {'error': 'No exite el comentario'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar comentarios segun el estado
    @action(methods=['get'], detail=False, url_path='list_comment_byState/(?P<status>[^/]+)')
    def lista_comment_byState(self, request, *args, **kwargs):
        try:
            status = kwargs.get('status')
            comment =  Comment.objects.filter(status=status).all()
            serializer =  CommentSerializer(comment, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            message = {'error': 'Comentario no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)
           
    #metodo para listar comentarios por persona
    @action(methods=['get'], detail=False, url_path='list_comment_byPerson/(?P<id_person>[^/]+)')
    def lista_comment_byPerson(self, request, *args, **kwargs):
        try:
            id_person = kwargs.get('id_person')
            comment =  Comment.objects.filter(person__id=id_person).all()
            serializer =  CommentSerializer(comment, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            message = {'error': 'Comentario no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar comentarios hechos a cada contenido
    @action(methods=['get'], detail=False, url_path='list_comment_byContent/(?P<id_content>[^/]+)')
    def lista_comment_byContent(self, request, *args, **kwargs):
        try:
            id_content = kwargs.get('id_content')
            comment =  Comment.objects.filter(content__id=id_content).all()
            serializer =  CommentSerializer(comment, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            message = {'error': 'Comentario no encontrado'}
            return Response(message, status.HTTP_404_NOT_FOUND)

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    #metodo para activar archivos   
    @action(methods=['get'], detail=False, url_path='activated/(?P<id>[^/]+)')
    def activated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            files = File.objects.get(id=id)
            files.status = 1
            files.save()
            serializer = FileSerializer(files)
            return Response(serializer.data, status.HTTP_200_OK)
        except File.DoesNotExist:
            message = {'error': 'No existe el archivo'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para bloquear archivos
    @action(methods=['get'], detail=False, url_path='deactivated/(?P<id>[^/]+)')
    def deactivated(self, request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            files = File.objects.get(id=id)
            files.status = 0
            files.save()
            serializer = FileSerializer(files)
            return Response(serializer.data, status.HTTP_200_OK)
        except File.DoesNotExist:
            message = {'error': 'No existe el archivo'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para buscar archivos por la extension
    @action(methods=['get'], detail=False, url_path='searching/(?P<extension>[^/]+)')
    def searching(self, request, *args, **kwargs):
        try:
            extension = kwargs.get('extension')
            files = File.objects.get(extension=extension)
            serializer = FileSerializer(files)
            return Response(serializer.data, status.HTTP_200_OK)
        except File.DoesNotExist:
            message = {'error': 'No existe el archivo'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar archivos segun el estado
    @action(methods=['get'], detail=False, url_path='list_file_byState/(?P<status>[^/]+)')
    def lista_file_byState(self, request, *args, **kwargs):
        try:
            status = kwargs.get('status')
            files =  File.objects.filter(status=status).all()
            serializer =  FileSerializer(files, many=True)
            return Response(serializer.data)
        except File.DoesNotExist:
            message = {'error': 'No existe el archivo'}
            return Response(message, status.HTTP_404_NOT_FOUND)
            
    #metodo para listar archivos segun el contenido al que pertenecen           
    @action(methods=['get'], detail=False, url_path='list_file_byContent/(?P<id_content>[^/]+)')
    def lista_file_byContent(self, request, *args, **kwargs):
        try:
            id_content = kwargs.get('id_content')
            files =  File.objects.filter(content__id=id_content).all()
            serializer =  FileSerializer(files, many=True)
            return Response(serializer.data)
        except File.DoesNotExist:
            message = {'error': 'No existe el archivo'}
            return Response(message, status.HTTP_404_NOT_FOUND)
        
    #metodo para listar archivos por fecha           
    @action(methods=['get'], detail=False, url_path='list_file_byDate/(?P<uploadDates>[^/]+)')
    def lista_file_byDate(self, request, *args, **kwargs):
        try:
            uploadDates = kwargs.get('uploadDates')
            files =  File.objects.filter(uploadDates=uploadDates).all()
            serializer =  FileSerializer(files, many=True)
            return Response(serializer.data)
        except File.DoesNotExist:
            message = {'error': 'No existe archivos para esta fecha'}
            return Response(message, status.HTTP_404_NOT_FOUND)
