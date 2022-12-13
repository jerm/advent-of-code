#!/usr/bin/env python3
import click

def do_the_necessary(test):
    file_ext = "test" if test else "txt"
    cycle = 1
    sum_signals = 0
    checkpoints = [20, 60, 100, 140, 180, 220]
    X = 1
    skipped_cycles = 0
    instruction = []
    sprite = [-1, 0, 1]
    screen_pos = 0

    with open(f"day10.{file_ext}", "r") as fp:

        while cycle <= 240:
            if instruction == []:
                instruction = fp.readline().strip().split()

            if cycle in checkpoints:
                sum_signals += cycle * X

            #screen output
            printed = False
            for sprite_pixel in sprite:
                if (screen_pos + sprite_pixel) == X:
                    print("#", end='')
                    printed = True

            if not printed:
                print(".", end='')
            screen_pos += 1

            match instruction:
                case ["addx", *args]:
                    if skipped_cycles > 0:
                        X += int(instruction[1])
                        instruction = []
                        skipped_cycles -= 1
                    else:
                        skipped_cycles = 1
                case ["noop"]:
                    instruction = []

            if cycle % 40 == 0:
                print("")
                screen_pos = 0
            cycle += 1

    print("")
    print(sum_signals)


@click.command()
@click.option("--test/--no-test", default=False)
@click.option("--debug/--no-debug", default=False)
def main(test,debug):

    do_the_necessary(test)


if __name__ == "__main__":
    main()

