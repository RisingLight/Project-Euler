/**
 * A palindromic number reads the same both ways. 
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

function LargestPalindromeProduct () {
    maxNumberFinded = 0;
    for (let i = 111; i < 999; i++) {
        for (let j = 111; j < 999; j++) {
            let product = i * j;
            if (isPalindrome(product) && product >= maxNumberFinded) {
                maxNumberFinded = product;
            }
        }
    }
    alert(maxNumberFinded)
}

function isPalindrome (number) {
    let strNumber = number.toString();
    let strReverseNumber = reverse(strNumber);

    if (strNumber === strReverseNumber) {
        return true;
    } else {
        return false;
    }
}

function reverse (stringToReverse) {
    arrayOfStr = stringToReverse.split("");
    
    reverseOfArray = arrayOfStr.reverse();

    strOfReverse = reverseOfArray.join("");
    
    return strOfReverse;
}