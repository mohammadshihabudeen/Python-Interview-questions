def tennis_game(input_str):
    scores = {'a': 0, 'b': 0}
    sets = {'a': 0, 'b': 0}
    win_points = {'a': 0, 'b': 0}
    tie_break = False
    tieA=tieB=0
    for char in input_str:
        if tie_break:
            if char=="a":
                tieA+=1
            else:
                tieB+=1
            if tieA==7:
                tieA=0
                scores["a"]=0
                scores["b"]=0
                sets["a"]=0
                sets["b"]=0
                win_points["a"]+=1
                tie_break=False
            elif tieB==7:
                tieB=0
                scores["a"]=0
                scores["b"]=0
                sets["a"]=0
                sets["b"]=0
                win_points["b"]+=1
                tie_break=False
        else:
            if char in scores:
                scores[char] += 1
            if scores['a'] >= 4 and scores['a'] - scores['b'] >= 2:
                if sets['a'] < 6 or sets['a'] - sets['b'] < 1:
                    sets['a'] += 1
                else:
                    win_points['a'] += 1
                scores['a'] = 0
                scores['b'] = 0

            elif scores['b'] >= 4 and scores['b'] - scores['a'] >= 2:
                if sets['b'] < 6 or sets['b'] - sets['a'] < 1:
                    sets['b'] += 1
                else:
                    win_points['b'] += 1
                scores['a'] = 0
                scores['b'] = 0

            if sets['a'] >= 6 and sets['a'] - sets['b'] >= 1:
                win_points['a'] += 1
                sets['a'] = 0
                sets['b'] = 0
                scores['a'] = 0
                scores['b'] = 0
            elif sets['b'] >= 6 and sets['b'] - sets['a'] >= 1:
                win_points['b'] += 1
                sets['a'] = 0
                sets['b'] = 0
                scores['a'] = 0
                scores['b'] = 0
            if sets['a'] == 6 and sets['b'] == 6:
                tie_break = True
        return f"Player A: {sets['a']} win(s), Player B: {sets['b']} win(s)"

input_string ="abbaaaabbbbaaaaabaababaaaaababbaabaabaababaaabbababababaabaaabbbbaaaaabbaabbb"
result = tennis_game(input_string)
print(result)
