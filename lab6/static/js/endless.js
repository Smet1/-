// Загрузка элементов
function loadBanks(pageNumber) {
    csrf_token = '{{ csrf_token }}';

    // Показываем загрузку
    $("#bank-cards").append("<p id=\"progress\" style=\"text-align: center;\n\">🔎 Loading..</p>");

    $.ajax({
        url: 'page=' + pageNumber,
        type: 'GET',
        headers: {'X-CSRFToken': csrf_token},
        success: function (response) {
            // Удаляем загрузку
            $('#progress').remove()

            // Добавляем новую порцию элементов
            var rows = $(response).find('#row')
            $('#bank-cards').append(rows);
        },
        error: function (response) {
            console.log('Error with response: ' + response) // ошибка загрузки порции
        }
    });
}