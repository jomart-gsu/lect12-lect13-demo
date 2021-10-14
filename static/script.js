window.onload = () => {
    document.getElementById("myCoolButton").addEventListener(
        'click', () => {
            console.log("Button was clicked");
            document.getElementById("flashes").style.color = "red";
        })
}

function validateForm() {
    let val = document.forms[0].elements[0].value;
    if (val === "jmartin191") {
        return true; 
    }
    console.log("Wrong value entered")
    return false;
}