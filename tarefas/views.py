from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ClienteForm
from django.contrib import messages


from .models import Cliente

@login_required
def listaCliente(request):

    search = request.GET.get('search')

    if search:

        cliente = Cliente.objects.filter(Nome_icontains=search, user=request.user)

    else:

        clientes_lista = Cliente.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(clientes_lista, 3)

        page = request.GET.get('page')

        tarefas = paginator.get_page(page)

    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

@login_required
def clienteView(request, id):
    tarefas = get_object_or_404(Cliente, pk=id)
    return render(request, 'tarefas/cliente.html', {'tarefas': tarefas})


@login_required
def novocliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            Cliente = form.save(commit=False)
            Cliente.Feito = 'Fazendo'
            Cliente.user = request.user
            Cliente.save()
            return redirect('/')
    else:
        form = ClienteForm()
        return render(request, 'tarefas/addcliente.html', {'form': form})


@login_required
def editcliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)

    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)

        if(form.is_valid()):
            cliente.save()
            return redirect('/')
        else:
            return render(request, 'tarefas/editcliente.html', {'form': form, 'cliente': cliente})
    
    else:
        return render(request, 'tarefas/editcliente.html', {'form': form, 'cliente': cliente})

@login_required
def deletecliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()

    messages.info(request, 'CLIENTE DELETADO COM SUCESSO!')

    return redirect('/')
@login_required
def helloWorld(request):
    return HttpResponse('hello world')

@login_required
def seunome(request, name):
    return render(request, 'tarefas/seunome.html', {'name': name})