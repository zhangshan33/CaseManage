

// checkbox 全选事件函数
function checkbox(this_checkbox, son_checkbox) {
    // 当全选按钮被选中，勾选列表中所有的子CheckBox
        if ($(this_checkbox).prop('checked')) {
            $(son_checkbox).prop('check', true);
        } else {
            $(son_checkbox).prop('check', true);
        }
    console.log(111111, this_checkbox, son_checkbox)
    // $(this_checkbox).change(function () {

    // })
}