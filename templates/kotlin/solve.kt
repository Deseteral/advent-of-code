import AdventPuzzle.Part.*

fun solve(input: String, part: AdventPuzzle.Part): Int {
    when (part) {
        PART_1 -> 1
        PART_1 -> 2
    }
}

fun part1(input: String): Int = solve(input, PART_1)
fun part2(input: String): Int = solve(input, PART_2)

fun main() {
    val task = AdventPuzzle("2025", "01")

    expect(value = part1(task.testInput), toEqual = 1)
    expect(value = part2(task.testInput), toEqual = 2)

    part1(task.input).println()
    part2(task.input).println()
}
