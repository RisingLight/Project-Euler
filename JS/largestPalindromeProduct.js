function largestPalindrome(){

    var arr = [];    
    for(var i =999; i>100; i--){
        for(var j = 999; j>100; j--){
            var mul = j*i;
            if(isPalindrome(mul)){
                arr.push(j * i);
            }
        }
    }

    return Math.max.apply(Math, arr);
}

function isPalindrome(i){
    return i.toString() == i.toString().split("").reverse().join("");
}

console.log(largestPalindrome());
