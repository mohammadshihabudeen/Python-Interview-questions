inp=[1,1,1,2,3,4,3,2,3,2,3,4,6,6,2,1,2,3,1,6,2,3,4,5,3,2,3,4,1,2,6,3,4,2,1,2,3,6,4,5,3,6,5,4,5,6,4,3,3,5,1]
ladder={2:7,9:15,18:27,33:46}
snake={12:3,21:7,30:13,37:22,49:40}
def player(score,ele):
    score+=ele
    if score in ladder:
        score=ladder[score]
    elif score in snake:
        score=snake[score]
    return score
p1=p2=p3=True
s1=s2=s3=False
score1=score2=score3=0
for ele in inp:
    if p1:
        if ele==1:
            s1=True
        if s1:
            score1=player(score1,ele)
            if score1>=50:
                print("shihab wins")
                break
        p1=False
        p2=True
    elif p2:
        if ele==1:
            s2=True
        if s2:
            score2=player(score2,ele)
            if score2>=50:
                print("mohab wins")
                break
        p2=False
        p3=True
    else:
        if ele==1:
            s3=True
        if s3:
            score3=player(score3,ele)
            if score3>=50:
                print("shimo wins")
                break
        p3=False
        p1=True
    
    