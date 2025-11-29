import AdventPuzzle.Part.*
import com.github.michaelbull.itertools.pairPermutations

private fun solve(input: String, part: AdventPuzzle.Part): Int {
    val level: Grid<Char> = Grid.fromMultilineString(input)

    val antennas = mutableMapOf<Char, MutableList<Vec2i>>()

    for (entry in level) {
        if (entry.tile == '.') continue
        antennas.getOrPut(entry.tile) { mutableListOf() }
            .add(entry.position)
    }

    val uniqueAntinodePositionsDoubledDistance = mutableSetOf<Vec2i>()
    val uniqueAntinodePositions = mutableSetOf<Vec2i>()

    for (value in antennas.values) {
        for ((a, b) in value.pairPermutations()) {
            // Part 1
            val antinodePos = a + a.distance(b) * 2
            if (level.isInBounds(antinodePos)) {
                uniqueAntinodePositionsDoubledDistance.add(antinodePos)
            }

            // Part 2
            for (rep in count(start = 1, step = 1)) {
                val antinodePos = a + a.distance(b) * rep
                if (level.isInBounds(antinodePos)) {
                    uniqueAntinodePositions.add(antinodePos)
                } else {
                    break
                }
            }
        }
    }

    return when (part) {
        PART_1 -> uniqueAntinodePositionsDoubledDistance.size
        PART_2 -> uniqueAntinodePositions.size
    }
}

private fun part1(input: String): Int = solve(input, PART_1)
private fun part2(input: String): Int = solve(input, PART_2)

fun main() {
    val task = AdventPuzzle("2024", "08")

    answer(value = part1(task.testInput), toEqual = 14)
    answer(value = part2(task.testInput), toEqual = 34)

    answer(value = part1(task.input), toEqual = 351)
    answer(value = part2(task.input), toEqual = 1259)
}
