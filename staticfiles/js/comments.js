document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            e.preventDefault();  // Prevent the default action
            let commentId = e.target.getAttribute("comment_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            let slug = commentForm.getAttribute("data-slug");
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `/assignment/${slug}/edit_comment/${commentId}/`);
        });
    }

    // Add logging to delete button event listeners
    for (let button of deleteButtons) {
        console.log("Attaching delete event listener to button:", button);
        button.addEventListener("click", (e) => {
            e.preventDefault();  // Prevent the default action
            let commentId = e.target.getAttribute("comment_id");
            console.log("Delete button clicked, comment_id:", commentId);
            let slug = commentForm.getAttribute("data-slug");
            deleteConfirm.href = `/assignment/${slug}/delete_comment/${commentId}/`;
            console.log("Delete confirmation link set to:", deleteConfirm.href);
            deleteModal.show();
        });
    }
});
