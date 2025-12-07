private fun part1(input: String): Int {
    val tiles = Grid.fromMultilineString(input)
    val startPosition = getStartingPosition(input)

    val beams = mutableListOf(startPosition)

    return sequence {
        while (beams.isNotEmpty()) {
            val nextPosition = beams.removeFirst() + Vec2i.south

            yield(
                when {
                    !tiles.isInBounds(nextPosition) -> 0

                    tiles[nextPosition].isEmptyTile -> {
                        tiles.markAsBeam(nextPosition)
                        beams.add(nextPosition)
                        0
                    }

                    tiles[nextPosition].isSplitterTile ->
                        listOf(
                            nextPosition + Vec2i.east,
                            nextPosition + Vec2i.west,
                        )
                            .filter { tiles[it].isEmptyTile }
                            .onEach { tiles.markAsBeam(it) }
                            .onEach { beams.add(it) }
                            .isNotEmpty().toInt()

                    else -> 0
                })
        }
    }.sum()
}

private fun part2(input: String): Long {
    val tiles = Grid.fromMultilineString(input)
    val startPosition = getStartingPosition(input)

    val cache: MutableMap<Vec2i, Long> = mutableMapOf()
    fun solve(beam: Vec2i): Long {
        val nextPosition = beam + Vec2i.south

        return when {
            !tiles.isInBounds(nextPosition) -> 1

            tiles[nextPosition].isEmptyTile ->
                cache.getOrPut(nextPosition) { solve(nextPosition) }

            tiles[nextPosition].isSplitterTile -> listOf(
                nextPosition + Vec2i.east,
                nextPosition + Vec2i.west
            )
                .filter { tiles[it].isEmptyTile }
                .sumOf { cache.getOrPut(it) { solve(it) } }

            else -> unreachable()
        }
    }

    return solve(startPosition)
}

private fun getStartingPosition(input: String) =
    Vec2i(input.lines().first().indexOfFirst { it == 'S' }, 0)

private val Char.isEmptyTile get() = this == '.'
private val Char.isSplitterTile get() = this == '^'
private fun Grid<Char>.markAsBeam(position: Vec2i) {
    this[position] = '|'
}

fun main() {
    Vec2i.yAxis = Vec2i.YAxisInversion.INVERTED
    AdventPuzzle("2025", "07").forTestType { input, isTestRun ->
        answer(value = part1(input), toEqual = if (isTestRun) 21 else 1626)
        answer(value = part2(input), toEqual = if (isTestRun) 40 else 48989920237096)
    }
}
