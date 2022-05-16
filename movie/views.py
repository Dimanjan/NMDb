from .forms import ReviewForm
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
    reviews=movie.reviews.filter(active=True)
    new_review=None
    # Review posted
    if request.method == 'POST':
        # A review was posted
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            # Create Review object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current movie to the review
            new_review.movie = movie
            # Save the review to the database
            new_review.save()
    else:
        review_form = ReviewForm()

    return render(request, template_name, 
                    {'movie': movie,
                    'reviews': reviews,
                    'new_review': new_review,
                    'review_form': ReviewForm()})


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