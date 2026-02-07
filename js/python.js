function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

$(document).ready(function () {
    $('.python').each(function (index) {
        code = $(this).text();
        $(this).empty();
        buttonRun = $('<button class="btn btn-primary large">Lancer le programme</button>');
        $(this).append(buttonRun);
        buttonHide = $('<button class="btn btn-danger large">Cacher la sortie</button>');
        $(this).append(buttonHide);
        divEdit = $('<div>');
        $(this).append(divEdit)
        var editor = ace.edit(divEdit.get(0));
        editor.setTheme("ace/theme/monokai");
        editor.getSession().setMode("ace/mode/python");
        editor.setOptions({
            maxLines: Infinity
        });
        editor.renderer.setScrollMargin(10, 10);
        editor.setValue(code, 1);
        buttonRun.click(function () {
            $(this).siblings('.output').remove();
            output = $('<pre>', {
                'class': 'output'
            });
            output.appendTo($(this).closest('.python'));
            Sk.pre = output.get()[0].id;
            Sk.configure({
                output: function (text) {
                    $(output).html($(output).html() + text);
                },
                read: builtinRead
            });
            eval(Sk.importMainWithBody("<stdin>", false, editor.getValue()));
        });
        buttonHide.click(function () {
            $(this).siblings('.output').remove();
        });
    });
});
