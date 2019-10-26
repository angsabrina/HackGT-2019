$('#myFormSubmit').click(function (e) {
    var formdata = new FormData()
    formdata.append('photo',$('#inputimage')[0].files[0])
    $.ajax({
        method : 'POST',
        processData : false,
        contentType : false,
        url : 'http://localhost:3000/home',
        data : formdata,
        success : function(o){
            //callback here on success
        },
        error : function(e){
            //callback here on error
        }
    })
});