function loadMenu999(profile) {
    console.log('### ' + profile);
    var toks = profile.split(SPLIT_ROLE_CHAR);
    var subtoks = toks[0].split(SPLIT_PROFILE_CHAR);
    var p = subtoks[0]+SPLIT_PROFILE_CHAR+subtoks[1];
    $.getJSON("json/maps/menumap.json", function(data) {
    }).done(function(data){
        $.each(data.map, function(i, item) {
            console.log('# '+p, item.profile);
            if(p === item.profile) {
                $("#menudiv").load("menus/"+item.profile+"/"+item.profile+".php",{
                    role:toks[1],
                    profile:item.profile
                }, function() {
                    $('#menudiv').css({"width":"70rem","height":"2.2rem","display":"block"});
                });
            }
        });
    });
    return false;
}