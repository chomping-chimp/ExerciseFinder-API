$(document).ready(function(){
    let timer;
    let timer_on = 0;

    $("td a").click(function() {
        let restTimer = $(this);
        let restTime = restTimer.text();
        let originalTime = restTime;

        if (!timer_on) {
            toggleInputs(false);
            timer_on = true;
            timer = setInterval(function(){
                restTime--;
                restTimer.text(restTime);
                if (restTime < 1) {
                    clearInterval(timer);
                    restTimer.removeClass("baby-blue").addClass('error');
                    toggleInputs();
                    // Add below to reset timer
                    // restTimer.text(originalTime);
                }
            }, 1000);
        } else {
            stopCount();
            toggleInputs();
        }
    });

    function stopCount() {
        clearInterval(timer);
        timer_on = 0;
    }
    function toggleInputs(active=true) {
        if (active) {
            $("input").prop('disabled', false);
            $("input").removeClass("greyed");
        } else {
            $("input").prop('disabled', true);
            $("input").addClass('greyed');
        }
    }
})

  
