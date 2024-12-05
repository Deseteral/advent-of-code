import java.io.File

val (rulesSection, pagesSection) = File("./input")
    .readText()
    .split("\n\n")

val adj = mutableMapOf<Int, MutableList<Int>>()
rulesSection.lines().forEach { line ->
    val (a, b) = line.split("|").map { it.toInt() }
    adj.getOrPut(a) { mutableListOf() }.add(b)
}

var total1 = 0
var total2 = 0

pagesSection.lines().forEach { line ->
    val pages = line.split(",").map { it.toInt() }
    val sortedPages = pages.sortedWith { a, b -> if (adj[a]!!.contains(b)) -1 else 1 }

    if (pages == sortedPages) {
        total1 += pages.middleElement
    } else {
        total2 += sortedPages.middleElement
    }
}

println(total1)
println(total2)

val <T> List<T>.middleElement get() = this[this.size / 2]
