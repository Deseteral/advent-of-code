import AdventPuzzle.Part.*
import com.github.michaelbull.itertools.pairCombinations

private fun solve(input: String, part: AdventPuzzle.Part, isTestRun: Boolean): Long {
    val boxes = input.lines().map { Vec3i.fromCommaSeparatedText(it) }

    val connectionsByLength = boxes.pairCombinations()
        .map { Pair(it.first.distance(it.second), it) }
        .sortedBy { it.first }
        .map { it.second }
        .toList()

    val circuits: MutableList<Set<Vec3i>> = boxes.map { setOf(it) }.toMutableList()

    val connections = when (part) {
        PART_1 -> connectionsByLength.take(if (isTestRun) 10 else 1000)
        PART_2 -> connectionsByLength
    }
    for ((a, b) in connections) {
        val circuitWithA = circuits.find { it.contains(a) }!!
        val circuitWithB = circuits.find { it.contains(b) }!!

        if (circuitWithA == circuitWithB) continue

        circuits.remove(circuitWithA)
        circuits.remove(circuitWithB)
        circuits.add(circuitWithA + circuitWithB)

        if (part == PART_2 && circuits.size == 1) {
            return a.x.toLong() * b.x.toLong()
        }
    }

    if (part == PART_1) {
        return circuits.map { it.size }.sortedDescending().take(3).multiply()
    }

    unreachable()
}

private fun part1(input: String, isTestRun: Boolean): Long = solve(input, PART_1, isTestRun)
private fun part2(input: String, isTestRun: Boolean): Long = solve(input, PART_2, isTestRun)

fun main() {
    AdventPuzzle("2025", "08").forTestType { input, isTestRun ->
        answer(value = part1(input, isTestRun), toEqual = if (isTestRun) 40 else 181584)
        answer(value = part2(input, isTestRun), toEqual = if (isTestRun) 25272 else 8465902405)
    }
}
