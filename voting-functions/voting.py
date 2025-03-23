# preferences.candidates() => list of candidates in form [1, ... , n]
# preferences.voters() =>  list of voters in form [1, ... , m]
# preferences.get_preference(candidate, voter) =>  integer rank of voter's rank for candidate

def tie_breaker_and_winner(preferences, scoring, tie_break):
    ''' Take in a scoring dictionary, a preferences object and a tie_break agent to produce an answer '''
    # Find the candidates with the highest score from the respective rule given
    winners = [c for c in preferences.candidates() if scoring[c] == max(scoring.values())]
    # If there is only 1 candidate with the highest score, return that candidate
    if len(winners) == 1:
        return winners[0]
    else:
        # If there is more than one candidate with the highest score...
        # create a list with the highest scoring candidate ordered by the preferences of the tie_break agent
        return sorted(winners, key=lambda c: preferences.get_preference(c, tie_break))[0]

def dictatorship(preferences, agent):
    ''' Dictatorship Rule '''
    # Raise error if agent is not valid
    if agent not in preferences.voters():
        raise ValueError("Invalid agent!")

    for i in preferences.candidates():
        # if preference of agent for candidate is 0, return candidate
        if preferences.get_preference(i, agent) == 0:
            # return agent with the highest preference of the dictator agent
            return i

def scoring_rule(preferences, score_vector, tie_break_agent):
    ''' Scoring Rule '''
    # create a dictionary storing score for each candidate based on rule
    scoring = {i: 0 for i in preferences.candidates()}

    # raise error as requested if score_vector doesn't match candidate length
    if len(score_vector) != len(preferences.candidates()):
        raise ValueError("Score vector is the wrong length!")

    score_vector = sorted(score_vector, reverse=True)
    # loop through all voters and candidates
    for v in preferences.voters():
        for c in preferences.candidates():
            # add the deserved score to the scoring dictionary using the values in the score_vector
            scoring[c] += score_vector[preferences.get_preference(c, v)]

    return tie_breaker_and_winner(preferences, scoring, tie_break_agent)

def plurality(preferences, tie_break):
    ''' Plurality Rule '''
    # create a dictionary storing score for each candidate based on rule
    scoring = {i: 0 for i in preferences.candidates()}

    # loop through all voters and candidates
    for v in preferences.voters():
        for c in preferences.candidates():
            if preferences.get_preference(c, v) == 0:
                # find the top choice of each voter and add 1 to their score in the scoring dictionary
                scoring[c] += 1

    return tie_breaker_and_winner(preferences, scoring, tie_break)

def veto(preferences, tie_break):
    ''' Veto Rule '''
    # create a dictionary storing score for each candidate based on rule
    scoring = {i: 0 for i in preferences.candidates()}

    # loop through all voters and candidates
    for v in preferences.voters():
        for c in preferences.candidates():
            if preferences.get_preference(c, v) != (len(preferences.candidates()) - 1):
                # find all candidates who are not last in the voter's preference and add 1 to their score in the scoring dictionary
                scoring[c] += 1

    return tie_breaker_and_winner(preferences, scoring, tie_break)

def borda(preferences, tie_break):
    ''' Borda Rule '''
    # Essentially same as the scoring_rule with a scoring vector of [0 to n-1]
    score_vector = range(len(preferences.candidates()), 0, -1)
    # The scoring rule already sorts the vector, assignes n-j to the score and includes the tie_breaker function
    # Since the vector is sorted from highest to lowest we will get n-j and not just j, where j is the get_preference output of a voter for a candidate
    return scoring_rule(preferences, score_vector, tie_break)

def STV(preferences, tie_break):
    ''' STV Rule '''
    # create a set of non-eliminated candidates
    survivors = set(preferences.candidates())

    while len(survivors) > 1:
        # create a dictionary storing score for each candidate based on rule
        scoring = {i: 0 for i in survivors}
        for v in preferences.voters():
            # create preference profile for voters that only include surviving candidates
            reduced_preference = sorted(survivors, key=lambda c: preferences.get_preference(c, v))
            # add 1 to the scoring dictionary to the candidate who is the top preference in the reduced_preference list
            scoring[reduced_preference[0]] += 1

        for c in scoring:
            # remove lowest value candidate(s), if only 1 survivor is left the loop will break
            if min(scoring.values()) != max(scoring.values()):
                if scoring[c] == min(scoring.values()):
                    survivors.remove(c)
            else:
                # STV tie-breaker, list withth only 1 value: the winner of the tie_break agent's preference.
                # This will mean len(survivors) = 1, breaking the while loop
                survivors = [sorted(scoring, key=lambda c: preferences.get_preference(c, tie_break))[0]]

    return list(survivors)[0]
