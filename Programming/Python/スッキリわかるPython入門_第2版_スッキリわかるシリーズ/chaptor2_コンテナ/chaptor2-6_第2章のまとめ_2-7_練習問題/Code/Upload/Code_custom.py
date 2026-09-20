1.
scores = []
scores.append(int(input('国語の点数>>')))
scores.append(int(input('算数の点数>>')))
scores.append(int(input('理科の点数>>')))
scores.append(int(input('社会の点数>>')))
scores.append(int(input('英語の点数>>')))
print(f'合計{sum(scores)}点 平均{sum(scores) / len(scores)}点')

2.
user1 = {'読書', '釣り', '料理', 'ゲーム', '散歩'}
user2 = {'料理', '散歩', '旅行', 'ガーデニング', '読書'}
input('心の準備ができたらEnterキーを押してください')
intersection = user1 & user2
union = user1 | user2
match_rate = len(intersection) / len(union) * 100
print(f'相性度は{match_rate}%です！')