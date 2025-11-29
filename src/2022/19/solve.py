#!/usr/local/bin/python3
import re
import functools
import math

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

def calc_blueprint(costs, simulation_time):
    most_ore_per_minute = max(list(map(lambda x: x[ORE], costs)))
    most_clay_per_minute = max(list(map(lambda x: x[CLAY], costs)))
    most_obsidian_per_minute = max(list(map(lambda x: x[OBSIDIAN], costs)))

    @functools.cache
    def can_afford(res, rbts):
        a = set([None])

        if res[ORE] >= costs[ORE][ORE] and rbts[ORE] < most_ore_per_minute:
            a.add(ORE)
        if res[ORE] >= costs[CLAY][ORE] and rbts[CLAY] < most_clay_per_minute:
            a.add(CLAY)
        if res[ORE] >= costs[OBSIDIAN][ORE] and res[CLAY] >= costs[OBSIDIAN][CLAY] and rbts[OBSIDIAN] < most_obsidian_per_minute:
            a.add(OBSIDIAN)
        if res[ORE] >= costs[GEODE][ORE] and res[OBSIDIAN] >= costs[GEODE][OBSIDIAN]:
            a.add(GEODE)

        return a

    @functools.cache
    def simulate(resources, robots, time, next_build):
        if time == 0:
            return resources[GEODE]

        next_robots = robots
        next_resources = resources

        # building
        if next_build != None:
            l = list(robots)
            l[next_build] += 1
            next_robots = tuple(l)

            c = costs[next_build]
            next_resources = (
                next_resources[ORE] - c[ORE],
                next_resources[CLAY] - c[CLAY],
                next_resources[OBSIDIAN] - c[OBSIDIAN],
                next_resources[GEODE] - c[GEODE],
            )

        # collection
        next_resources = (
            next_resources[ORE] + robots[ORE],
            next_resources[CLAY] + robots[CLAY],
            next_resources[OBSIDIAN] + robots[OBSIDIAN],
            next_resources[GEODE] + robots[GEODE],
        )

        # picking what to build
        best = -1
        afford_set = can_afford(next_resources, next_robots)

        if GEODE in afford_set:
            best = simulate(next_resources, next_robots, time-1, GEODE)
        else:
            for next_build in afford_set:
                outcome = simulate(next_resources, next_robots, time-1, next_build)
                best = max(best, outcome)

        return best

    return simulate((0, 0, 0, 0), (1, 0, 0, 0), simulation_time, None)

with open('input') as f:
    lines = f.read().splitlines()

    # parsing
    blueprint_data = []
    for line in lines:
        g = re.match(r"^Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.$", line).groups()
        data = tuple(map(int, g))

        costs = (
            (data[1], 0, 0, 0),
            (data[2], 0, 0, 0),
            (data[3], data[4], 0, 0),
            (data[5], 0, data[6], 0),
        )

        blueprint_data.append((data[0], costs))

    # part 1
    print("Warning - this might take about 20 minutes to complete")
    quality_level = 0

    for blueprint_id, costs in blueprint_data:
        geodes_opened = calc_blueprint(costs, 24)
        quality_level += (blueprint_id * geodes_opened)

    print(quality_level)

    # part 2
    results = []
    for blueprint_id, costs in blueprint_data[:3]:
        geodes_opened = calc_blueprint(costs, 32)
        results.append(geodes_opened)

    print(math.prod(results))
