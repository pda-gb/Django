window.onload = function () {
    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });

    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });

    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */

    // добавляем ajax-обработчик для обновления количества товара
    $('.product_jquery').on('click', 'span', function () {

        let target_href = event.target;
        let qty = $(this).parent().find('input[type="text"]'),
            val = parseInt(qty.val()),
            min = parseInt(qty.attr('min')),
            max = parseInt(qty.attr('max')),
            step = parseInt(qty.attr('step'));
        pk_name = parseInt(qty.attr('name'));

        console.log('======')
        console.log(target_href, qty, val, min, max, step)

        // дальше меняем значение количества в зависимости от нажатия кнопки
        if ($(this).is('.btn_plus')) {
            if (max && (max <= val)) {
                qty.val(max);
            } else {
                qty.val(val + step);
                val = parseInt(qty.val());
            }
        }
        if ($(this).is('.btn_minus')) {
            if (min && (min >= val)) {
                qty.val(min);
            } else if (val > 1) {
                qty.val(val - step);
                val = parseInt(qty.val());
            }
        }

        // формируем ссылку для обновления "товара-корзинки"
        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + pk_name + "/" + val + "/",

                success: function (data) {
                    // получаем обновлённый блок страницы с "товарами-корз."
                    $('.product_jquery').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

};

// // при клике на кнопки
// $( 'body' ).on( 'click', 'button.plus, button.minus', function() {
//
// 	var qty = $(this).parent().find( 'input' ),
// 	    val = parseInt( qty.val() ),
// 	    min = parseInt( qty.attr( 'min' ) ),
// 	    max = parseInt( qty.attr( 'max' ) ),
// 	    step = parseInt( qty.attr( 'step' ) );
//
// 	// дальше меняем значение количества в зависимости от нажатия кнопки
// 	if ( $( this ).is( '.plus' ) ) {
// 		if ( max && ( max <= val ) ) {
// 			qty.val( max );
// 		} else {
// 			qty.val( val + step );
// 		}
// 	} else {
// 		if ( min && ( min >= val ) ) {
// 			qty.val( min );
// 		} else if ( val > 1 ) {
// 			qty.val( val - step );
// 		}
// 	}
//
// });
//
