#!/usr/bin/env python3
import click

def do_the_necessary(test):
    file_ext = "test" if test else "txt"
    num_knots = 2
    rope = []

    def calc_t_move(rope, direction=None):
        if direction:
            match direction:
                case "U":
                    rope[0][1] += 1
                case "D":
                    rope[0][1] -= 1
                case "L":
                    rope[0][0] -= 1
                case "R":
                    rope[0][0] += 1

        xd = rope[0][0] - rope[1][0]
        yd = rope[0][1] - rope[1][1]
        if abs(yd) > 1 or abs(xd) > 1:
            if rope[0][0] > rope[1][0]:
                rope[1][0] +=1
                direction = 'R'
            elif rope[0][0] < rope[1][0]:
                rope[1][0] -=1
                direction = 'L'
            if rope[0][1] > rope[1][1]:
                rope[1][1] +=1
                direction = 'U'
            elif rope[0][1] < rope[1][1]:
                rope[1][1] -=1
                direction = 'D'
        if len(rope) > 2:
            rope = [rope[0], calc_t_move(rope[1:])]
        return rope


    for _ in range(num_knots):
        rope.append([0,0])

    locations = set()
    with open(f"day9.{file_ext}", "r") as fp:
        for line in fp.readlines():
            [direction, distance_str] = line.strip().split(" ")
            distance = int(distance_str)
            for _ in range(distance):
                calc_t_move(rope, direction)
                locations.add(tuple(rope[-1]))

    print(len(locations))


@click.command()
@click.option("--test/--no-test", default=False)
@click.option("--debug/--no-debug", default=False)
def main(test,debug):

    do_the_necessary(test)


if __name__ == "__main__":
    main()

