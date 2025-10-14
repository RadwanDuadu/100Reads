from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Review
from .forms import ReviewForm


# Create your views here.
class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "library/index.html"
    paginate_by = 6


def book_detail(request, slug):
    """
    Display an individual :model:`library.Book`.

    **Context**

    ``book``
        An instance of :model:`library.Book`.

    **Template:**

    :template:`library/book_detail.html`
    """

    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)
    reviews = book.Reviews.all().order_by("-created_on")
    review_count = book.Reviews.filter(approved=True).count()
  
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.book = book
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )

    review_form = ReviewForm()

    return render(
        request,
        "library/book_detail.html",
        {
            "book": book,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )


def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.book = book
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))