function target_ADM(profile, target) {
    console.log(profile,target);
    $('#seconddiv').css({'background-color':'#CCCCCC'});
    $('#thirddiv').css({'background-color':'#CCCCCC'});
    $('#fouthdiv').css({'background-color':'#CCCCCC'});
    $('#fifthdiv').css({'background-color':'#CCCCCC'});
    $('#sixthdiv').css({'background-color':'#CCCCCC'});
    switch(target) {
        //USUARIOS
        case 'ADM-USUARIOS':
            setTwoByThreeLayout999('10rem','20rem','20rem');

            $.get("static/usuario/pesquisa.html", function( data ) {
                $('#firstdiv').html( data );
            });
            $.getScript('static/usuario/usuario.js', function(data, textStatus, jqxhr) {});
            break;
        default:
            break;
    }
}