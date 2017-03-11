$(document).ready(function() {
    var register_service = function(form_id){
        var service_form = $('#' + form_id);
        form_action(service_form.attr('id'), 'create');
    };

    var save_service = function(form_id){
        service_form = $('#' + form_id);
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

    var get_service_name = function(form_id){
        dev_form_id = form_id
        var form_data = serialize_form(form_id, 'json');
        return form_data.name
    };


    $('body').on('click', '#register_service', function(){
        register_service($(this).data('form-id'));
    });

    $('body').on('click', '#save_service', function(){
        save_service($(this).data('form-id'));
    });

    $('body').on('click', '#add_new_api', function(){
        var service_name = get_service_name($(this).data('form-id'));
        add_new_api_html(service_name);
    });

    $('body').on('click', '.register_service_api', function(){
        register_service_api($(this).data('form-id'));
    });
});