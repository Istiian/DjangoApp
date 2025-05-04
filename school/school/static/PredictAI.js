const age = document.getElementById("id_age");
const gender = document.getElementById("id_gender");
const interests = document.querySelectorAll('input[type="checkbox"][name="interest"]');
const course = document.getElementById("id_course");
let checked = document.querySelectorAll('input[type="checkbox"][name="interest"]:checked');
const courseName = document.getElementById("course-name");
const courseDisplay = document.getElementById("course-display");

age.addEventListener("change", function () {
    PredictCourse();
});

gender.addEventListener("change", function () {
    PredictCourse();
});

window.addEventListener('load', (event) => {
    // PredictCourse();
    // checkCourse();
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

course.addEventListener("change", checkCourse);
function checkCourse(){
    if (course.value === "") {
        courseDisplay.classList.add("d-none");
        courseDisplay.classList.remove("d-block");
    } else {
        courseDisplay.classList.remove("d-none");
        courseDisplay.classList.add("d-block");
    }
}
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
        courseDisplay.classList.add("d-none");
        courseDisplay.classList.remove("d-block");
    } else {
        fetch('/students/predict/', {
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
            return response.json(); 
        })
        .then(data => {
            if (data && data.course) {
                // if(course.value === ""){
                    courseName.innerHTML = data.course;
                    courseDisplay.classList.remove("d-none");
                    courseDisplay.classList.add("d-block");
                // }
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



