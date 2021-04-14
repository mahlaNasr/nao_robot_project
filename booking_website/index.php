<!DOCTYPE html>
<!-- To access the page: http://192.168.64.2/eep/index.php -->

<html lang="en" dir="ltr">
    <head>
        <meta charset="UTF-8">
        <title>Booking a Ticket</title>
        <!-- Import all the external links and the scripts -->
        <?php include('extras/header.php'); ?>
  </head>

  <body>

    <!-- Import the navigation bar and other body parts -->
    <?php include('extras/body_nav.php'); ?>


    <div class="main top-bar-sm tnew-content">
        <div class="container">

        <!-- END INJECTED HEADER -->
        <nav class="tn-subnav-component">
          <div style="clear: both;"></div>
        </nav>

        <main class="tn-events-detail-page" >
            <div>
                <div class="tn-event-detail__main-container">
                    <div>
                        <h2>Conversations with God</h2>
                        <h1><b>Jan Matejko’s Copernicus</b></h1><br/>
                    </div>

                    <!-- FORM -->
                    <form action="extras/confirmation.php" class="form-horizontal tn-ticket-selector form-signin" method="POST" id="form">
            						<div>
            								<!-- NAME -->
            								<div>
            										<ul class="list-unstyled form-group">
            												<label class="control-label">Name</label>
            												<div>
            														<input class="form-control width" id="name" name="name" type="text" placeholder="Name" required="required">
            												</div>
            										</ul><br/>
            								</div>

            								<!-- Email -->
            								<div>
            										<ul class="list-unstyled form-group">
            												<label class="control-label">Email</label>
            												<div>
            														<input class="form-control width" id="email" name="email" type="email" placeholder="Email address" required="required">
            												</div>
            										</ul><br/>
            								</div>


            								<!-- Membership Type -->
            								<div>
            										<ul class="list-unstyled form-group">
            												<li class="ng-spacer"></li>
            												<label class="control-label">Ticket Type</label>
            												<div>
            													<select class="form-control css-sel" id="ticket_type" name="ticket_type" required="required">
                                        <option value="">Choose a ticket type</option>
                                        <option value="Member">Member</option>
                                        <option value="Standard + Variety of Donation Options">Standard + Variety of Donation Options</option>
                                        <option  value="Standard + Free">Standard + Free</option>
                                        <option value="Standard + Under 13 for free">Standard + Under 13 for free</option>
            													</select>
            												</div>
            										</ul><br/>
            								</div>


            								<!-- Interests -->
            								<div>
            										<ul class="list-unstyled form-group">
            												<li class="ng-spacer"></li><li class="tn-ticket-selector__pricetype-list-item">
            														<label class="control-label">Choose an Interest</label>
            														<div>
            																<select class="form-control css-sel" id="interests" name="interests" required="required">
            																		<option value="">Choose an option</option>
            																		<option value="Artist">About the the Artist</option>
            																		<option value="History">History of the Artist/Art</option>
            																		<option value="Culture">About the Culture</option>
            																</select>
            														</div>
                                      </li>
            										</ul><br/>
            								</div>

            						</div>

            						<div class="row button-row">
            								<div class="col-12 text-right">
            										<input name="submit" id="submit" class="btn btn-next btn-primary btn-primary-blue" type="submit" value="Book Now" />
            								</div>
            						</div>
            				</form>
                </div>
            </div>
        </main>
    </div>


    <!-- jQuery for getting data for QR code -->
    <script src="input_variables.js"></script>



    <?php include('extras/footer.php'); ?>


  </body>
</html>
