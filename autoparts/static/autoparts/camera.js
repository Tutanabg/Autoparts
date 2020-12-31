document.addEventListener('DOMContentLoaded', function() {
	
	const myform = document.querySelector("#camera");
	myform.addEventListener("submit", (event) => {
		event.preventDefault();
	const name = document.querySelector('#c_type').value;
	const price = document.querySelector('#c_price').value;
	fetch ('/newcamera', {
		method:'POST',
		body:JSON.stringify({
			"cameras_name": name,
			"cameras_price": price,
})
})
.then(response => response.json())
.then(result => {
alert("New Camera!");

})
})
})


