from django.shortcuts import render, redirect
from .models import Word
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return render(request, 'vocabulario_app/global/index.html')

def create_vocabulary(request):
    if request.method == 'GET':
        return render(request, 'vocabulario_app/pages/create_vocabulary.html')
    
    if request.method == 'POST':
        vocabulo = request.POST.get('vocabulo')
        significado = request.POST.get('significado')
        exemplo = request.POST.get('exemplo')
        frequencia = request.POST.get('frequencia')
        print(vocabulo, significado, exemplo, frequencia)

        if not all([vocabulo, significado, exemplo, frequencia]):
            messages.error(request, "Preencha todos os campos.")
            return render(request, 'vocabulario_app/pages/create_vocabulary.html')
    
        new_word = Word.objects.create(vocabulo=vocabulo, significado=significado, exemplo=exemplo, frequencia=frequencia)
        # new_word = Word(vocabulo=vocabulo, significado=significado, exemplo=exemplo, frequencia=frequencia)
        # new_word.save()
        messages.success(request, f'Palavra: {vocabulo} cadastrada com sucesso')
        return redirect('create_vocabulary')  # evita reenvio de formulário ao recarregar
        #não fazer return no post: intencional no padrão Post/Redirect/Get (PRG)
        #evitar que o formulário seja reenviado se o usuário atualizar a página após um POST
        #return render(request, 'vocabulario_app/pages/create_vocabulary.html', context={'word': new_word})

def list_vocabulary(request):
    words = Word.objects.all().order_by('vocabulo')#('created_at')

    paginator = Paginator(words, 2)  # itens por página

    page_number = request.GET.get('page')
    word_count = paginator.get_page(page_number)

    return render(request, 'vocabulario_app/pages/list_vocabulary.html', context={'words': words, 'count': word_count})

# @require_POST
def  delete_vocabulary(request,id):
    #word_found = get_object_or_404(Word, id=id)
    #Evita necessidade de try/except para o caso da palavra não existir.
    word_found = Word.objects.get(id=id)
    try:
        word_found.delete()
        messages.success(request, f"Palavra: {word_found.vocabulo} deletada com sucesso!")
    # except Word.DoesNotExist:
    #     messages.error(request, f"Palavra: {word_found.vocabulo} não encontrada!")
    # except Word.MultipleObjectsReturned:
    #     messages.error(request, f"Palavra: {word_found.vocabulo} não encontrada!")
    # except Exception:
    #     messages.error(request, f"Erro ao deletar palavra: {word_found.vocabulo}")
    except Exception as e:
        messages.error(request, f"Erro ao deletar palavra: {word_found.vocabulo}. Detalhes: {str(e)}")
   
        
    return redirect('list_vocabulary')

def update_vocabulary(request, id):
    if request.method == 'GET':
        word_found = Word.objects.get(id=id)
        return render(request, 'vocabulario_app/pages/update_vocabulary.html', context={'found': word_found})
    
    if request.method == 'POST':
        vocabulo = request.POST.get('vocabulo')
        significado = request.POST.get('significado')
        exemplo = request.POST.get('exemplo')
        frequencia = request.POST.get('frequencia')

    Word.objects.filter(id=id).update(
            vocabulo=vocabulo,significado=significado,exemplo=exemplo,frequencia=frequencia
            )
    messages.success(request, f"Dados da palavra: {vocabulo}")
    return redirect('list_vocabulary')