document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

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
});
