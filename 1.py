def can_eat(horse, victim):
    if (abs(horse[0] - victim[0]) == 1 and abs(horse[1] - victim[1]) == 2) or (abs(horse[0] - victim[0]) == 2 and abs(horse[1] - victim[1]) == 1):
        return True
    else:
        return False

print(can_eat((5, 5), (6, 567)))