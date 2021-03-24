function toggleElement(e,d) {
    var x = document.getElementById(e);
    if (x.style.display === d)
        x.style.display = "none";
    else
        x.style.display = d;
}