input_str = "abbaaaabbbbaaaaabaababaaaaababbaabaabaababaaabbababababaabaaabbbbaaaaabbaabbb"
setA = setB = scoreA = scoreB = winA = winB = 0
tieA = tieB = 0
tie = False

for char in input_str:
    if tie:
        if char == "a":
            tieA += 1
        else:
            tieB += 1
        if tieA == 7:
            winA += 1
            setA = tieA = scoreA = 0
            setB = tieB = scoreB = 0
            tie = False
        elif tieB == 7:
            winB += 1
            setA = tieA = scoreA = 0
            setB = tieB = scoreB = 0
            tie = False
    else:
        if char == "a":
            scoreA += 1
            if (scoreA == 4 and scoreB < 3) or (scoreA > 4 and scoreA - scoreB >= 2):
                setA += 1
                scoreA = scoreB = 0
                if (setA == 6 and setB < 5) or (setA > 6 and setA - setB >= 2):
                    winA += 1
                    setA = setB = 0
                elif setA >= 6 and setA == setB:
                    tie = True
            elif scoreA >= 4 and scoreA == scoreB:
                scoreA = scoreB = 3
        else:
            scoreB += 1
            if (scoreB == 4 and scoreA < 3) or (scoreB > 4 and scoreB - scoreA >= 2):
                setB += 1
                scoreB = scoreA = 0
                if (setB == 6 and setA < 5) or (setB > 6 and setB - setA >= 2):
                    winB += 1
                    setA = setB = 0
                elif setB >= 6 and setA == setB:
                    tie = True
            elif scoreB >= 4 and scoreB == scoreA:
                scoreA = scoreB = 3

if winA > winB:
    print('A is the winner')
elif winB > winA:
    print("B is the winner")
else:
    print("It's a tie")

print("Player A wins:", winA)
print("Player B wins:", winB)
