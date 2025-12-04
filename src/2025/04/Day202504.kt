fun canTileBeMoved(position: Vec2i, level: Grid<Char>): Boolean {
    return level.getNeighboursOfTile(position, withDiagonals = true)
        .filter { it.isPaper }
        .size
        .let { it < 4 }
}

private fun part1(input: String): Int {
    val level = Grid.fromMultilineString(input)
    return level.entries()
        .filter { it.isPaper }
        .count { canTileBeMoved(it.position, level) }
}

private fun part2(input: String): Int {
    val level = Grid.fromMultilineString(input)
    var total = 0

    while (true) {
        val toBeRemoved = level.entries()
            .filter { it.isPaper }
            .filter { canTileBeMoved(it.position, level) }
            .map { it.position }
            .toSet()

        if (toBeRemoved.isEmpty()) break

        total += toBeRemoved.size
        toBeRemoved.forEach { level[it] = '.' }
    }

    return total
}

private val Grid.Entry<Char>.isPaper get() = this.tile == '@'

fun main() {
    AdventPuzzle("2025", "04").forTestType { input, isTestRun ->
        answer(value = part1(input), toEqual = if (isTestRun) 13 else 1428)
        answer(value = part2(input), toEqual = if (isTestRun) 43 else 8936)
    }
}
