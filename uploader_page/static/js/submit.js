let drag_drop = document.getElementById("drag-drop");
let choose_button = document.getElementById("chose-file");

let submit_button_1 = document.getElementById("submit-drag-drop");
let submit_button_2 = document.getElementById("submit-choose");


drag_drop.onchange = () => {submit_execution(submit_button_1)};
choose_button.onchange = () => {submit_execution(submit_button_2)};

function submit_execution(submit_button){
    submit_button.click();
}