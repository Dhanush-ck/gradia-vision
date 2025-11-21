const courses = {
    'Computer Science': {
        'BCA': 'BCA - Bachelor of Computer Application', 
        'MSc CS': 'MSc Computer Science with Artificial Intelligence'
    },
    'Commerce': { 
        'BCom': 'BCom - Bachelor of Commerce'
    },
    'History': {
        'BA History': 'BA History - Bachelor of Arts in History'
    }
}

var departmentDropdown = document.getElementById('department');
var courseDropdown = document.getElementById('course');
var semester = document.getElementById('semester');
var password = document.getElementById('password');
var confirmPassword = document.getElementById('confirm-password');
var signUpForm = document.getElementById('signUpForm');
var submitBtn = document.getElementById('submit-button');

var semesterError = document.getElementById('semester-error');
var passwordError = document.getElementById('password-error');

departmentDropdown.addEventListener('change', function() {
    console.log("Department: " + this.value);
    handleCourse();
})

const handleCourse = ()=> {
    courseDropdown.innerHTML = "";
    const currentCourse = courses[departmentDropdown.value];
    for(i in currentCourse) {
        courseDropdown.innerHTML += `<option value='${i}'> ${currentCourse[i]} </option>`;
        // console.log(`<option value='${i}'> ${currentCourse[i]} <option>`);
    }
}
handleCourse();

semester.addEventListener('change', ()=> {
    const val = semester.value;
    if(val) {
        if(val < 1 || val > 8 ) {
            semesterError.innerHTML = 'Enter a valid semester';
        }
        else {
            semesterError.innerHTML = "";
        }
    }
    else {
        semesterError.innerHTML = ""; 
    }
})
