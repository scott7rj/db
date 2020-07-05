function showMessage999(msg) {
    alert(msg);
    return false;
}
(function() {
    $(document).ready(function(){
        clearDivs999('all');
        $('#txtCode').focus();
        
        $(document).on({
             ajaxStart: function() {
                 $('body').addClass('loading');
             },
             ajaxStop: function() {
                 $('body').removeClass('loading');
             }
         });
         
         //console.log('Jquery ready...setting default layout...');
         setInitialLayout999();
         $('#txtId').focus();
         
         
         
         //login999();//DEBUG
         
         //setRawLayout999();
    });
})();
