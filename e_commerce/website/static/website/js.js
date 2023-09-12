
var shoppingCart=[]

$(document).ready(function() {
    
    function initializeComponent($component) {
        let productDict = {product_name:'',product_price:'',product_quantity:''}
        let counter = 0;
        let $incrementButton = $component.find('.addItems');
        let $decrementButton = $component.find('.subtractItems');
        let $counterDisplay = $component.find('.counterPlace');
        let $addToCartBtn = $component.find('.productAdder')
        

        $incrementButton.on('click', function() {
            counter++;
            $counterDisplay.text(counter);
            updateButtonStates();
           
        });

        $decrementButton.on('click', function() {
            if (counter > 0) {
                counter--;
                $counterDisplay.text(counter);
                updateButtonStates();
            }
        });

        $addToCartBtn.on('click', function(){
            
            
            let $productName = $component.find('.card_title')
            let $productPrice = $component.find('.priceHolder')
            let $productQuantity = $component.find('.counterPlace')
            
            productDict.product_name = $productName.text()
            productDict.product_price = $productPrice.text()
            productDict.product_quantity = $productQuantity.text()
            shoppingCart.push(productDict)
            updateLocalStorage()
            

        
            
        })

        function updateLocalStorage(){
            let arrayName = localStorage.getItem('cartData') 
            if (arrayName){
                shoppingCart=JSON.parse(arrayName)
                shoppingCart.push(productDict)
                localStorage.setItem('cartData',JSON.stringify(shoppingCart))
            }
            else{
    
                localStorage.setItem('cartData',JSON.stringify(shoppingCart))
                
            }
        }

        function updateButtonStates() {
            if (counter === 0) {
                $decrementButton.prop('disabled', true);
            } else {
                $decrementButton.prop('disabled', false);
            }
        }

        // Initialize button states
        updateButtonStates();
    }

    // Call initializeComponent for each component
    $('.card_body').each(function() {
        initializeComponent($(this));
    });
});




// load function's purpose is to execute a function after the DOM is fully loaded
window.addEventListener("load",function(){
    // The target page is the shopping cart page
        if (this.window.location.href.includes('checkout')){
            // Disable checkout button if cart is empty
                    $('.checkingOut').prop('disabled',true)
                    // retrieving cart data to display them
                shoppingCart=localStorage.getItem('cartData')
                shoppingCart=JSON.parse(shoppingCart)
                if (shoppingCart.length>0){
                    let overallTotal=0
                    $('.checkingOut').prop('disabled',false)
                    for (let i=0;i<shoppingCart.length;i++){
                        let newRow=$('<tr>')
                        let total=parseFloat(shoppingCart[i].product_price)*parseInt(shoppingCart[i].product_quantity)
                        overallTotal+=total
                        newRow.append(`
                        <td>${i}</td>
                        <td>${shoppingCart[i].product_name}</td>
                        <td>${shoppingCart[i].product_price}</td>
                        <td>${shoppingCart[i].product_quantity}</td>
                        <td>$${total}</td>
                        `)
                        $('table').append(newRow)
                    }
                    $('table').append(`<tr><td colspan="2"><strong>Order Total: </strong> </td><td colspan="3">$${overallTotal}</td></tr>`)

                    
                }

        }
        else{
            console.log('you have visited a new page')
        }

        $(".checkingOut").on('click',function(){
            $.ajax({
                url: 'http://127.0.0.1:8000/checkout',
                method: 'POST',
                data: JSON.stringify(shoppingCart), // Convert the JavaScript array to a JSON string
                contentType: 'application/json', // Set the content type to JSON
                success: function (response,message) {
                  // Handle the response from the Django backend
                  console.log(message);
                  shoppingCart=[]
                  localStorage.removeItem('cartData')
                  location.reload()
                },
                error: function (error) {
                  console.error('Error:', error);
                },
              });
        })
});



$(".userLoggingOut").on('click',function(event){

    event.preventDefault()
    localStorage.removeItem('cartData')
    window.location.href=event.target.href

})



 






