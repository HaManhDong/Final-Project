'use strict';

$('.pas-sidebar-element').each(function (index) {
    $(this).on('click', function () {
        if (!$(this).hasClass('active')) {
            $('ul.sidebar-menu li.pas-sidebar-element.active').removeClass('active');
            $(this).addClass('active');
        }
    })
});

var create_datatables_info = function (selector, data, columns) {
    return $('#' + selector).DataTable({
        data: data,
        columns: columns
    });
};

