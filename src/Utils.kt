import java.math.BigInteger
import java.security.MessageDigest
import java.util.PriorityQueue
import kotlin.io.path.Path
import kotlin.io.path.readText

class AdventPuzzle(val year: String, val day: String) {
    /**
     * Input for this day.
     */
    val input: String get() = readInput(test = false)

    /**
     * Test input for this day.
     */
    val testInput: String get() = readInput(test = true)

    private fun readInput(test: Boolean): String {
        val basePath = "src/$year/$day"
        val path = if (test) "$basePath/test_input" else "$basePath/input"
        return Path(path).readText().trim()
    }

    /**
     * Identifier for part 1 or 2 of this day's puzzle task.
     */
    enum class Part {
        PART_1,
        PART_2,
    }

    fun forTestType(fn: (input: String, isTestRun: Boolean) -> Unit) {
        fn(testInput, true)
        fn(input, false)
    }
}

/**
 * Converts string to md5 hash.
 */
fun String.md5() = BigInteger(1, MessageDigest.getInstance("MD5").digest(toByteArray()))
    .toString(16)
    .padStart(32, '0')

/**
 * The cleaner shorthand for printing output.
 */
fun Any?.println() = println(this)

/**
 * Checks if two values are the same and prints out message when they are not.
 */
fun <T : Any> answer(value: T, toEqual: T) {
    check(value == toEqual) { "Expected '$value' to be '$toEqual'." }
    println("$value is correct answer!")
}

/**
 * Make a sequence that contains evenly spaced values beginning with start and increasing by step.
 */
fun count(start: Int, step: Int) = generateSequence(start) { it + step }

/**
 * Returns middle element of that list.
 */
val <T> List<T>.middleElement get() = this[this.size / 2]

data class Vec2i(val x: Int, val y: Int) {
    operator fun plus(v: Vec2i) = Vec2i(x + v.x, y + v.y)
    operator fun minus(v: Vec2i) = Vec2i(x - v.x, y - v.y)
    operator fun times(v: Vec2i) = Vec2i(x * v.x, y * v.y)
    operator fun div(v: Vec2i) = Vec2i(x / v.x, y / v.y)

    operator fun plus(v: Int) = Vec2i(x + v, y + v)
    operator fun minus(v: Int) = Vec2i(x - v, y - v)
    operator fun times(v: Int) = Vec2i(x * v, y * v)
    operator fun div(v: Int) = Vec2i(x / v, y / v)

    fun equals(other: Vec2i) = x == other.x && y == other.y

    override fun toString(): String = "Vec2($x, $y)"

    fun distance(to: Vec2i) = Vec2i(to.x - x, to.y - y)

    companion object {
        val zero: Vec2i get() = Vec2i(0, 0)

        /**
         * Vectors for north, east, south, west.
         * ↑ → ↓ ←
         */
        val directions: List<Vec2i>
            get() = listOf(
                Vec2i(0, 1),
                Vec2i(1, 0),
                Vec2i(0, -1),
                Vec2i(-1, 0),
            )

        /**
         * Vectors for north, north-east, east, south-east, south, south-west, west, north-west.
         * ↑ ↗ → ↘ ↓ ↙ ← ↖
         */
        val directionsWithDiagonals: List<Vec2i>
            get() = listOf(
                Vec2i(0, 1),
                Vec2i(1, 1),
                Vec2i(1, 0),
                Vec2i(1, -1),
                Vec2i(0, -1),
                Vec2i(-1, -1),
                Vec2i(-1, 0),
                Vec2i(-1, 1),
            )


        fun fromCommaSeparatedText(text: String): Vec2i {
            val (x, y) = text.split(',').map { it.toInt() }
            return Vec2i(x, y)
        }
    }
}

typealias Vec2f = dev.romainguy.kotlin.math.Float2
typealias Vec3f = dev.romainguy.kotlin.math.Float3

class Grid<TileT>(val tiles: MutableList<MutableList<TileT>>) : Iterable<Grid.Entry<TileT>> {
    val width: Int get() = tiles[0].size
    val height: Int get() = tiles.size

    operator fun get(position: Vec2i) = tiles[position.y][position.x]
    operator fun get(x: Int, y: Int) = tiles[y][x]

    operator fun set(position: Vec2i, value: TileT) {
        tiles[position.y][position.x] = value
    }

    operator fun set(x: Int, y: Int, value: TileT) {
        tiles[y][x] = value
    }

    fun getOrNull(position: Vec2i): TileT? = try {
        tiles[position.y][position.x]
    } catch (_: Exception) {
        null
    }

    fun isInBounds(position: Vec2i) =
        position.x in 0..<width && position.y in 0..<height

    override fun iterator(): Iterator<Entry<TileT>> {
        return GridIterator(this)
    }

    companion object {
        fun fromMultilineString(s: String): Grid<Char> {
            val tiles = s.lines().map { row -> row.map { col -> col }.toMutableList() }
            return Grid(tiles.toMutableList())
        }

        fun <TileT> fromRepeatingValue(value: TileT, width: Int, height: Int): Grid<TileT> {
            val tiles = MutableList(height) { MutableList(width) { value } }
            return Grid(tiles)
        }
    }

    data class Entry<TileT>(val position: Vec2i, val tile: TileT)

    private class GridIterator<TileT>(private val grid: Grid<TileT>) : Iterator<Entry<TileT>> {
        private var idx = 0
        private val maxIdx = grid.width * grid.height

        override fun hasNext(): Boolean {
            return idx < maxIdx
        }

        override fun next(): Entry<TileT> {
            val position = Vec2i(idx % grid.width, idx / grid.width)
            val tile = grid[position]
            idx += 1
            return Entry(position, tile)
        }
    }
}

data class DijkstraResult<NodeT, DistanceT>(
    val endNodes: List<Pair<DistanceT, NodeT>>,
    val bestDistance: Map<NodeT, DistanceT>,
)

private fun <NodeT, DistanceT> dijkstra(
    startingNodes: List<Pair<NodeT, DistanceT>>,
    getConnectedNodes: (NodeT) -> List<NodeT>,
    getEdgeWeight: (from: NodeT, to: NodeT) -> DistanceT,
    isEndNode: (NodeT) -> Boolean,
    addDistanceFn: (DistanceT, DistanceT) -> DistanceT,
): DijkstraResult<NodeT, DistanceT> where DistanceT : Number, DistanceT : Comparable<DistanceT> {
    val bestDistance = mutableMapOf<NodeT, DistanceT>()
    val queue = PriorityQueue<Pair<DistanceT, NodeT>>(compareBy { it.first })

    for ((node, initialDistance) in startingNodes) {
        queue.add(Pair(initialDistance, node))
    }

    while (!queue.isEmpty()) {
        val (distance, node) = queue.poll()

        if (bestDistance.containsKey(node)) {
            continue
        }

        bestDistance[node] = distance

        for (neighbourNode in getConnectedNodes(node)) {
            if (!bestDistance.containsKey(neighbourNode)) {
                val nextDist = addDistanceFn(bestDistance[node]!!, getEdgeWeight(node, neighbourNode))
                queue.add(Pair(nextDist, neighbourNode))
            }
        }
    }

    val endNodes = mutableListOf<Pair<DistanceT, NodeT>>()
    for ((node, distance) in bestDistance.entries) {
        if (isEndNode(node)) {
            endNodes.add(Pair(distance, node))
        }
    }

    return DijkstraResult(endNodes, bestDistance)
}

fun <NodeT> dijkstraSinglePrecision(
    startingNodes: List<Pair<NodeT, Int>>,
    getConnectedNodes: (NodeT) -> List<NodeT>,
    getEdgeWeight: (from: NodeT, to: NodeT) -> Int,
    isEndNode: (NodeT) -> Boolean,
): DijkstraResult<NodeT, Int> =
    dijkstra(startingNodes, getConnectedNodes, getEdgeWeight, isEndNode, addDistanceFn = { a, b -> a + b })

fun <NodeT> dijkstraDoublePrecision(
    startingNodes: List<Pair<NodeT, Double>>,
    getConnectedNodes: (NodeT) -> List<NodeT>,
    getEdgeWeight: (from: NodeT, to: NodeT) -> Double,
    isEndNode: (NodeT) -> Boolean,
): DijkstraResult<NodeT, Double> =
    dijkstra(startingNodes, getConnectedNodes, getEdgeWeight, isEndNode, addDistanceFn = { a, b -> a + b })
