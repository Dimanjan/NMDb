from .forms import CommentForm
from django.shortcuts import get_object_or_404, render
# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Movie

# movie list view
class MovieList(ListView):
    model = Movie
    paginate_by = 10
    template_name = 'movie/movie_list.html'


def MovieDetail(request, pk):
    template_name = 'movie/movie_detail.html'
    movie=get_object_or_404(Movie, pk=pk)
    comments=movie.comments.filter(active=True)
    new_comment=None
    # Comment posted
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current movie to the comment
            new_comment.movie = movie
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, 
                    {'movie': movie,
                    'comments': comments,
                    'new_comment': new_comment,
                    'comment_form': CommentForm()})


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