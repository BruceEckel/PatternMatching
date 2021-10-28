// https://github.com/BruceEckel/PatternMatching
package kotlinpm

sealed interface Transport

data class Bicycle(val id: String): Transport

data class Glider(val size: Int): Transport

data class Surfboard(val weight: Double): Transport

fun exhaustive(t: Transport): String = when (t) {
    is Bicycle -> "Bicycle " + t.id
    is Glider -> "Glider " + t.size
    is Surfboard -> "Surfboard " + t.weight
}

fun main() {
    listOf(
        Bicycle ("Bob"),
        Glider (65),
        Surfboard (6.4),
    ).forEach { println(exhaustive(it)) }
}

// If you uncomment this:
// data class Skis(val length: Int): Transport
// You get an error: "'when' expression must be exhaustive,
// add necessary 'is Skis' branch or 'else' branch
