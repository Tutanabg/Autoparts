document.addEventListener('DOMContentLoaded', function() {
	
	const myform = document.querySelector("#pay-form");
	myform.addEventListener("submit", (event) => {
		event.preventDefault();
	const name = document.querySelector('#name').value;
	const price = document.querySelector('#price').value;
	const number = document.querySelector('#card_number').value;
	fetch ('/payment', {
		method:'POST',
		body:JSON.stringify({
			"name": name,
			"price": price,
			"card_number": number,
})
})
.then(response => response.json())
.then(result => {
alert("Payed!");

})
})
})


