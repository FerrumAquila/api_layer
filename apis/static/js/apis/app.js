$(document).ready(function() {
    var register_api = function(form_id){
        var api_form = $('#' + form_id);
        form_action(api_form.attr('id'), 'create');
    };

    var save_api = function(form_id){
        api_form = $('#' + form_id);
        form_action(api_form.attr('id'), 'create');

        end_point_cards = $('.card.api')
        $.each(end_point_cards, function(i){
            var end_point_card = end_point_cards.eq(i);
            var end_point_form = end_point_card.children('.card-body').children('.form').children();
            register_end_point(end_point_form.attr('id'));
        })
    };

    var register_end_point = function(form_id){
        var end_point_form = $('#' + form_id);
        form_action(end_point_form.attr('id'), 'create');
    };

    var remove_end_point = function(form_id){
        var end_point_form = $('#' + form_id);
        form_action(end_point_form.attr('id'), 'remove');
    };

    var add_new_api_html = function(api_name){
        var url = get_new_end_point_url.replace('6969aetos_api6969', api_name);
        console.log(url)
        $.get(url, function(response){
            if($('.card.api').length){
                $('.card.api').last().after(response);
            }else{
                $('.card.api').last().after(response);
            }
        });
        var api = $('.card.api').last();
    };

    var get_api_name = function(form_id){
        dev_form_id = form_id
        var form_data = serialize_form(form_id, 'json');
        return form_data.name
    };


    $('body').on('click', '#register_api', function(){
        register_api($(this).data('form-id'));
    });

    $('body').on('click', '#save_api', function(){
        save_api($(this).data('form-id'));
    });

    $('body').on('click', '#add_new_api', function(){
        var api_name = get_api_name($(this).data('form-id'));
        add_new_api_html(api_name);
    });

    $('body').on('click', '.register_end_point', function(){
        register_end_point($(this).data('form-id'));
    });

    $('body').on('click', '.remove_end_point', function(){
        remove_end_point($(this).data('form-id'));
    });
});