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
fun <T: Any> expect(value: T, toEqual: T) {
    check(value == toEqual) { "Expected '$value' to be '$toEqual'." }
}

/**
 * Returns middle element of that list.
 */
val <T> List<T>.middleElement get() = this[this.size / 2]
