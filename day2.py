#!/usr/bin/env python3

score = 0
correct_score = 0

def i_win(os):
    global correct_score
    global line
    correct_score += 6
    ss = os + 1
    if ss == 3:
        ss = 0
    print(line, f"win, adding 6 + {ss}")
    correct_score += ss + 1

def i_draw(os):
    global correct_score
    global line
    print(line, f"draw, adding 3 + {os}")
    correct_score += 3
    correct_score += os + 1

def i_lose(os):
    global correct_score
    global line
    ss = os - 1
    if ss == -1:
        ss = 2
    print(line, f"loss, adding {ss}")
    correct_score += ss + 1

def win(ss):
    global score
    global line
    print(line, f"win, adding 6 + {ss}")
    score += 6
    score += ss + 1

def draw(ss):
    global score
    global line
    print(line, f"draw, adding 3 + {ss}")
    score += 3
    score += ss + 1

def loss(ss):
    global score
    global line
    print(line, f"loss, adding {ss}")
    score += ss + 1

opponent_throws = ['A','B','C']
self_throws = ['X','Y','Z']

print("Reading RPS data...")

with open("day2.txt", "r") as fp:
    for line in fp.readlines():
        line = line.strip()
        ot,st = line.split(" ")
        os = opponent_throws.index(ot)
        ss = self_throws.index(st)
        match ss - os:
            case 0:
                draw(ss)
            case 1:
                win(ss)
            case -1:
                loss(ss)
            case 2 | -2:
                if ss > os:
                    loss(ss)
                else:
                    win(ss)
        match st:
            case "X":
                i_lose(os)
            case "Y":
                i_draw(os)
            case "Z":
                i_win(os)

    print(score)
    print(correct_score)
