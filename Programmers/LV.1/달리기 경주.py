def solution(players, callings):
    # players.push(answer)
    # if callings in players:
    #   players[i].swap(callings)
    # resturn answer
    answer = []
    result = {players: i for i, players in enumerate(players)}
    for who in callings:
        idx = result[who]
        result[who] -= 1
        result[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players
