$('#myFormSubmit').click(function (e) {
    var formdata = new FormData()
    formdata.append('photo',$('#input-image').files[0])
    $.ajax({
        method : 'POST',
        processData : false,
        contentType : false,
        url : 'http://127.0.0.1:8000/home',
        data : formdata,
        success : function(o){
            //callback here on success
        },
        error : function(e){
            //callback here on error
        }
    })
});