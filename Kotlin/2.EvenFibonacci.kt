fun main(args: Array<String>) {
    var firstNumber = 0
    var secondNumber = 1
    var i = 0
    var sum:Int
    println("Enter number of terms: ")
    val numberOfTimes = readLine()!!.toInt()
    while (i != numberOfTimes) {
        sum = firstNumber + secondNumber
        if (sum % 2 == 0) {
            i++
            System.out.println(sum)
        }
        firstNumber = secondNumber
        secondNumber = sum
    }
}
