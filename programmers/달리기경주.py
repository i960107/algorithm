def solution(players, callings):
    ranks = {name: index for index, name in enumerate(players, 0)}
    for winner in callings:
        winner_now = ranks[winner]
        loser_now = winner_now - 1
        loser = players[loser_now]
        players[loser_now], players[winner_now] = winner, loser
        ranks[loser] = winner_now
        ranks[winner] = loser_now
    return players
