$(document).ready(function(){

    query_string_to_JSON = function(query_string){
        var pairs = query_string.split('&');
        var result = {};
        pairs.forEach(function(pair){
            pair = pair.split('=');
            var name = pair[0]
            var value = pair[1]
            if(name.length)
                if(result[name] !== undefined){
                    if(!result[name].push){
                        result[name] = [result[name]];
                    }
                    result[name].push(value || '');
                } else {
                    result[name] = value || '';
                }
        });
        return result;
    }

    var toggle_color = function(status_slab, toggle_color_class){
        status_slab.toggleClass(toggle_color_class);
        var color_class = status_slab.data('color-class');
        status_slab.toggleClass(color_class);
    }

    var toggle_status_slab_color = function(status_slab){
        toggle_color(status_slab, STATUS_SLAB_COLOR_CLASS);
    }

    var make_status_slab_active = function(status_slab, note_html){
        status_slab.toggleClass('inactive-container');
        status_slab.toggleClass('active-container');
        status_slab.html(note_html);
        toggle_status_slab_color(status_slab);
        increase_note_count(status_slab.data('status'));
    }

    var make_status_slab_inactive = function(status_slab){
        status_slab.toggleClass('inactive-container');
        status_slab.toggleClass('active-container');
        status_slab.html('');
        toggle_status_slab_color(status_slab);
        decrease_note_count(status_slab.data('status'));
    }

    var change_note_status = function(note, now_active_status_slab){
        toggle_color(note, now_active_status_slab.data('color-class'));
        note.data('status', now_active_status_slab.data('status'));
        note.data('color-class', now_active_status_slab.data('color-class'));
    }

    var increase_note_count = function(status){
        var summary_box = $('#summary_box_' + status);
        var note_count = parseInt(summary_box.children('h2').children('.note-count').html());
        note_count ++;
        update_note_count(status, note_count);
    }

    var decrease_note_count = function(status){
        var summary_box = $('#summary_box_' + status);
        var note_count = parseInt(summary_box.children('h2').children('.note-count').html());
        note_count --;
        update_note_count(status, note_count);
    }

    var update_note_count = function(status, note_count){
        var summary_box = $('#summary_box_' + status);
        summary_box.children('h2').children('.note-count').html(note_count);
    }

    mark_note_status = function(note_id, status){
        var note = $('#note_' + note_id);
        if(note.data('status') == status){
            alert('naughty boy\ndelivery note status is already "' + status + '"!!');
            return
        }
        var active_status_slab = note.children('.active-container');
        var note_html = active_status_slab.html();
        var inactive_status_slabs = note.children('.inactive-container');

        make_status_slab_inactive(active_status_slab);

        $.each(inactive_status_slabs, function(i){
            var inactive_status_slab = inactive_status_slabs.eq(i);
            var inactive_status = inactive_status_slab.data('status');
//            console.log("inactive_status")
//            console.log(inactive_status)
//            console.log("status")
//            console.log(status)
//            console.log("inactive_status == status")
//            console.log(inactive_status == status)
            if(inactive_status == status){
                make_status_slab_active(inactive_status_slab, note_html);
                change_note_status(note, inactive_status_slab);
            }
        });
    };

    add_note = function(data_json){
        var url = NOTE_HTML_URL;
        $.get(url, function(response){
            dev_response = response;
            console.log(response)
            $('#delivery-note-list').append(response.html);
        });
    };

});