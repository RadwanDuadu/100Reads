/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific review.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
console.log("reviews.js loaded");

document.addEventListener("DOMContentLoaded", () => {
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteConfirm = document.getElementById("deleteConfirm");
  const deleteButtons = document.querySelectorAll(".reviews .btn-delete");

  deleteButtons.forEach(button => {
  console.log("Found button with data-review-id:", button.dataset.reviewId);
  });

  deleteButtons.forEach(button => {
    button.addEventListener("click", e => {
      e.preventDefault();

      // const reviewId = button.dataset.reviewId;
      let reviewId = e.target.getAttribute("review_id");
      if (!reviewId) {
        console.error("No review ID found!");
        return;
      }

      let deleteUrl;

      if (window.location.pathname.includes("/moderator/")) {
        // Moderator dashboard delete
        deleteUrl = `/moderator/dashboard/delete_review/${reviewId}`;
      } else {
        // Book detail page delete
        // Get the slug from the current URL dynamically
        // e.g., /the-complete-sherlock-holmes/ → slug = 'the-complete-sherlock-holmes'
        const pathParts = window.location.pathname.split("/").filter(Boolean);
        const slug = pathParts[0]; // first part is the book slug
        deleteUrl = `/${slug}/delete_review/${reviewId}/`;
      }

      deleteConfirm.setAttribute("href", deleteUrl);
      deleteModal.show();
    });
  });
});
