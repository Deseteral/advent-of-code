import kotlin.math.pow

private fun findMaxInSub(bank: String, level: Int): Long {
    val sub = bank.take(bank.length - level).map { it.digitToInt() }
    val a = sub.max()

    return if (level == 0) a.toLong() else {
        val idx = sub.indexOfFirst { it == a }
        val rest = bank.substring(idx + 1)
        val magnitude = (10.0).pow(level).toLong()

        (a * magnitude) + findMaxInSub(rest, level - 1)
    }
}

private fun solve(batteryCount: Int, input: String) =
    input.lines().sumOf { findMaxInSub(it, batteryCount - 1) }

fun main() {
    AdventPuzzle("2025", "03").forTestType { input, isTestRun ->
        answer(
            value = solve(batteryCount = 2, input),
            toEqual = if (isTestRun) 357 else 17524
        )
        answer(
            value = solve(batteryCount = 12, input),
            toEqual = if (isTestRun) 3121910778619 else 173848577117276
        )
    }
}
