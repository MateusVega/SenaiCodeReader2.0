from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import mecanica, eletrica, eletronica, eventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='login:login')
def mecanicas(request):
    return render(request, 'reader/index.html', {'ferramentas': mecanica.objects.all().values(), 'tabela' : 'mecanica', 'evento' : eventos.objects.all().values()})

@login_required(login_url='login:login')
def eletricas(request):
    return render(request, 'reader/index.html', {'ferramentas': eletrica.objects.all().values(), 'tabela' : 'eletrica', 'evento' : eventos.objects.all().values()})

@login_required(login_url='login:login')
def eletronicas(request):
    return render(request, 'reader/index.html', {'ferramentas': eletronica.objects.all().values(), 'tabela' : 'eletronica', 'evento' : eventos.objects.all().values()})

@login_required(login_url='login:login')
def add(request):
    return render(request, 'reader/add.html')

@login_required(login_url='login:login')
@csrf_exempt
def save_qr_data(request):
    if request.method == "POST":
        tabela = request.POST.get("tabela")
        if tabela == "mecanica":
            ferramenta = mecanica()
        elif tabela == "eletrica":
            ferramenta = eletrica()
        else:
            ferramenta = eletronica()

        ferramenta.numero = request.POST.get("numero")
        ferramenta.nome = request.POST.get("nome")
        ferramenta.local = request.POST.get("local")
        ferramenta.instrutor = request.POST.get("instrutor")
        ferramenta.status = "off"
        ferramenta.save()
        return render(request, 'reader/add.html')

@login_required(login_url='login:login')
@csrf_exempt
def off_to_on(request):
    if request.method == "POST":
        decodetext = request.POST.get("decodetext")
        tabela = request.POST.get('tabela')
        if decodetext:
            if tabela == "mecanica":
                mecanica.objects.filter(numero=decodetext).update(status="on")
                return redirect('reader:mecanica')
            elif tabela == "eletrica":
                eletrica.objects.filter(numero=decodetext).update(status="on")
                return redirect('reader:eletrica')
            else:
                eletronica.objects.filter(numero=decodetext).update(status="on")
                return redirect('reader:eletronica')

@login_required(login_url='login:login')
def reset(request, tabela):
    print(tabela)
    if tabela == "mecanica":
        mecanica.objects.filter(status="on").update(status="off")
        return redirect('reader:mecanica')
    elif tabela == "eletrica":
        eletrica.objects.filter(status="on").update(status="off")
        return redirect('reader:eletrica')
    else:
        eletronica.objects.filter(status="on").update(status="off")
        return redirect('reader:eletronica')

@login_required(login_url='login:login')
@csrf_exempt
def delete_line(request):
    if request.method == 'POST':
        tabela = request.POST.get('tabela')
        dbline_id = request.POST.get('dbline')
        if tabela == "mecanica":
            mecanica.objects.filter(numero=dbline_id).delete()
            return render(request, 'reader/index.html', {'ferramentas': mecanica.objects.all().values(), 'tabela' : 'mecanica', 'evento' : eventos.objects.all().values()})
        elif tabela == "eletrica":
            eletrica.objects.filter(numero=dbline_id).delete()
            return render(request, 'reader/index.html', {'ferramentas': eletrica.objects.all().values(), 'tabela' : 'eletrica', 'evento' : eventos.objects.all().values()})
        else:
            eletronica.objects.filter(numero=dbline_id).delete()
            print(dbline_id)
            return render(request, 'reader/index.html', {'ferramentas': eletronica.objects.all().values(), 'tabela' : 'eletronica', 'evento' : eventos.objects.all().values()})
        
@login_required(login_url='login:login')
@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        evento = eventos()
        evento.username = request.user.username
        evento.data = request.POST.get('data')
        evento.evento = request.POST.get('evento')
        evento.save()

        return redirect('reader:mecanica')

def user_logout(request):
    logout(request)
    return redirect('login:login')