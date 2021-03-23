// https://sumtips.com/snippets/javascript/tab-in-textarea/

function customKeyEvents(o, e)
{		
    var kC = e.keyCode ? e.keyCode : e.charCode ? e.charCode : e.which;
    // Tab
    if (kC == 9 && !e.shiftKey && !e.ctrlKey && !e.altKey)
    {
        var oS = o.scrollTop;
        if (o.setSelectionRange)
        {
            var sS = o.selectionStart;	
            var sE = o.selectionEnd;
            o.value = o.value.substring(0, sS) + "\t" + o.value.substr(sE);
            o.setSelectionRange(sS + 1, sS + 1);
            o.focus();
        }
        else if (o.createTextRange)
        {
            document.selection.createRange().text = "\t";
            e.returnValue = false;
        }
        o.scrollTop = oS;
        if (e.preventDefault)
        {
            e.preventDefault();
        }
        return false;
    }
    // Enter
    else if (kC == 13 && !e.shiftKey && e.ctrlKey && !e.altKey)
    {
        document.codeForm.submit();
        return false;
    }
    return true;
}