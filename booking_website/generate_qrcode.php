<!-- ##########################################################################
Author: Mahla Nasrollahi
Last Updated: 11/03/2021
File Name: generate_qr_code.php

This prgram reads the user inputs from HTML form in index.php and inserts them
into a unique QR code. The data inside the QR code is then saved to a Json file
for the robot to access and read the data.
############################################################################-->

<?php

  if(isset($_POST) && !empty($_POST)) {

    // Import the external qrcode library for php
    include('library/phpqrcode/qrlib.php');

    // This a location where generated QR code is to be stored
    $qrcode_file_path = dirname(__FILE__).DIRECTORY_SEPARATOR.'images'.DIRECTORY_SEPARATOR;

    // If directory is not created then create a new directory
    if(!file_exists($qrcode_file_path)){
        mkdir($qrcode_file_path);
    }

    // Set a secure random file name of each generated QR code image
    $filename	= $qrcode_file_path.md5(uniqid()).'.png';

    // Capture the HTML form data into variables

    $name = $_POST['name'];
    $email = $_POST['email'];
    $ticket_type = $_POST['ticket_type'];
    $interests = $_POST['interests'];

    // Store all data into an array
    $arr_data = [
      'Name' => $name,
      'Email' => $email,
      'Ticket_type' => $ticket_type,
      'Interest' => $interests
    ];

    // Put the array data into a json file
    $qrcode_data = json_encode($arr_data, JSON_PRETTY_PRINT);
    // QR code properties
    $qrcode_level = 'M';
    $qrcode_size = 5;
    $qrcode_margin = 3;

    // Generate the QR code for a user
    //      png($text, $outfile=false, $level=QR_ECLEVEL_L, $size, $margin, $saveandprint=false)
    QRcode::png($qrcode_data, $filename, $qrcode_level, $qrcode_size, $qrcode_margin);
  }
  else {
        header('location:./');
  }
?>
