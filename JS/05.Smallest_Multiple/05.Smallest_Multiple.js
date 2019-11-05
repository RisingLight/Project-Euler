const lcm = (firstNum, ...remainingNums) => {
    if (remainingNums.length === 0) {
        throw (new Error("Input for method must contain at least two numbers"));
    }
    if (remainingNums.length === 1) {
        secondNum = remainingNums[0];
        return (firstNum * secondNum) / gcd(firstNum, secondNum);
    }
    const [nextNum, ...otherNums] = remainingNums;
    return lcm(lcm(firstNum, nextNum), ...otherNums);
}
const gcd = (firstNum, secondNum) => {
    const biggerNum = firstNum > secondNum ? firstNum : secondNum;
    const smallerNum = firstNum > secondNum ? secondNum : firstNum;
    let greatestCommonFactor = smallerNum;
    while (biggerNum % greatestCommonFactor !== 0 || smallerNum % greatestCommonFactor !== 0) {
        greatestCommonFactor--;
    }
    return greatestCommonFactor;
}
const nums = new Array(20).fill(1);
const firstTwentyNumbers = nums.map((num, index) => index + num);
console.log(lcm(...firstTwentyNumbers));