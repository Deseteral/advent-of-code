import AdventPuzzle.Part.*

data class Machine(
    val lights: Set<Int>,
    val buttons: List<Set<Int>>,
)

private fun part1(input: String): Int {
    val machines = input.lines().map { line ->
        val tokens = line.split(' ')
        val lightTokens = tokens.first()
        val buttonTokens = tokens.subList(1, tokens.size - 1)

        val lights = lightTokens
            .substring(1, lightTokens.length - 1)
            .mapIndexed { index, ch -> if (ch == '#') index else null }
            .filterNotNull()
            .toSet()

        val buttons = buttonTokens
            .map { token -> token.substring(1, token.length - 1) }
            .map { token -> token.split(',').map { it.toInt() }.toSet() }

        Machine(lights, buttons)
    }

    val presses: List<Int> = machines.map { machine ->
        val queue = mutableListOf(Pair(0, emptySet<Int>()))
        val previous = mutableSetOf<Set<Int>>()

        while (queue.isNotEmpty()) {
            val (level, current) = queue.removeFirst()

            if (current == machine.lights) {
                return@map level
            }

            for (button in machine.buttons) {
                val nn = current.symmetricDifference(button)
                if (nn in previous) {
                    continue
                } else {
                    previous.add(nn)
                    queue.add(Pair(level + 1, nn))
                }
            }
        }
        unreachable()
    }

    return presses.sum()
}

fun main() {
    val task = AdventPuzzle("2025", "10")

    answer(value = part1(task.testInput), toEqual = 7)
    answer(value = part1(task.input), toEqual = 505)
}
