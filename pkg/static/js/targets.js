function target999(profile, target) {
    console.log(profile, target);
    $.getJSON("static/json/targetmap.json", function(data) { 
    }).done(function(data){
        clearDivs999('all');
        setDefaultLayout999();
        
        $.each(data.map, function(i, item) {
            if(profile === item.profile) {
                console.log('item.script--->'+item.script+' item.fn--->'+item.fn)
                $.getScript(item.script, function(data, textStatus, jqxhr) {
                    window[item.fn](profile,target);
                });
            }
        });
        
        
    });
    return false;
}