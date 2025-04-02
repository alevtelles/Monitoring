from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Mentorados, Navigator
from django.contrib import messages
from django.contrib.messages import constants

def mentorados(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'GET':
        navigator = Navigator.objects.filter(user=request.user)
        mentorados = Mentorados.objects.filter(user=request.user)

        return render(request, 'mentorados.html', {'estagios': Mentorados.estagio_choices, 'navigators': navigator, 'mentorados': mentorados})
    elif request.method == 'POST':
        name = request.POST.get('nome')
        foto = request.FILES.get('foto')
        estagio = request.POST.get("estagio")
        navigator = request.POST.get('navigator')

        mentorado = Mentorados(
            name=name,
            foto=foto,
            estagio=estagio,
            navigator_id=navigator,
            user=request.user
        )

        mentorado.save()

        messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso!')
        return redirect('mentorados')