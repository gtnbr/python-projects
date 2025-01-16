def dictatorship(preferences, agent):
    ''' Dictatorship Rule '''
    if agent not in preferences.voters():
        raise ValueError("Invalid agent!")
    for i in preferences.candidates():
        if preferences.get_preference(i, agent) == 0:
            return i

def scoring_rule(preferences, score_vector, tie_break_agent):
    ''' Scoring Rule '''
    scoring = {i: 0 for i in preferences.candidates()}
    if len(score_vector) != len(preferences.candidates()):
        raise ValueError("Score vector is the wrong length!")
    score_vector = sorted(score_vector, reverse=True)
    for v in preferences.voters():
        for c in preferences.candidates():
            scoring[c] += score_vector[preferences.get_preference(c, v)]
    winners = [c for c in preferences.candidates() if scoring[c] == max(scoring.values())]
    if len(winners) == 1:
        return winners[0]
    return sorted(winners, key=lambda c: preferences.get_preference(c, tie_break))[0]

def plurality(preferences, tie_break):
    ''' Plurality Rule '''
    score_vector = [1] + [0 for i in range(len(preferences.candidates())-1)]
    return scoring_rule(preferences, score_vector, tie_break)

def veto(preferences, tie_break):
    ''' Veto Rule '''
    score_vector = [1 for i in range(len(preferences.candidates())-1)] + [0]
    return scoring_rule(preferences, score_vector, tie_break)

def borda(preferences, tie_break):
    ''' Borda Rule '''
    score_vector = range(len(preferences.candidates()), 0, -1)
    return scoring_rule(preferences, score_vector, tie_break)

def STV(preferences, tie_break):
    ''' STV Rule '''
    survivors = set(preferences.candidates())
    while len(survivors) > 1:
        scoring = {i: 0 for i in survivors}
        for v in preferences.voters():
            reduced_preference = sorted(survivors, key=lambda c: preferences.get_preference(c, v))
            scoring[reduced_preference[0]] += 1
        for c in scoring:
            if min(scoring.values()) != max(scoring.values()):
                if scoring[c] == min(scoring.values()):
                    survivors.remove(c)
            else:
                survivors = [sorted(scoring, key=lambda c: preferences.get_preference(c, tie_break))[0]]
    return list(survivors)[0]
