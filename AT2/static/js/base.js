// 菜单栏点击着色
// $("#left_li").on('click', 'li', function () {
//     $(this).addClass('active').siblings().removeClass('active')
// });


$.ajaxSetup({
        data: {csrfmiddlewaretoken: '{{ csrf_token }}'}
    });