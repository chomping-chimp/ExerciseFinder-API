
$(document).ready(function () {
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
            let newSet = newExercise.find(".exercise-set").first().clone(true);
            newSet.removeAttr('hidden');
            newSet.appendTo(`.exercise-${hash}`);
        }
        $('#modal_1').prop("checked", false);
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

var setHTML = `
    <div class="exercise-set" id="set-1" hidden>
        <select id="quantLabel" name="quantLabel">
            <option>Metric</option>
            <option value="reps">Reps</option>
            <option value="time">Time (s)</option>
        </select>
        <label><input name="quantity" type="number" placeholder="Quantity" min="1" max="50"></label>
        <label><input name="pct_1rm" type="number" placeholder="1RM %" min="1" max="100"></label>
        <label><input name="rpe" type="number" placeholder="RPE" min="1" max="10" step="0.1"></label>
        <label><input name="rest" type="number" placeholder="Rest Time (secs)" min="0" max="300"></label>
        <a class="button error" id="remove-set">&#x26CC; Delete Set</a>
    </div>
`
