Url = {
    get(){
        var vars= {};
        if(window.location.search.length!==0)
            window.location.search.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value){
                key=decodeURIComponent(key);
                if(typeof vars[key]==="undefined") {vars[key]= decodeURIComponent(value);}
                else {vars[key]= [].concat(vars[key], decodeURIComponent(value));}
            });
        return vars;
    }
};
$(document).ready(function(){
    if(Url.get('error').error == 'exceded'){
        $('#error').append('<em>Error:</em> 3 works in progress! Wait...')
        $('#error').show()
    }
});


$(".btn-play").click(function(){
    $.get( "play", { id: $(this).attr('id') },function(data){
        if(data['status'] == "3"){
            window.location.href="/?error=exceded";
        }else window.location.href="/";
    } );


});
