private fun solve(input: String): Pair<Int, Int> {
    var state = 50
    var hit1 = 0
    var hit2 = 0

    for (line in input.lines()) {
        val direction = when(line.first()) {
            'L' -> -1
            'R' -> 1
            else -> unreachable()
        }
        val amount = line.substring(1).toInt()

        repeat(amount) {
            state += direction
            state %= 100
            if (state == 0) hit2 += 1
        }

        if (state == 0) hit1 += 1
    }

    return Pair(hit1, hit2)
}

fun main() {
    val task = AdventPuzzle("2025", "01")
    answer(value = solve(task.testInput), toEqual = Pair(3, 6))
    answer(value = solve(task.input), toEqual = Pair(1105, 6599))
}
