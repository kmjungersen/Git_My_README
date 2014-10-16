/**
 * Created by kurtisjungersen on 10/16/14.
 */

$(function() {

    var input_content = $( "input_field").val();

        $.ajax({
            type: "POST",
            url: "/input",
            data: input_content,
        });

    }
);