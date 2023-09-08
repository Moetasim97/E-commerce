


$(document).ready(function() {
    function initializeComponent($component) {
        let counter = 0;
        let $incrementButton = $component.find('.addItems');
        let $decrementButton = $component.find('.subtractItems');
        let $counterDisplay = $component.find('.counterPlace');

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
    $('.selectingContainer').each(function() {
        initializeComponent($(this));
    });
});