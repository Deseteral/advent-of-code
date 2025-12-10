import java.math.BigInteger
import java.security.MessageDigest
import java.util.PriorityQueue
import kotlin.collections.mutableListOf
import kotlin.io.path.Path
import kotlin.io.path.readText
import kotlin.math.pow
import kotlin.math.sqrt

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

fun unreachable(): Nothing = throw IllegalStateException("This should not happen!")

/**
 * Returns middle element of that list.
 */
val <T> List<T>.middleElement get() = this[this.size / 2]

@kotlin.jvm.JvmName("productOfInt")
fun List<Int>.multiply(): Long = this.fold(1L) { acc, i -> acc * i.toLong() }

@kotlin.jvm.JvmName("productOfLong")
fun List<Long>.multiply(): Long = this.fold(1L) { acc, i -> acc * i }

/**
 * Returns 0 for false, 1 for true.
 */
fun Boolean.toInt() = if (this) 1 else 0

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

    override fun toString(): String = "Vec2i($x, $y)"

    fun distance(to: Vec2i) = Vec2i(to.x - x, to.y - y)

    enum class YAxisInversion {
        NORMAL,
        INVERTED,
    }

    companion object {
        var yAxis: YAxisInversion = YAxisInversion.NORMAL

        val zero: Vec2i get() = Vec2i(0, 0)

        val north: Vec2i
            get() = Vec2i(
                0, when (yAxis) {
                    YAxisInversion.NORMAL -> 1
                    YAxisInversion.INVERTED -> -1
                }
            )
        val east: Vec2i get() = Vec2i(1, 0)
        val south: Vec2i
            get() = Vec2i(
                0, when (yAxis) {
                    YAxisInversion.NORMAL -> -1
                    YAxisInversion.INVERTED -> 1
                }
            )
        val west: Vec2i get() = Vec2i(-1, 0)

        /**
         * Vectors for north, east, south, west.
         * ↑ → ↓ ←
         */
        val directions: List<Vec2i>
            get() = listOf(north, east, south, west)

        /**
         * Vectors for north, north-east, east, south-east, south, south-west, west, north-west.
         * ↑ ↗ → ↘ ↓ ↙ ← ↖
         */
        val directionsWithDiagonals: List<Vec2i>
            get() = listOf(
                north,
                north + east,
                east,
                south + east,
                south,
                south + west,
                west,
                north + west,
            )


        fun fromCommaSeparatedText(text: String): Vec2i {
            val (x, y) = text.split(',').map { it.toInt() }
            return Vec2i(x, y)
        }
    }
}

data class Vec3i(val x: Int, val y: Int, val z: Int) {
    operator fun plus(v: Vec3i) = Vec3i(x + v.x, y + v.y, z + v.z)
    operator fun minus(v: Vec3i) = Vec3i(x - v.x, y - v.y, z - v.z)
    operator fun times(v: Vec3i) = Vec3i(x * v.x, y * v.y, z * v.z)
    operator fun div(v: Vec3i) = Vec3i(x / v.x, y / v.y, z / v.z)

    operator fun plus(v: Int) = Vec3i(x + v, y + v, z + v)
    operator fun minus(v: Int) = Vec3i(x - v, y - v, z - v)
    operator fun times(v: Int) = Vec3i(x * v, y * v, z * v)
    operator fun div(v: Int) = Vec3i(x / v, y / v, z / v)

    fun equals(other: Vec3i) = x == other.x && y == other.y && z == other.z

    override fun toString(): String = "Vec3i($x, $y, $z)"

    fun distance(to: Vec3i) =
        sqrt((x - to.x).toDouble().pow(2) + (y - to.y).toDouble().pow(2) + (z - to.z).toDouble().pow(2))

    enum class YAxisInversion {
        NORMAL,
        INVERTED,
    }

    companion object {
        val zero: Vec3i get() = Vec3i(0, 0, 0)

        fun fromCommaSeparatedText(text: String): Vec3i {
            val (x, y, z) = text.split(',').map { it.toInt() }
            return Vec3i(x, y, z)
        }
    }
}

typealias Vec2f = dev.romainguy.kotlin.math.Float2
typealias Vec3f = dev.romainguy.kotlin.math.Float3

class Grid<TileT>(val tiles: MutableList<MutableList<TileT>>) : Iterable<Grid.Entry<TileT>> {
    val width: Int get() = tiles[0].size
    val height: Int get() = tiles.size

    val rows: List<List<TileT>> get() = tiles

    val columns: List<List<TileT>>
        get() = (0..<width).map { x ->
            (0..<height).map { y -> tiles[y][x] }
        }

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

    fun getNeighboursOfTile(position: Vec2i, withDiagonals: Boolean): List<Entry<TileT>> {
        return (if (withDiagonals) Vec2i.directionsWithDiagonals else Vec2i.directions)
            .map { position + it }
            .filter { isInBounds(it) }
            .map { Entry(it, get(it)) }
    }

    fun print(tilePrinter: (entry: Entry<TileT>) -> Char) {
        for (y in 0..<height) {
            for (x in 0..<width) {
                val c = tilePrinter(Entry(Vec2i(x, y), get(x, y)))
                print(c)
            }
            println("")
        }
        println("")
    }

    fun entries(): List<Entry<TileT>> {
        val entries = mutableListOf<Entry<TileT>>()
        for (y in 0..<height) {
            for (x in 0..<width) {
                entries.add(Entry(Vec2i(x, y), get(x, y)))
            }
        }
        return entries.toList()
    }

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

        fun <TileT> fromTwoDimensionalCollection(tiles: Collection<Collection<TileT>>): Grid<TileT> {
            return Grid(tiles.map { it.toMutableList() }.toMutableList())
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

/**
 * Calculate the count of distinct values in that range.
 * Does not create a collection with all values in it.
 */
fun LongRange.distinctValueCount() = this.last - this.first + 1L

fun List<LongRange>.reduceMergeRanges(): List<LongRange> {
    val ranges = this.sortedBy { it.first }
    val reducedRanges = mutableListOf<LongRange>()

    var current = ranges.first()

    for (range in ranges.subList(1, ranges.size)) {
        if (range.first in current) {
            /*
             *       ┌──────── range A ────────┐
             * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶
             *    └───── range B ─────┘
             *
             * or
             *
             *         ┌─ range A ─┐
             * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶
             *    └──────── range B ────────┘
             *
             * Ranges are overlapping - merge them.
             */
            val last = maxOf(range.last, current.last)
            current = current.first..last
        } else {
            /*
             *                   ┌─ range A ─┐
             * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶
             *    └─ range B ─┘
             *
             * Ranges are not overlapping - move on.
             */
            reducedRanges.add(current)
            current = range
        }
    }
    reducedRanges.add(current)

    return reducedRanges.toList()
}

fun <ElementT : Any> List<ElementT>.chunkBy(separator: ElementT): List<List<ElementT>> {
    return this
        .fold(mutableListOf(mutableListOf<ElementT>())) { acc, element ->
            if (element == separator) {
                acc.add(mutableListOf())
            } else {
                acc.last().add(element)
            }
            acc
        }
        .filter { it.isNotEmpty() }
}

fun diffTool(a: List<Any>, b: List<Any>) {
    if (a.size != b.size) {
        "Lists are not the same size. a.size = ${a.size}, b.size = ${b.size}.".println()
    }

    for (idx in 0..<maxOf(a.size, b.size)) {
        if (a[idx] != b[idx]) {
            "Elements at idx $idx are not the same!".println()
            "  a[$idx] = ${a[idx]},".println()
            "  b[$idx] = ${b[idx]}.".println()
            throw IllegalStateException("Diff tool comparison failed!")
        }
    }
}
fun <T> Set<T>.symmetricDifference(other: Set<T>): Set<T> {
    val onlyInThis = this.minus(other)
    val onlyInOther = other.minus(this)
    return onlyInThis.union(onlyInOther)
}
