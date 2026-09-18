#List:マラソン大会参加者を順位が高い順に登録する
members = ["A", "B", "C", "D", "E"]
scores = [1, 2, 3, 4, 5] #ディクショナリへの変換のため追加
print(f"優勝は{members[:1]}")

#Dictionary:受験者のテストの点数を対応させて登録する
scores = {"A":70, "B":60, "C":50}
print(scores["A"])

#リストをタプル・セット・ディクショナリに変換
print(tuple(members)) #タプルに変換
print(set(members)) #セットに変換
print(dict(zip(members, scores))) #ディクショナリに変換

#ディクショナリをキーだけ・値だけ・キーと値の3種類でリストに変換
#タプル・セットもlistの部分を変更することで変換可能
print(list(scores.keys())) #キーだけ変換
print(list(scores.values())) #値だけ変換
print(list(scores.items())) #キーと値を変換