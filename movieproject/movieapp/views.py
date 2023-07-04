from django.shortcuts import render, redirect
from movieapp.form import MovieForm
from movieapp.models import Movie


def index(request):
    movie = Movie.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def detail(request, movie_id):
    x = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'m': x})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bdesc = request.POST.get('bdesc')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie = Movie(name=name, bdesc= bdesc, desc=desc, year=year, image=image)
        movie.save()
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
