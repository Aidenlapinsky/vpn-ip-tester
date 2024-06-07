fetch('/get_ip')
    .then(response => response.json())
    .then(data => {
        document.getElementById('original_ip').innerHTML = data.original_ip;
        document.getElementById('plan_a_ip').innerHTML = data.plan_a_ip;
        document.getElementById('plan_b_ip').innerHTML = data.plan_b_ip;
        document.getElementById('plan_c_ip').innerHTML = data.plan_c_ip;
    })
    .catch(error => console.error('Error:', error));
