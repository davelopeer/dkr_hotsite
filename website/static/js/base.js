// SET THE CHILD OPTIONS IN THE EVENT SECTION TO LINK TO THE MODAL POP-UP ALERT
$(document).ready(function(){
      $('#id_event_option_1, #id_event_option_2, #id_payment_0').attr('data-toggle', 'modal')
      $('#id_event_option_1, #id_event_option_2').attr('data-target', '#childModal')
});


// CHANGING THE PAYMENT SECTION DISPLAY - CREDIT CARD OR DEPOSIT
$("#id_payment_0").on("click", function(){
      $('#payment1').css('display', 'block')
      $('#payment2').css('display', 'none')
});
$("#id_payment_1").on("click", function(){
      $('#payment2').css('display', 'block')
      $('#payment1').css('display', 'none')
});


// CHANGING THE PAYMENT SECTION DISPLAY ACCORDING TO THE EVENT CHOSED - ADULT OR KID
$("#id_event_option_0").on("click", function(){
      $('#payment-adult').css('display', 'block')
      $('#payment-child').css('display', 'none')
      $('.payment_form, .payment').css('display', 'block')
});
$("#id_event_option_1").on("click", function(){
      $('#payment-adult').css('display', 'none')
      $('#payment-child').css('display', 'block')
      $('.payment_form, .payment').css('display', 'block')
});
$("#id_event_option_2").on("click", function(){
      $('.payment_form, .payment').css('display', 'none')
      $('.cancel_terms_area').css('margin-top', '50px')
});


// PAYPAL INPUT OPENING THE SITE
$("#id_payment_international_0").on("click", function () {
  window.open("https://www.paypal.com/");
})
