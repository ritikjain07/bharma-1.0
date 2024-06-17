const pannel = document.getElementById("mySidepannel"); 

function btn_open(){
    pannel.style.height = "600px"; 
    pannel.style.zIndex = "4"; 
}

function closeNav(){
    pannel.style.height = "0px"; 
    pannel.style.zIndex = "0"; 
}