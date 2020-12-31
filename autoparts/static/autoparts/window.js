document.addEventListener('DOMContentLoaded', function() {
	
	const myform = document.querySelector("#window");
	myform.addEventListener("submit", (event) => {
		event.preventDefault();
	const name = document.querySelector('#w_type').value;
	const price = document.querySelector('#w_price').value;
	fetch ('/newwindow', {
		method:'POST',
		body:JSON.stringify({
			"windows_name": name,
			"windows_price": price,
})
})
.then(response => response.json())
.then(result => {
alert("New Window!");

})
})
})


