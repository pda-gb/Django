// скрипт перехода для редактирования объекта
window.onload = function () {
    $('tr[data-href]').on("click", function () {
        document.location = $(this).data('href');
    });
};