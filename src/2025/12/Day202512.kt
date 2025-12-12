private fun solve(input: String): Int {
    val inputGroups = input.split("\n\n")

    data class Region(val size: Pair<Int, Int>, val indices: List<Int>)

    val regions: List<Region> = inputGroups.last().lines()
        .map { it.split(": ") }
        .map { (size, indices) ->
            Region(
                size = size.split("x").map { it.toInt() }.toPair(),
                indices = indices.split(' ').map { it.toInt() }
            )
        }

    return regions
        .map { region ->
            val presentsCount = region.indices.sum()

            val unitWidth = region.size.first / 3
            val unitHeight = region.size.second / 3
            val unitArea = unitWidth * unitHeight

            presentsCount <= unitArea
        }
        .countTrue()
}

fun main() {
    val task = AdventPuzzle("2025", "12")
    answer(value = solve(task.input), toEqual = 587)
}
