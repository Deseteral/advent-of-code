fun solve(input: String, part: Part): Int {
    return 1
}

fun main() {
    val task = Task("2025", "01")

    fun part1(input: String): Int = solve(input, Part.PART_1)
    fun part2(input: String): Int = solve(input, Part.PART_2)

    expect(part1(task.testInput), 1)
    expect(part2(task.testInput), 1)

    part1(task.input).println()
    part2(task.input).println()
}
