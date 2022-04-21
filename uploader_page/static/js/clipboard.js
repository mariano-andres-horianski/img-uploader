
function copy_to_clipboard(){
    let input_text = document.getElementById("url-input");
    
    navigator.clipboard.writeText(input_text.value);

}