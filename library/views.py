from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book


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

    return render(
        request,
        "library/book_detail.html",
        {
            "book": book,
            "reviews": reviews,
            "review_count": review_count,
        },
    )
