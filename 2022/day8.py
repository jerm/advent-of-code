#!/usr/bin/env python3
import click

def day8(test):
    file_ext = "test" if test else "txt"
    forest_rows = []
    visible_trees = 0
    best_view = False

    def count_row(row):
        nonlocal best_view
        visible_in_row = 0
        tallest_in_view = -1
        for tree in row:
            view = 0
            if tree['height'] > tallest_in_view:
                tallest_in_view = tree['height']
                if not tree['visible']:
                    visible_in_row += 1
                    tree['visible'] = True


            # determine view
            possible_view = row[row.index(tree)+1:]
            if possible_view == []:
                view = 0
            still_in_view = True
            for next_tree in row[row.index(tree)+1:]:
                if still_in_view:
                    view += 1
                    if next_tree['height'] >= tree['height']:
                        still_in_view = False
            if view > 0:
                tree['view'] *= view
            tree['views'].append(view)
            if tree['view'] > best_view:
                best_view = tree['view']


        # Determine visibility
        tallest_in_view = -1
        row.reverse()
        for tree in row:
            if tree['height'] > tallest_in_view:
                tallest_in_view = tree['height']
                if not tree['visible']:
                    visible_in_row += 1
                    tree['visible'] = True
        if visible_in_row > len(row):
            visible_in_row -= 1
        return visible_in_row

    def process_forest_rows(forest_trees):
        nonlocal visible_trees
        for row in forest_rows:
            row = list(row)
            new_trees = count_row(list(row))
            visible_trees += new_trees

    with open(f"day8.{file_ext}", "r") as fp:
        for line in fp.readlines():
            row = []
            for tree in line.strip():
                row.append({"height": int(tree), "visible": False, "view": 1, "views": []})
            forest_rows.append(row)

    for row in forest_rows:
        forest = [tree['height'] for tree in row]

    for _ in [0,90,180,270]:
        process_forest_rows(forest_rows)

        # rotate the matrix 90 degrees
        forest_rows = list(zip(*forest_rows))[::-1]

    print(f"Visible trees: {visible_trees}")
    print(f"Best view: {best_view}")



@click.command()
@click.option("--test/--no-test", default=False)
@click.option("--debug/--no-debug", default=False)
def main(test,debug):

    day8(test)


if __name__ == "__main__":
    main()

