from django.shortcuts import render
# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Movie

# movie list view
class MovieList(ListView):
    model = Movie
    paginate_by = 10
    template_name = 'movie/movie_list.html'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    """Returns the URL to access a particular instance of the model."""
    def get_object(self):
        return Movie.objects.get(id=self.kwargs['pk'])
    

def search(request):
    if request.method == 'GET':
        search_text = request.GET.get('search')
        try:
            status = Movie.objects.filter(title__icontains=search_text)
            print(status)
            return render(request, 'movie/search.html', {'results': status})
        except:
            return render(request, 'movie/search.html', {'results': status})

    else:
        return render(request, 'movie/search.html')