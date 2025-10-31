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
    queryset = Book.objects.all()
    book = get_object_or_404(queryset, slug=slug)

    # Get all reviews for pagination
    reviews = book.Reviews.all().order_by("-created_on")

    # Count approved reviews
    review_count = book.Reviews.filter(approved=True).count()

    # Calculate average rating from approved reviews
    average_rating = (
        book.Reviews.filter(approved=True)
        .aggregate(avg=Avg('rating'))['avg']
        or 0
    )
    average_rating = round(average_rating)

    # Pagination: 3 reviews per page
    paginator = Paginator(reviews, 3)
    page = request.GET.get("page")

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    # Handle review submission
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.book = book
            review.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Review submitted and awaiting approval'
            )
            return HttpResponseRedirect(
                reverse('book_detail', args=[slug])
            )

    review_form = ReviewForm()

    return render(
        request,
        "library/book_detail.html",
        {
            "book": book,
            "reviews": page_obj.object_list,
            "page_obj": page_obj,
            "review_count": review_count,
            "review_form": review_form,
            "average_rating": average_rating,
        },
    )


def review_edit(request, slug, review_id):
    """Edit an existing review."""
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
            messages.add_message(
                request, messages.SUCCESS, 'Review updated!'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!'
            )

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


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
