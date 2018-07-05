// CHANGING THE PAYMENT SECTION DISPLAY - CREDIT CARD OR DEPOSIT
$("#id_payment_0").on("click", function(){
      $('#payment1').css('display', 'block')
      $('#payment2').css('display', 'none')
});
$("#id_payment_1").on("click", function(){
      $('#payment2').css('display', 'block')
      $('#payment1').css('display', 'none')
});





$("#id_event_option_0").on("click", function(){
      $('#cielo_link').prop('href', 'https://cieloecommerce.cielo.com.br/TransactionalVNext/Checkout/Index/f0111d24-26ca-47a5-9f69-c77335892ff5')
      $('.payment_form').css('display', 'block-level')
      $('.payment').css('display', 'block')
});
$("#id_event_option_1").on("click", function(){
      $('#cielo_link').prop('href', '')
      $('.payment_form').css('display', 'block-level')
      $('.payment').css('display', 'block')
});
$("#id_event_option_2").on("click", function(){
      $('.payment_form').css('display', 'none')
      $('.payment').css('display', 'none')
      $('.cancel_terms_area').css('margin-top', '50px')
});
