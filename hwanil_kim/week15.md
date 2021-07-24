## Q.48

#### 문제. https://programmers.co.kr/learn/courses/30/lessons/42578

#### 나의 풀이
- 의상 종류가 Key, 의상 이름이 value(list)인 dict를 만든다.
- 경우의 수 구하듯이 의상의 종류 수를 서로 곱해주면 된다.
- 이때, 의상을 안입는 경우도 있으므로 각 의상에 +1을 해준다.
- 하지만 아무것도 안입는 경우는 없으므로 전체 결과에서 -1을 해준다.
```
def solution(clothes):
    clothes_dict = dict()
    for cloth in clothes:
        if cloth[1] in clothes_dict:
        	clothes_dict[cloth[1]].append(cloth[0])
        else:
            clothes_dict[cloth[1]] = [cloth[0]]
    res = 1
    for k in clothes_dict.keys():
        res *= len(clothes_dict[k]) + 1
    return res - 1
```

## Q.49

#### 문제. https://programmers.co.kr/learn/courses/30/lessons/42579
![Screen Shot 2021-07-24 at 12 43 33 PM](https://user-images.githubusercontent.com/60768642/126856408-3b96f247-2d07-4d4a-9912-dd685d77ba80.png)
![Screen Shot 2021-07-24 at 12 43 37 PM](https://user-images.githubusercontent.com/60768642/126856411-69c22805-d06c-4fe0-8d45-2b4fc285ea11.png)

#### 나의 풀이
```
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

```
- 어려워서 결국 다른 블로그를 참고해서 풀었다.
- 해결로직을 차근차근 복기해보자.
#### 풀이과정
- 각 장르 별로 전체 재생수를 구한다.
  - `play_total = {'classic': 1450, 'pop': 3100}`
- 위에서 구한 값을 재생수를 기준으로 내림차순 정렬한다.
  - `total_sort = [('pop', 3100), ('classic', 1450)]`
- 각 장르별로 재생수와 인덱스를 구한다.
- `play_info = {'classic': [(800, 3), (500, 0), (150, 2)], 'pop': [(2500, 4), (600, 1)]}`
  - 위에서 구한 값을 재생수별로 내림정렬하고, 다시 인덱스별로 오름 정렬한다.
- 높은 재생수를 기록한 장르부터 인덱스를 2개씩 더해 결과를 리턴한다. 