from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def landing(request):
    return render(request, 'main/index.html')


class BanksDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'


class BanksUpdateView(UpdateView):
    model = Articles
    template_name = 'main/create.html'
    form_class = ArticlesForm


class BanksDeleteView(DeleteView):
    model = Articles
    success_url = '/banking'
    template_name = 'main/banks_delete.html'


def calc(request):
    return render(request, 'main/calculator.html')


def bank(request):
    banks = Articles.objects.all()
    return render(request, 'main/bank.html', {'banks': banks})


# ошибка из за data
#     error = ''
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('banking')
#         else:
#             error = "Wrong Form"
#
#     banks = Articles.objects.all()
#     form = ArticlesForm()
#
#     data = {
#         'form': form,
#         'error': error
#     }

def create(request):
    error = ' '
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Wrong Form'

    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'main/create.html', data)
