//Загрузка страницы
$(onLoad); function  onLoad() {

  var  $button  =  $ ( '.button' );

}

//Элементы управления
$(function () {

    var $from = $('.from');
    var $to =$('.to');
    var $fun =$('.fun');
    var $graph =$('.graph');
    var $button =$('.button');
    // var $button2 =$('.button2');

   $button.click(function(e)
    {
        //Отмена действия по умолчанию
        e.preventDefault();
        //Получение значений из полей ввода(преобразованные из строк в числа)
        var from = parseFloat($from.val());
        var to = parseFloat($to.val());
        var fun = ($fun.val());
        //Создание массива точек
        const points = [];
        for(var x = from; x<= to; x += 0.01 )
            points.push([x, eval(fun)]);
        //Вывод легенды
        $.plot($graph, [{ label: fun, data: points }], [points], {});
    });

});