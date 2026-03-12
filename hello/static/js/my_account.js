function editProfile(){
    document.getElementById("nameText").classList.add("d-none");
    document.getElementById("emailText").classList.add("d-none");
    document.getElementById("phoneText").classList.add("d-none");


    document.getElementById("nameInput").classList.remove("d-none");
    document.getElementById("emailInput").classList.remove("d-none");
    document.getElementById("phoneInput").classList.remove("d-none");

    document.getElementById("editBtn").classList.add("d-none");
document.getElementById("saveBtn").classList.remove("d-none");
}