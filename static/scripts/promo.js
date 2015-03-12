/* Promo page specific JS fucntions */

function onReferralURLClick() {
    var ref_url = document.getElementById('referral_display').value;
    window.prompt("Copy to clipboard: Ctrl+C, Enter", ref_url);
}

function showEmailList() {
    var email_list = document.getElementById('emailList')
    var show_email_button = document.getElementById('showEmailButton')

    // Toggle the visibility of the list and the text of the button
    if ( email_list.style.display == 'block') {
        show_email_button.value = 'Show Email List';
        email_list.style.display = 'none';
    } else {
        show_email_button.value = 'Hide Email List';
        email_list.style.display = 'block';
    }
}