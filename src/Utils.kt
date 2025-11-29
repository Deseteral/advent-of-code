import java.math.BigInteger
import java.security.MessageDigest
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
fun <T : Any> expect(value: T, toEqual: T) {
    check(value == toEqual) { "Expected '$value' to be '$toEqual'." }
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
}

typealias Vec2f = dev.romainguy.kotlin.math.Float2
typealias Vec3f = dev.romainguy.kotlin.math.Float3

class Grid<TileT>(val tiles: List<List<TileT>>) : Iterable<Grid.Entry<TileT>> {
    val width: Int get() = tiles[0].size
    val height: Int get() = tiles.size

    operator fun get(position: Vec2i) = tiles[position.y][position.x]
    operator fun get(x: Int, y: Int) = tiles[y][x]

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
            val tiles = s.lines().map { row -> row.map { col -> col } }
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
