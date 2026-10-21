# 表示文
print("""

○○中学3年5組の3回分のテストの結果を発表します。
自分の名前を入力すると結果が表示されるので、各自で確認するようにしてください。

平均点が50点未満なら、
xx月に開講される補講に参加してください。
(具体的な日程は追ってご連絡します。)

""".strip())

# データ
members_scores = {
    "田中": [50, 60, 40],
    "佐藤": [30, 40, 50],
    "鈴木": [80, 90, 80]
}

# 名前入力
name = input("あなたの名前を入力してください >>")

if name in members_scores:
   data = members_scores.get(name)
   print(f'あなたの得点は、第一回は{data[0]}点、第二回は{data[1]}点、第三回は{data[2]}点です。')

   total = sum(data)
   avg = total / len(data)
  
   if avg >= 50:
      print(f'平均点は{avg:.2f}点です。次も頑張りましょう。')
   else:
      print(f"平均点は{avg:.2f}点です。補講に参加してください。")

else:
   print(f'{name}さんの名前は見つかりませんでした。')