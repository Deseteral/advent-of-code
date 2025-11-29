import java.math.BigInteger
import java.security.MessageDigest
import kotlin.io.path.Path
import kotlin.io.path.readText

class Task(val year: String, val day: String) {
    val input: String get() = readInput(test = false)
    val testInput: String get() = readInput(test = true)

    private fun readInput(test: Boolean): String {
        val basePath = "src/$year/$day"
        val path = if (test) "$basePath/test_input" else "$basePath/input"
        return Path(path).readText().trim()
    }
}

enum class Part {
    PART_1,
    PART_2,
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

fun <T: Any> expect(value: T, toBe: T) {
    check(value == toBe) { "Expected $value to be $toBe" }
}
