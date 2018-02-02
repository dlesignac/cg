import math._
import scala.util._

object Player extends App {

    val surface = SurfaceReader.read()
    Console.err.println(surface)

    while(true) {
        val Array(x, y, hspeed, vspeed, fuel, rotate, power) = for(i <- readLine split " ") yield i.toInt
        Console.err.println("err")
        println("-20 3")
    }
}

object SurfaceReader {

    def read() : Surface = {
        val n = readInt
        val points = readPoints(n)
        new Surface(points)
    }

    def readPoints(n : Int) : Seq[Point] = {
        for(i <- 0 until n) yield readPoint()
    }
    
    def readPoint() : Point = {
        val Array(x, y) = for(i <- readLine split " ") yield i.toInt
        new Point(x, y)
    }
}

class Surface(val points : Seq[Point]) {
    
    override def toString: String = {
        points
            .map(point => point.toString())
            .mkString(",")
    }

}

class Point(val x : Int, val y : Int) {
    
    override def toString: String = {
        s"($x,$y)"
    }
       
}
