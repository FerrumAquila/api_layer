$(document).ready(function() {
    var register_service = function(){
        var service_form = $("form[id^='service']");
        form_action(service_form.attr('id'), 'create');
    };

    var add_new_api_html = function(){
        var url = get_new_api_url;
        $.get(url, function(response){
            if($('.card.api').length){
                $('.card.api').last().after(response);
            }else{
                $('.card.service').last().after(response);
            }
        });
        var api = $('.card.api').last();
    };


    $('body').on('click', '#register_service', function(){
        register_service();
    });

    $('body').on('click', '#add_new_api', function(){
        add_new_api_html();
    });
});