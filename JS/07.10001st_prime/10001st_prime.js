const MAX_NUM = 1000007;

function sieveOfEratosthenes(k) {
	var visited = new Array(MAX_NUM);

	var result = -1;
	var countOfPrimes = 0;
	
	var found = false;
	var j; var i = 2;
		while(i < MAX_NUM && !found) {
		if(!visited[i]) {
			countOfPrimes++;

			if(countOfPrimes == k) {
				result = i;
				found = true;
			} else {
				j = 2;

				while(j * i < MAX_NUM) {
					visited[j*i] = true;
					j++;
				}
			}
		}
		i++;
	}

	return result;
}


(function main() {
	console.log(sieveOfEratosthenes(10001));
})()
