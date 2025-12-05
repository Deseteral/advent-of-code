private fun part1(input: String): Long {
    val (rangesInput, ingredientsInput) = input.split("\n\n")
    val ranges = parseRangesInput(rangesInput)

    return ingredientsInput
        .lines()
        .map { it.toLong() }
        .fold(0) { acc, ingredientId ->
            acc + ranges.any { ingredientId in it }.toInt()
        }
}

private fun part2(input: String): Long {
    val (rangesInput, _) = input.split("\n\n")
    val ranges = parseRangesInput(rangesInput)

    return ranges.reduceMergeRanges().sumOf { it.distinctValueCount() }
}

private fun parseRangesInput(rangesInput: String) = rangesInput.lines().map { line ->
    val (a, b) = line.split('-').map { it.toLong() }
    a..b
}

fun main() {
    AdventPuzzle("2025", "05").forTestType { input, isTestRun ->
        answer(value = part1(input), toEqual = if (isTestRun) 3 else 733)
        answer(value = part2(input), toEqual = if (isTestRun) 14 else 345821388687084)
    }
}
