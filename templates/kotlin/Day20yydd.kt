import AdventPuzzle.Part.*

private fun solve(input: String, part: AdventPuzzle.Part): Int {
    return when (part) {
        PART_1 -> 1
        PART_2 -> TODO()
    }
}

private fun part1(input: String): Int = solve(input, PART_1)
private fun part2(input: String): Int = solve(input, PART_2)

fun main() {
    val task = AdventPuzzle("2025", "01")

    answer(value = part1(task.testInput), toEqual = 1)
//    answer(value = part2(task.testInput), toEqual = 2)

    part1(task.input).println()
//    part2(task.input).println()
}
