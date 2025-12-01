fun main() {
    AdventPuzzle("2024", "18").forTestType { input, isTestRun ->
        val startPos = Vec2i.zero
        val endPos = if (isTestRun) Vec2i(6, 6) else Vec2i(70, 70)
        val stepsToSimulate = if (isTestRun) 12 else 1024

        val w = if (isTestRun) 6 + 1 else 70 + 1
        val h = if (isTestRun) 6 + 1 else 70 + 1
        val level = Grid.fromRepeatingValue('.', w, h)

        for (line in input.lines().subList(0, stepsToSimulate)) {
            level[Vec2i.fromCommaSeparatedText(line)] = '#'
        }

        val getTileNeighbours = { tilePosition: Vec2i ->
            Vec2i.directions
                .map { tilePosition + it }
                .filter { level.isInBounds(it) }
                .filter { level[it] == '.' }
        }
        val getDistanceToNeighbour = { _: Vec2i, _: Vec2i -> 1 }
        val isEndTile = { tilePosition: Vec2i -> tilePosition == endPos }

        fun part1(): Int {
            val (_, bestDistance) = dijkstraSinglePrecision(
                startingNodes = listOf(Pair(startPos, 0)),
                getConnectedNodes = getTileNeighbours,
                getEdgeWeight = getDistanceToNeighbour,
                isEndNode = isEndTile,
            )
            return bestDistance[endPos]!!
        }

        fun part2(): String {
            for (line in input.lines().subList(stepsToSimulate, input.lines().size)) {
                level[Vec2i.fromCommaSeparatedText(line)] = '#'

                val (_, bestDistance) = dijkstraSinglePrecision(
                    startingNodes = listOf(Pair(startPos, 0)),
                    getConnectedNodes = getTileNeighbours,
                    getEdgeWeight = getDistanceToNeighbour,
                    isEndNode = isEndTile,
                )
                if (!bestDistance.containsKey(endPos)) {
                    return line
                }
            }

            unreachable()
        }

        answer(value = part1(), toEqual = if (isTestRun) 22 else 290)
        answer(value = part2(), toEqual = if (isTestRun) "6,1" else "64,54")
    }
}
