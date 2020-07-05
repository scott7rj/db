function searchUsuario999() {
    document.getElementById('thirddiv').innerHTML = '';
    document.getElementById('fourthdiv').innerHTML = '';
    document.getElementById('fifthdiv').innerHTML = '';
    
    $.post('db2/tds/csvmonth.php', {
        month:$("#selFilterTdsMonth option:selected").val(),
        year:$("#selFilterTdsYear option:selected").val(),
        stat:$("#selFilterTdsStat option:selected").val()
    }, function(data){
        //alert(data);
        if (data.indexOf(ERROR_TAG) >= 0) {
            alert(data);
            return false;
        }
        $('#thirddiv').html(data);
    });
    return false;
}