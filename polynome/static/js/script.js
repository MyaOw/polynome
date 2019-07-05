$(document).ready( function() {
    $(".form-control").focus( function() {
        if ( $(this).val()=="0") {
            $(this).val('');
        } 
    });

    $(".form-control").blur( function() {
        if ( this.value.length == 0) {
            $(this).val('0');
        } 
    });
});