// ##########################################################################
// Author: Mahla Nasrollahi
// Last Updated: 11/03/2021
// File Name: ajax_generate_qrcode.js
//
// This program is called when the user clicks on the "Book Now" button in
// index.php file. This file captures all the input data by their ID's assigned
// to them and sends them to generate_qr_code.php file to add them to a QR code.
// ############################################################################

$(document).ready(function() {
  $("#form").submit(function(){
    $.ajax({
      url:'generate_qrcode.php',
      type:'POST',
      data: {name:$("#name").val(),
             email:$("#email").val(),
             ticket_type:$("#ticket_type").val(),
             interests:$("#interests").val()
             }
    });
  });
});
