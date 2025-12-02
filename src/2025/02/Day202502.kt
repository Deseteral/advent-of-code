private fun solve(input: String, isValidId: (Long) -> Boolean): Long {
    var total: Long = 0

    for (range in input.split(',')) {
        val (a, b) = range.split('-').map { it.toLong() }
        for (r in a..b) {
            if (!isValidId(r)) total += r
        }
    }
    return total
}

private fun part1(input: String): Long {
    val isValidId = fun(id: Long): Boolean {
        val id = id.toString()
        if (id.length % 2 != 0) return true
        val (a, b) = id.chunked(id.length / 2)
        return a != b
    }
    return solve(input, isValidId)
}

private fun part2(input: String): Long {
    val isValidId = fun(id: Long): Boolean {
        val id = id.toString()

        for (size in (id.length / 2) downTo 1) {
            if (id.length % size != 0) continue
            val chunks = id.chunked(size)
            if (chunks.all { it == chunks[0] }) return false
        }
        return true
    }

    return solve(input, isValidId)
}

fun main() {
    AdventPuzzle("2025", "02").forTestType { input, isTestRun ->
        answer(value = part1(input), toEqual = if (isTestRun) 1227775554 else 53420042388)
        answer(value = part2(input), toEqual = if (isTestRun) 4174379265 else 69553832684)
    }
}
