1.
print("""
問題1
太郎さんはりんごを10個買いました。
その後、先輩が5個くれました。
翌日の午前、家に遊びにきたAさんに2個あげました。
午後には青森の実家から、ちょうど倍の数になる分のりんごが送られてきました。
食べきれないため、BさんとCさんと自分で当分しようと思いました。
今回はその場で食べるわけではないためあまりを出す形にしました。
さて、一人当たりのりんごの数と当分できずに余った数を答えなさい。

この問題を一緒に解いてみましょう!
""".strip())

bought = int(input("買った数を入力>>"))
received = int(input("貰った数を入力>>"))
given = int(input("あげた数を入力>>"))
multiplier = int(input("倍率を入力>>"))
people = int(input("人数を入力>>"))
total_apples = (bought + received - given) * multiplier
per_person = total_apples // people
leftover = total_apples % people

print(f"解答\n一人当たり{per_person}個\n余り{leftover}個")