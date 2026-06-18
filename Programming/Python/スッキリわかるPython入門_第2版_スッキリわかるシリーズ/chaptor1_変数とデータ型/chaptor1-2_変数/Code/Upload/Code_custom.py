1
name = input("あなたの名前を入力してください>>")
print("ようこそ、" + name + "、この世界の救世主様。")

2
print("""
問題1
太郎さんはりんごを10個買いました。
その後、先輩が5個くれました。
翌日の午前、家に遊びにきたAさんに2個あげました。
午後には青森の実家から、ちょうど倍の数になる分のりんごが送られてきました。
食べきれないため、BさんとCさんと自分で当分しようと思いました。
今回はその場で食べるわけではないためあまりを出す形にしました。
さて、一人当たりのりんごの数と当分できずに余った数を答えなさい。
""".strip())

number_of_people = 3
initial_apples = 10
gifted_apples = 5
given_to_A = 2
doubled_factor = 2

current_number = (initial_apples + gifted_apples - given_to_A) * doubled_factor
share_per_person , leftover = current_number // number_of_people , current_number % number_of_people

print("回答")
print("一人当たり個数")
print(share_per_person)
print("余り個数")
print(leftover)

#なお、今回は str() や f-string は学習範囲にないため使用していない。