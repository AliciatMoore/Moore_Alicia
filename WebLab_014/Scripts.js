/*Second Method...
function validate(){
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    //need...username@web.extension
    //if the following...
        //@ is not in the string (return neg value)
        //@ is in the wrong place
        //there is no .com or other extensions
        //final dot in the right place

    var y = document.forms.input.password.value;

    if((atPos < 1|| dotPos < atPos + 2|| dotPos + 2 > x.length) && y.length < 6)
        alert("We were unable to process your request. Please check the following errors...This is not a valid email address. Your password does not meet the minimum requirements.");
    else if(atPos < 1|| dotPos < atPos + 2|| dotPos + 2 > x.length)
        alert("We were unable to process your request. Please check the following errors...This is not a valid email address.");
    else if(y.length < 6)
        alert("We were unable to process your request. Please check the following errors...Your password does not meet the minimum requirements.");
    else
        alert("Success!");
}*/
function validate(){
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    if(atPos < 1|| dotPos < atPos + 2|| dotPos + 2 > x.length)
        return "wrong";
    else
        return "right";
}

function validatey(){
    var y = document.forms.input.password.value;

    if(y.length < 6)
        return "wrong";
    else
        return "right";
}

function check(){
    if (validate() == "wrong" && validatey() == "wrong")
        alert("We were unable to process your request. Please check the following errors...This is not a valid email address. Your password does not meet the minimum requirements.");
    else if(validate() == "wrong")
        alert("We were unable to process your request. Please check the following errors...This is not a valid email address.");
    else if(validatey() == "wrong")
    alert("We were unable to process your request. Please check the following errors...Your password does not meet the minimum requirements.");
    else 
        alert("Success!");
    
}
