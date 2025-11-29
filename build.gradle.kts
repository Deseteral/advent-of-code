plugins {
    kotlin("jvm") version "2.2.21"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("dev.romainguy:kotlin-math:1.6.0")
    implementation("com.michael-bull.kotlin-itertools:kotlin-itertools:1.0.2")
}

sourceSets {
    main {
        kotlin.srcDir("src")
    }
}

tasks {
    wrapper {
        gradleVersion = "9.2.1"
    }
}
