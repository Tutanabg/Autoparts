document.addEventListener('DOMContentLoaded', function() {
	
	const myform = document.querySelector("#door");
	myform.addEventListener("submit", (event) => {
		event.preventDefault();
	const name = document.querySelector('#d_type').value;
	const price = document.querySelector('#d_price').value;
	fetch ('/newdoor', {
		method:'POST',
		body:JSON.stringify({
			"doors_name": name,
			"doors_price": price,
})
})
.then(response => response.json())
.then(result => {
alert("New Door!");

})
})
})


