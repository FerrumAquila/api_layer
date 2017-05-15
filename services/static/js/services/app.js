$(document).ready(function() {
    var register_service = function(form_id){
        var service_form = $('#' + form_id);
        form_action(service_form.attr('id'), 'create');
    };

    var save_service = function(form_id){
        service_form = $('#' + form_id);
        form_action(service_form.attr('id'), 'create');

        service_api_cards = $('.card.api')
        $.each(service_api_cards, function(i){
            var service_api_card = service_api_cards.eq(i);
            var service_api_form = service_api_card.children('.card-body').children('.form').children();
            register_service_api(service_api_form.attr('id'));
        })
    };

    var register_service_api = function(form_id){
        var service_api_form = $('#' + form_id);
        form_action(service_api_form.attr('id'), 'create');
    };

    var remove_service_api = function(form_id){
        var service_api_form = $('#' + form_id);
        form_action(service_api_form.attr('id'), 'remove');
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
        $.getScript(function_js);
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
        json_editor = $('#' + $(this).data('form-id')).find('.json_editor');
        ace_editor = ace.edit(json_editor[0]);
        db_value = JSON.stringify(JSON.parse(ace_editor.getValue()));
        json_editor.parent('.fg-line').children('textarea').val(db_value);

        register_service_api($(this).data('form-id'));
    });

    $('body').on('click', '.remove_service_api', function(){
        remove_service_api($(this).data('form-id'));
    });
});