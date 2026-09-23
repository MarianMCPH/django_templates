from django.shortcuts import render

# Create your views here.
def perfil_uno(request):
    data={"nombre":"Daisy", "año":1980, "correo":"daisy@example.com"}
    return render(request, 'perfil/p1.html',data)

def perfil_dos(request):
    data={"nombre":"Peach", "año":1980, "correo":"peach@example.com", "foto":"peach.webp"}
    return render(request, 'perfil/p2.html',data)