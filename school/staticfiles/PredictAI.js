const age = document.getElementById("id_age");
const gender = document.getElementById("id_gender");
const interests = document.querySelectorAll('input[type="checkbox"][name="interest"]');
let checked = document.querySelectorAll('input[type="checkbox"][name="interest"]:checked');
const courseName = document.getElementById("course-name");
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
        
    } else {
        fetch('predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `age=${age.value}&gender=${gender.value}&interests=${InterestValue()}`
        })
        .then(response => {
            console.log("Raw response:", response);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json(); // Parse the JSON response from the server
        })
        .then(data => {
            if (data && data.course) {
                courseName.innerHTML = data.course;
                alert(data.course)
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



