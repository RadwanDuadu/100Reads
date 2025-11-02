from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Avg
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Review
from .forms import ReviewForm


class BookList(generic.ListView):
    """Display paginated list of all books."""
    queryset = Book.objects.all()
    template_name = "library/index.html"
    paginate_by = 6


def book_detail(request, slug):
    """
    Display a single book and its reviews, with pagination and review form.
    """
    book = get_object_or_404(Book, slug=slug)
    reviews = book.Reviews.all().order_by("-created_on")

    review_count = book.Reviews.filter(approved=True).count()
    average_rating = round(
        book.Reviews.filter(approved=True).aggregate(
            avg=Avg("rating"))["avg"] or 0
    )

    paginator = Paginator(reviews, 4)
    page = request.GET.get("page", 1)
    page_obj = paginator.get_page(page)

    # --- Detect editing mode ---
    review_to_edit = None
    edit_id = request.GET.get("edit")
    if edit_id and request.user.is_authenticated:
        try:
            review_to_edit = Review.objects.get(
                id=edit_id, author=request.user)
            review_form = ReviewForm(instance=review_to_edit)
        except Review.DoesNotExist:
            review_to_edit = None
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()

    # --- Handle POST (new or update) ---
    if request.method == "POST" and request.user.is_authenticated:
        review_id = request.POST.get("review_id")

        if review_id:  # Editing existing review
            review = get_object_or_404(
                    Review,
                    pk=review_id,
                    author=request.user)
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                edited_review = review_form.save(commit=False)
                edited_review.approved = False  # Require reapproval
                edited_review.save()
                messages.success(
                    request, (
                        "Your review was updated and is awaiting reapproval."
                        )
                )
                return redirect("book_detail", slug=slug)

        else:  # Creating new review
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.author = request.user
                new_review.book = book
                new_review.save()
                messages.success(request, (
                            "Review submitted and awaiting approval."
                        )
                    )
                return redirect("book_detail", slug=slug)

    return render(
        request,
        "library/book_detail.html",
        {
            "book": book,
            "reviews": page_obj.object_list,
            "page_obj": page_obj,
            "review_count": review_count,
            "review_form": review_form,
            "review_to_edit": review_to_edit,
            "average_rating": average_rating,
        },
    )


def review_delete(request, slug, review_id):
    """Delete a user's own review."""
    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own reviews!'
        )

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


def is_moderator(user):
    """Check if the user has moderator privileges."""
    return hasattr(user, 'userprofile') and user.userprofile.is_moderator


@login_required
@user_passes_test(is_moderator)
def moderator_dashboard(request):
    """Display all reviews for moderators."""
    reviews = Review.objects.all().order_by('-created_on')
    return render(request, 'moderator/dashboard.html', {'reviews': reviews})


@login_required
@user_passes_test(is_moderator)
def approve_review(request, review_id):
    """Allow moderators to approve a review."""
    review = get_object_or_404(Review, id=review_id)
    review.approved = True
    review.save()
    messages.success(request, "Review approved successfully.")
    return redirect('moderator_dashboard')


@login_required
@user_passes_test(is_moderator)
def delete_review_moderator(request, review_id):
    """Allow moderators to delete any review."""
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.success(request, "Review deleted successfully.")
    return redirect('moderator_dashboard')


@login_required
def delete_review(request, review_id):
    """Allow users to delete their own or moderator delete others' reviews."""
    review = get_object_or_404(Review, id=review_id)

    if request.user.userprofile.is_moderator or review.author == request.user:
        review.delete()
        messages.success(request, "Review deleted successfully.")
    else:
        messages.error(request, "You are not allowed to delete this review.")

    return redirect('book_detail', slug=review.book.slug)
