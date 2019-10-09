function largestPrimeFactor (){
    let number = 600851475143;

    let index = Math.floor(Math.sqrt(number));

    while (index > 1) {
        if (number % index == 0 && isPrime(index)) {
            alert(index);
            break;
        }
        index--;
    }
}

function isPrime (number) {
    let result = true;

	for (let i = 2; i < Math.floor(Math.sqrt(number)); i++) {
		if (number % i == 0){
			result = false;
			break;
		}
	}
	return result;
}