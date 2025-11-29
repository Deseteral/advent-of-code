import AdventPuzzle.Part.*

private fun solve(input: String, part: AdventPuzzle.Part): Int {
    val (rulesSection, pagesSection) = input.split("\n\n")

    val adj = mutableMapOf<Int, MutableList<Int>>()
    rulesSection.lines().forEach { line ->
        val (a, b) = line.split("|").map { it.toInt() }
        adj.getOrPut(a) { mutableListOf() }.add(b)
    }

    var total1 = 0
    var total2 = 0

    pagesSection.lines().forEach { line ->
        val pages = line.split(",").map { it.toInt() }
        val sortedPages = pages.sortedWith { a, b ->
            if (adj[a]?.contains(b) == true) -1 else 1
        }

        if (pages == sortedPages) {
            total1 += pages.middleElement
        } else {
            total2 += sortedPages.middleElement
        }
    }

    return when (part) {
        PART_1 -> total1
        PART_2 -> total2
    }
}

private fun part1(input: String): Int = solve(input, PART_1)
private fun part2(input: String): Int = solve(input, PART_2)

fun main() {
    val task = AdventPuzzle("2024", "05")

    answer(value = part1(task.testInput), toEqual = 143)
    answer(value = part2(task.testInput), toEqual = 123)

    part1(task.input).println()
    part2(task.input).println()
}
