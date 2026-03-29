document.addEventListener("DOMContentLoaded", () => {
  const placeholder = document.getElementById("footer-placeholder");
  if (!placeholder) return;

  fetch("/components/footer.html?v=5")
    .then((res) => res.text())
    .then((html) => {
      placeholder.innerHTML = html;
    })
    .catch((err) => {
      console.error("Footer load error:", err);
    });
});
