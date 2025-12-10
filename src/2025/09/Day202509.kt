import com.github.michaelbull.itertools.pairCombinations

private fun part1(input: String): Long {
    return input.lines()
        .map { Vec2i.fromCommaSeparatedText(it) }
        .pairCombinations()
        .map { (a, b) -> Rectangle.fromOppositeCorners(a, b) }
        .map { rectangle -> rectangle.area }
        .sortedDescending()
        .first()
}

private fun part2(input: String): Long {
    val positions = input.lines().map { Vec2i.fromCommaSeparatedText(it) }
    val areas = positions.pairCombinations()
        .map { (a, b) -> Rectangle.fromOppositeCorners(a, b) }
        .sortedByDescending { it.area }
        .map { rectangle -> Pair(rectangle.area, rectangle) }
        .toList()

    // Compress the grid.
    val positionIndex = (positions + listOf(Vec2i.zero, Vec2i(100000, 100000)))
        .flatMap { listOf(it.x, it.y) }
        .distinct()
        .sorted()
        .mapIndexed { idx, v -> Pair(v, idx) }
        .toMap()

    fun scaleDown(v: Vec2i) = Vec2i(positionIndex[v.x]!!, positionIndex[v.y]!!)

    // Setup scaled down grid.
    val scaledPositions = positions.map { scaleDown(it) }
    val tiles = Grid.fromRepeatingValue('.', positionIndex.size, positionIndex.size)

    for ((current, next) in scaledPositions.pairwise(circular = true)) {
        tiles.markAsPolygon(current)
        for (xx in current.x toward next.x) tiles.markAsPolygon(Vec2i(xx, next.y))
        for (yy in current.y toward next.y) tiles.markAsPolygon(Vec2i(next.x, yy))
    }

    // Flood fill outside of polygon.
    val queue = mutableListOf(Vec2i.zero)
    while (queue.isNotEmpty()) {
        val position = queue.removeFirst()
        for (nextPosition in Vec2i.directions.map { position + it }) {
            if (tiles.isInBounds(nextPosition) && tiles[nextPosition].isEmptyTile) {
                tiles.markAsOutsideTile(nextPosition)
                queue.add(nextPosition)
            }
        }
    }

    // Find the largest rectangle that has borders which are not intersecting flood-filled area outside of polygon.
    for ((area, rectangle) in areas) {
        val corners = rectangle.corners.map { scaleDown(it) }

        val edges = corners.pairwise(circular = true)
            .flatMap { (current, next) ->
                val xAxis = (current.x toward next.x).map { Vec2i(it, current.y) }
                val yAxis = (current.y toward next.y).map { Vec2i(current.x, it) }
                xAxis + yAxis
            }
            .distinct()

        if (edges.none { tiles[it].isOutsideTile }) {
            return area
        }
    }

    unreachable()
}

private val Char.isEmptyTile get() = this == '.'
private val Char.isOutsideTile get() = this == 'f'
private fun Grid<Char>.markAsPolygon(v: Vec2i) {
    this[v] = '#'
}

private fun Grid<Char>.markAsOutsideTile(v: Vec2i) {
    this[v] = 'f'
}

fun main() {
    AdventPuzzle("2025", "09").forTestType { input, isTestRun ->
        answer(value = part1(input), toEqual = if (isTestRun) 50 else 4777824480)
        answer(value = part2(input), toEqual = if (isTestRun) 24 else 1542119040)
    }
}
