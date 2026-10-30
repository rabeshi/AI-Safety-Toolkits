// Filters the "All resources" table on the toolkit catalogue page as you type.
document.addEventListener("DOMContentLoaded", function () {
  var input = document.getElementById("toolkit-filter");
  if (!input) return;
  // The table to filter is the first one that comes after the search box.
  var table = Array.prototype.find.call(document.querySelectorAll(".md-typeset table"), function (t) {
    return input.compareDocumentPosition(t) & Node.DOCUMENT_POSITION_FOLLOWING;
  });
  if (!table) return;
  input.addEventListener("input", function () {
    var terms = input.value.toLowerCase().split(/\s+/).filter(Boolean);
    table.querySelectorAll("tbody tr").forEach(function (row) {
      var text = row.textContent.toLowerCase();
      row.style.display = terms.every(function (t) { return text.indexOf(t) !== -1; }) ? "" : "none";
    });
  });
});
