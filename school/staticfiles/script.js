const age = document.getElementById("id_age");
const gender = document.getElementById("id_gender");
const interests = document.querySelectorAll('input[type="checkbox"][name="interest"]');
let checked = document.querySelectorAll('input[type="checkbox"][name="interest"]:checked');

age.addEventListener("change", function () {
    PredictCourse();
});

interests.forEach((interest) => {
    interest.addEventListener("change", function () {
        checked = document.querySelectorAll('input[type="checkbox"][name="interest"]:checked');
        if (checked.length > 3) {
            alert("You can select only 3 interests");
            this.checked = false;
        }else{
            PredictCourse();
        }
    });
})

gender.addEventListener("change", function () {
    PredictCourse();
});

function InterestValue(){
    let checked = document.querySelectorAll('input[type="checkbox"][name="interest"]:checked');
    let values = [];
    checked.forEach((interest) => {
        values.push(interest.value);
    });
    return values.join(",");
}


function PredictCourse() { 
    console.log("PredictCourse function was called!");
    const checked = document.querySelectorAll('input[name="interest"]:checked');

    if (age.value === "" || checked.length === 0 || gender.value === "") {
        alert("Please fill all required fields.");
    } else {
        fetch('predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `age=${age.value}&gender=${gender.value}&interests=${InterestValue()}`
        })
        .then(() => {
            // Mock response
            return Promise.resolve({ course: "Mock Course" });
        })
        .then(data => {
            console.log("Mock data:", data);
            if (data && data.course) {
                alert(data.course);
            } else {
                alert("No course found or invalid response.");
            }
        })
        .catch(err => {
            alert("Error: " + err.message);
            console.error(err);
        });
    }
}



