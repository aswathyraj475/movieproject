from django.shortcuts import render
from film.models import Film
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from film.forms import filmform

# def home(request):
#         k = Film.objects.all()
#         return render(request, 'home.html', {'b': k})

class movielistview(ListView):
    model=Film
    template_name="home.html"
    context_object_name="b"

# def add(request):
#     if (request.method == "POST"):
#         n = request.POST['n']
#         d = request.POST['d']
#         c = request.FILES['c']
#         b = Film.objects.create(name=n, desc=d,cover=c)
#         b.save()
#         return home(request)
#     return render(request,'add.html')

class createview(CreateView):
    model=Film
    template_name="add.html"
    fields=['name','desc','cover']
    success_url=reverse_lazy('home')

# def view_cinema(request,p):
#     b=Film.objects.get(id=p)
#     return render(request,'view.html',{'b':b})

class detailview(DetailView):
    model=Film
    template_name="view.html"
    context_object_name="b"

# def update_movie(request,p):
#     film= Film.objects.get(id=p)
#     form = filmform(instance=film)
#     if (request.method == "POST"):
#         form = filmform(request.POST, request.FILES, instance=film)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request, 'update.html', {'form': form})
#
class updateview(UpdateView):
    model=Film
    template_name="update.html"
    fields=['name','desc','cover']
    success_url=reverse_lazy('home')

# def delete_movie(request,p):
#     if (request.method == "POST"):
#         film = Film.objects.get(id=p)
#         film.delete()
#         return home(request)
#     return render(request,'delete.html')

class deleteview(DeleteView):
    model=Film
    template_name="delete.html"
    success_url=reverse_lazy('home')



