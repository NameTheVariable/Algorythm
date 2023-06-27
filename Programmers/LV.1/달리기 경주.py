def solution(players, callings):
    # players.push(answer)
    # if callings in players:
    #   players[i].swap(callings)
    # resturn answer
    answer = []
    for i in callings:
        index = players.index[i]
        players[index], players[index-1] = players[index-1], players[index]
    return players
