$(document).ready(function() {
    var register_service = function(form_id){
        var service_form = $('#' + form_id);
        form_action(service_form.attr('id'), 'create');
    };

    var register_service_api = function(form_id){
        var service_api_form = $('#' + form_id);
        form_action(service_api_form.attr('id'), 'create');
    };

    var add_new_api_html = function(service_name){
        var url = get_new_api_url.replace('6969aetos_service6969', service_name);
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
        register_service($(this).data('form-id'));
    });

    $('body').on('click', '#add_new_api', function(){
        add_new_api_html('SMD');
    });

    $('body').on('click', '.register_service_api', function(){
        alert('register api')
        register_service_api($(this).data('form-id'));
    });
});