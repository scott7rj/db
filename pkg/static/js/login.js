function menuteste999() {
    setInitialLayout999();
    console.log(processSpecialChars($('#txtId').val().toUpperCase()), $('#txtPwd').val());
    $.post('menu',{
        txtId:processSpecialChars($('#txtId').val().toUpperCase()),
        txtPwd:$('#txtPwd').val()
    }, function(data){
        console.log('------->'+data);
        if (isError999(data)) {
            return;
        }
        $('#menudiv').css({"width":"50rem","height":"3rem","display":"block"});
        $("#menudiv").html(data);
    });
    return false;
}

function login999() {
    setInitialLayout999();
    //console.log(processSpecialChars($('#txtId').val().toUpperCase()), $('#txtPwd').val().toUpperCase());
    $.post('login/',{
            txtId:processSpecialChars($('#txtId').val().toUpperCase()),
            txtPwd:$('#txtPwd').val()
        }, function(data){
            if (isError999(data)) {
            	$('#txtId').val('');
                $('#txtPwd').val('');
                $('#txtId').focus();
            	return;
        	}
            var json = $.parseJSON(data);
            if (isError999(json)) {
            	$('#txtId').val('');
                $('#txtPwd').val('');
                $('#txtId').focus();
            	return;
        	}
            sessionStorage.setItem('currentIdUser', json[0].id_user);
            sessionStorage.setItem('currentProfile', json[0].profile);
            sessionStorage.setItem('currentNmUser', json[0].nm_user);
            
            $('#txtId').val('');
            $('#txtPwd').val('');
            loadMenu999(json[0].profile);
            $('#sessiondiv').append("<p id='sessionIdUser'>"+sessionStorage.getItem('currentIdUser')+" - "+sessionStorage.getItem('currentNmUser')+
                "</p>").css("color","white");
            
    });
}
function logoff999() {
    $( "#menudiv" ).html('');
    $( "#sessiondiv" ).html('');
    sessionStorage.setItem('currentUserId', null);
    setInitialLayout999();
	$('#txtId').val('');
	$('#txtPwd').val('');
    $('#txtId').focus();
}