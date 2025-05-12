from django.shortcuts import render, get_object_or_404, redirect

from .models import Movie, Review
from .forms import ReviewForm
from .utils import predict_rating
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'reviews/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.order_by('-created_at')
    return render(request, 'reviews/movie_detail.html', {'movie': movie, 'reviews': reviews})

def submit_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        if "confirm" in request.POST:
            form = ReviewForm(request.POST, show_content=False, show_rating=True)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.predicted_rating = int(request.POST["predicted_rating"])
                review.content = request.POST["content"] 
                review.save()
                return redirect("movie_detail", movie_id=movie.id)
        else:
            form = ReviewForm(request.POST, show_content=True, show_rating=False)
            if form.is_valid():
                content = form.cleaned_data["content"]
                predicted = predict_rating(content)
                return render(request, "reviews/review_confirm.html", {
                    "form": ReviewForm(initial={"user_rating": predicted}, show_content=False, show_rating=True),
                    "movie": movie,
                    "predicted_rating": predicted,
                    "content": content
                })
    else:
        form = ReviewForm(show_content=True, show_rating=False)

    return render(request, "reviews/submit_review.html", {"form": form, "movie": movie})
