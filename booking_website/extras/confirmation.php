<!DOCTYPE html>
<!-- ##########################################################################
Author: Mahla Nasrollahi
Last Updated: 11/03/2021
File Name: confirmation.php

This php file shows a message that a user has successfully booked when they
click on the "Book Now" button.
############################################################################-->

<html lang="en" dir="ltr">
  <head>
        <meta charset="UTF-8">
        <title>Booking a Ticket</title>
        <!-- Import all the external links and the scripts -->
        <?php include('header.php'); ?>
  </head>

  <body>
    <!-- Import the navigation bar and other body parts -->
    <?php include('body_nav.php'); ?>

    <div class="main top-bar-sm tnew-content">
        <div class="container">
          <div class="feedback_page">
            <?php echo "<h1>Thank you for booking.</h1>
                        <br>
                        <p>Your ticket with information will be emailed to you shortly.</p>"; ?>
          </div>
      </div>
    </div>

    <!-- Import footer section of the website -->
    <?php include('footer.php'); ?>
  </body>
</html>
