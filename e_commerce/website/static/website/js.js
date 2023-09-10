
var shoppingCart=[]

$(document).ready(function() {
    console.log("I just loaded")
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
            console.log(shoppingCart)
            
        })

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



