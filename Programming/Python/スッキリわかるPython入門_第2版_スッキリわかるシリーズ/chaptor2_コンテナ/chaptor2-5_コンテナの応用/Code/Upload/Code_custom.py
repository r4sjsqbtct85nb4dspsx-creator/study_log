print("""
問題5
以下の生徒たちを、
1,生徒会・部活・委員会すべてに所属している者
2,生徒会と部活両方に所属している者
3,生徒会と委員会両方に所属している者
4,部活と委員会に両方所属している者
5,生徒会のみに所属している者
6,部活のみに所属している者
7,委員会のみに所属している者
に分類しなさい。

また、コンテナの種類をセットから、
councilをリスト・clubをタプル・committeeをリストに変換して表示しなさい。
""".strip())


council = {'松田', '浅木', '工藤', '遠野'}
club = {'松田', '工藤', '紫藤', '夏目', '橘', '伊藤', '日向', '柴田'}
committee = {'松田', '浅木', '紫藤', '橘', '日向', '柴田', '神田', '七海', '大竹', '岡沢', '渡辺'}

print(council & club & committee)
print(council & club - committee)
print(council & committee - club)
print(club & committee - council)
print(council - club - committee)
print(club - council - committee)
print(committee- council - club)

print(list(council))
print(tuple(club))
print(list(committee))