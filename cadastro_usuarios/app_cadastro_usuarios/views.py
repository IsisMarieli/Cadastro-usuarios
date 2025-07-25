from django.shortcuts import render, get_object_or_404,redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.sobrenome = request.POST.get('sobrenome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.area_atuacao = request.POST.get('area_atuacao')
        novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)
    if request.method == "POST":
        usuario.nome = request.POST.get("nome")
        usuario.sobrenome = request.POST.get("sobrenome")
        usuario.email = request.POST.get("email")
        usuario.area_atuacao = request.POST.get("area_atuacao")
        usuario.save()
        return redirect('listagem_usuarios')
    
    return render(request, 'usuarios/editar.html',{'usuario': usuario})

def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('listagem_usuarios')

    return render(request, 'usuarios/excluir.html', {'usuario': usuario})
