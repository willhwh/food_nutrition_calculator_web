function check() {
    select_restaurant = document.getElementById("check_restaurant").value;
    check_value = document.getElementById("tf").value;
    console.log(check_value);
    if (check_value == "True" ){
        document.getElementById('check_tf').value = 'Yes';
        document.getElementById('select_restaurant').value =  select_restaurant;
    }
    else if (check_value == 'False'){
        document.getElementById('check_tf').value = 'No';
    }
    else{
        //document.getElementById('target_form').reset()
        document.getElementById('check_tf').value = '';
        window.alert('Please select Yes or No then click confirm to submit.');
    };
};



function meal_check() {
    check_box = document.getElementById("meal");
    check_value = check_box.options[check_box.selectedIndex].text;
    console.log(check_value);
    if (check_value == "Select Your Meal" ){
        document.getElementById('select_meal').value = '';
        window.alert('Please select your meal and click confirm to submit.');
    }
    else{
        document.getElementById('select_meal').value = check_value;
    };
};

