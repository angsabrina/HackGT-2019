$('#myFormSubmit').click(function (e) {
    var formdata = new FormData()
    var file = $('#inputimage')[0].files[0]
    formdata.append('photo',file)
    console.log(formdata)
    $.ajax({
        method : 'POST',
        processData : false,
        contentType : false,
        url : 'http://localhost:5000/test/img/upload',
        data : formdata,
        success : function(o){
            //callback here on success
        },
        error : function(e){
            //callback here on error
        }
    })
});