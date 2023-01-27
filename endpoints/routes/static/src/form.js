
$(document).ready(function () {
    $(window).keydown(function(event){
        if(event.keyCode == 13) {
          event.preventDefault();
          return false;
        }
    });
    
    $("#add-set").click(function() {
        $(".exercise-set").first().clone(true).insertBefore("#set-placeholder");
        console.log(this);
        return false;
    });
    
    $("#remove-set").click(function() {
        $(this).parent().remove();
    });

    $("#add-exercise").click(function() {
        // Get entered values
        let exerciseName = $("#ex-name").val();
        let exerciseSets = $("#ex-sets").val();
        // Clone hidden template and populate
        let newExercise = $(".exercise").first().clone(true);
        newExercise.find(".exercise-name").val(exerciseName);
        newExercise.find(".set-counter").val(exerciseSets);

        newExercise.removeAttr('hidden');
        hash = generateHash(exerciseName);
        newExercise.removeClass("exercise").addClass(`exercise-${hash}`);
        newExercise.insertBefore("#exercise-placeholder");

        for (let i=0; i<exerciseSets; i++) {
            var newSet;
            if (i == 0) {
                newSet = newExercise.find(".exercise-set").first();
            } else {
                newSet = newExercise.find(".exercise-set").first().clone(true);
            }
            newSet.removeAttr('hidden');
            newSet.appendTo(`.exercise-${hash}`);
        }
        $('#add_exercise_modal').prop("checked", false);
        return false;
    });
});

function generateHash(string) {
    var hash = 0;
    if (string.length == 0)
        return hash;
    for (let i = 0; i < string.length; i++) {
        var charCode = string.charCodeAt(i);
        hash = ((hash << 7) - hash) + charCode;
        hash = hash & hash;
    }
    return hash;
}
