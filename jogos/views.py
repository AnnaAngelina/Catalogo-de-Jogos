from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Jogo, Desenvolvedora, Plataforma


def listar_jogos(request):
    busca = request.GET.get("q", "")
    desenvolvedora_id = request.GET.get("desenvolvedora", "")
    plataforma_id = request.GET.get("plataforma", "")

    jogos = Jogo.objects.select_related("desenvolvedora", "plataforma").all()

    if busca:
        jogos = jogos.filter(nome__icontains=busca)

    if desenvolvedora_id:
        jogos = jogos.filter(desenvolvedora_id=desenvolvedora_id)

    if plataforma_id:
        jogos = jogos.filter(plataforma_id=plataforma_id)

    paginator = Paginator(jogos, 5)
    numero_pagina = request.GET.get("page")
    pagina_jogos = paginator.get_page(numero_pagina)

    contexto = {
        "jogos": pagina_jogos,
        "busca": busca,
        "desenvolvedora_selecionada": desenvolvedora_id,
        "plataforma_selecionada": plataforma_id,
        "desenvolvedoras": Desenvolvedora.objects.all(),
        "plataformas": Plataforma.objects.all(),
        "total_jogos": paginator.count,
    }

    return render(request, "jogos/listar_jogos.html", contexto)
