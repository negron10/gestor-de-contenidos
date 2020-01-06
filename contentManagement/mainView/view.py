from django.http import HttpResponse

def main(request):
	return HttpResponse("<h1 style='color:green; text-align:center;'>Bienvenido!</h1><br><br> \
                             <h2 style='color:blue; text-align:center;'>Sistema Gestor de Contenido</h2><br> \
                             <h3 style='color:orange; text-align:center;'>UNL</h3><br><br><br> \
                             <p style='text-align:center;'>1) <a href='http://localhost:8000/admin/'>Ingresar al panel de administrador</a></p> \
                             <p style='text-align:center;'>2) <a href='http://localhost:8000/api/content/'>Visualizar contenido de api content</a></p> \
                             <p style='text-align:center;'>3) <a href='http://localhost:8000/api/person/'>Visualizar contenido de api person</a></p> \
                             <p style='text-align:center;'>4) <a href='http://localhost:8000/docs/'>Visualizar documentacion</a></p>")
