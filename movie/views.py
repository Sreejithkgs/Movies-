from django.shortcuts import render
from movie.models import Movie
# from movie.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# def home(request):
#     m=Movie.objects.all()
    # return render(request,'home.html',{'m':m})

class homeview(ListView):
    model=Movie
    template_name="home.html"
    context_object_name='m'

# def addmovie(request):
    # if(request.method=='POST'):
    #     a=request.POST['a']
    #     b=request.POST['b']
    #     c=request.POST['c']
    #
    #     d=request.FILES['d']
    #     p=Movie.objects.create(name=a,desc=b,year=c,image=d)
    #     p.save()
    #     return home(request)
    # return render(request,'addmovie.html')

    # if (request.method=="POST"):
    #     form=movieform(request.POST,request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return home(request)
    #
    # form=movieform()
    # return render(request,'addmovie.html',{'form':form})

class addmovies(CreateView):
    model=Movie
    template_name="addmovie.html"
    fields=['name','desc','year','image']
    success_url = reverse_lazy('movie:home')


# def detail(request,n):
#     b=Movie.objects.get(id=n)
#     return render(request,'details.html',{'b':b})

class detail(DetailView):
    model=Movie
    template_name="details.html"
    context_object_name="b"


# def delete(request,n):
#     b=Movie.objects.get(id=n)
#     b.delete()
#     return home(request)

class delete(DeleteView):
    model=Movie
    template_name='delete.html'
    success_url = reverse_lazy('movie:home')


# def edit(request,n):
#     b=Movie.objects.get(id=n)
#     if(request.method=="POST"):
#         form=movieform(request.POST,request.FILES,instance=b)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form=movieform(instance=b)
#     return render(request,'edit.html',{'form':form})

class update(UpdateView):
    model=Movie
    template_name='edit.html'
    fields = ['name','desc','year','image']
    success_url = reverse_lazy('movie:home')

