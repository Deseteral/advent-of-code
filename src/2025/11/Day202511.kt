private fun part1(input: String): Int {
    val graph = makeGraph(input)

    val queue = mutableListOf(listOf("you"))
    val donePaths = mutableListOf<List<String>>()
    while (queue.isNotEmpty()) {
        val currentPath = queue.removeFirst()
        val currentNode = currentPath.last()

        if (currentNode == "out") {
            donePaths.add(currentPath)
            continue
        }

        for (n in graph[currentNode]!!) {
            queue.add(currentPath + n)
        }
    }

    return donePaths.size
}

private fun part2(input: String): Long {
    val graph = makeGraph(input)

    val cache: MutableMap<Pair<String, Set<String>>, Long> = mutableMapOf()

    fun look(at: String, poi: Set<String>): Long {
        if (at == "out") {
            return if ("dac" in poi && "fft" in poi) 1 else 0
        }

        val nextPoi = when {
            (at == "fft" || at == "dac") -> poi + at
            else -> poi
        }

        return graph[at]!!.sumOf {
            cache.getOrPut(it to nextPoi) { look(it, nextPoi) }
        }
    }

    return look("svr", emptySet())
}

private fun makeGraph(input: String): Map<String, Set<String>> {
    return input.lines()
        .map { it.split(':') }
        .associate { (from, toRaw) ->
            Pair(from, toRaw.trim().split(' ').toSet())
        }
}

fun main() {
    val task = AdventPuzzle("2025", "11")

    answer(value = part1(task.input), toEqual = 796)

    answer(value = part2(task.testInput), toEqual = 2)
    answer(value = part2(task.input), toEqual = 294053029111296)
}
