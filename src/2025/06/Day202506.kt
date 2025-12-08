private fun part1(input: String): Long {
    val cleanedInput = input.lines()
        .map { line ->
            line.split(' ').filter { it.isNotEmpty() }
        }

    return Grid.fromTwoDimensionalCollection(cleanedInput)
        .columns
        .map { column ->
            MathProblem(
                numbers = column.subList(0, column.size - 1).map { it.toLong() },
                operation = MathOperation.fromString(column.last()),
            )
        }
        .sumOf { it.solution }
}

private fun part2(input: String): Long {
    val input = input.lines().map { it.reversed() }
    val numberRows = input.subList(0, input.size - 1)

    val operations = input.last()
        .split(' ')
        .filter { it.isNotEmpty() }
        .map { MathOperation.fromString(it) }

    val numbers = Grid.fromMultilineString(numberRows.joinToString("\n"))
        .columns
        .map { it.joinToString("").trim() }
        .chunkBy("")
        .map { list -> list.map { it.toLong() } }

    val problems = numbers.zip(operations)
        .map { (numbers, operations) -> MathProblem(numbers, operations) }

    return problems.sumOf { it.solution }
}

private enum class MathOperation {
    SUM,
    MULTIPLY;

    companion object {
        fun fromString(input: String): MathOperation {
            return when (input) {
                "+" -> SUM
                "*" -> MULTIPLY
                else -> unreachable()
            }
        }
    }
}

private data class MathProblem(val numbers: List<Long>, val operation: MathOperation) {
    val solution: Long
        get() = when (operation) {
            MathOperation.SUM -> numbers.sum()
            MathOperation.MULTIPLY -> numbers.multiply()
        }
}

fun main() = AdventPuzzle("2025", "06").forTestType { input, isTestRun ->
    answer(value = part1(input), toEqual = if (isTestRun) 4277556 else 6757749566978)
    answer(value = part2(input), toEqual = if (isTestRun) 3263827 else 10603075273949)
}
