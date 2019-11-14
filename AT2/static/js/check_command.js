// 过滤敏感命令 如 rm -rf
function testRe(doc) {
    // 每个变量表示要过滤的敏感命令或者敏感词
    var rm = new RegExp("rm -rf", "g");
    var rm1 = new RegExp("中国", "g");
    var l = [rm, rm1];  // 将多个命令放到这个数组中
    var result = '';
    var result1 = '';
    var new_doc = doc;
    for (var i = 0; i < l.length; i++) {
        while ((result = l[i].exec(doc)) != null) {

            result1 += result + ' ';
            var reg = new RegExp(result, 'g');
            new_doc = new_doc.replace(reg, '<b style="color:red;font-size:22px;">' + result + '</b>');
        }

    }
    return [new_doc, result1];
}