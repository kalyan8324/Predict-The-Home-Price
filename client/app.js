function getBathValues(){
    var uiBathroms = document.getElementsByName('uiBathrooms')
    for(var i in uiBathroms){
        if(uiBathroms[i].checked){
            return uiBathroms[i].value
        }
    }

}


window.onload = getBathValues