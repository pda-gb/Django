// скрипт перехода по ссылке объекта
// кроме кнопки перехода для редактирования объекта link-edit
window.onload = function () {
    $("tr[data-href]:not(.link-edit)").on("click", function () {
        document.location = $(this).data('href');
        console.log($(this).data('href'));
    });
};
