$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        // here 0,600,100 are screen size 0 for mobile size screen , 600 for tab size screen , 1000 for big screen
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


$('.plus-cart').click (function(){
    var id = $(this).attr('pid').toString(); //this is used for current object$(this)    
    var eml = this.parentNode.children[2]
    // console.log(id)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id : id
        },
        success: function(data) {
            // console.log(data)
            // console.log ("Success")
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})


$('.minus-cart').click (function(){
    var id = $(this).attr('pid').toString(); //this is used for current object$(this)    
    var eml = this.parentNode.children[2]
    // console.log(id)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id : id
        },
        success: function(data) {
            // console.log(data)
            // console.log ("Success")
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})


$('.remove-cart').click (function(){
    var id = $(this).attr('pid').toString(); //this is used for current object "$(this)"    
    var eml = this
    // console.log(id)
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id : id
        },
        success: function(data) {
            // console.log(data)
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})