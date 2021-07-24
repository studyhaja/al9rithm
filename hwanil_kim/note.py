def solution(genres, plays):
    play_total = dict()
    play_info = dict()
    answer = []
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        play_total[genre] = play_total.get(genre, 0) + play
        play_info[genre] = play_info.get(genre, []) + [(play, i)]

    total_sort = sorted(play_total.items(), key=lambda x: x[1], reverse=True)
    for genre, total in total_sort:
        play_info[genre] = sorted(play_info[genre], key=lambda x: (-x[0], x[1]))
        for play, index in play_info[genre][:2]:
            answer.append(index)
    return answer




genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)

