
fun main(args: Array<String>){

    var numberofTimes= readLine()!!.toInt()
    for (i in 1..numberofTimes)
    {
        if(i%3==0 && i%5==0)
        println(i)
    }


}
