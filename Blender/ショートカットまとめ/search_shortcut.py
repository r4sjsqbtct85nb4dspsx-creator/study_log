import json
import sys

def search_shortcut(query):
    # JSONファイルを読み込む
    try:
        with open('shortcut.json', 'r', encoding = 'utf-8') as f:
            data = json.load(f)

        results = []
        for section, items in data.items():
            for key, value in items.items():
                if query in key or query in value:
                    results.append(f"[{section}]{key}: {value}")

        if results:
            print(f"\n--- '{query}'の検索結果 ---")
            for res in results:
                print(res)

        else:
            print(f"\n'{query}' は見つかりませんでした。")

    except FileNotFoundError:
        print("エラー: short_cut.json が見つかりません。")

if __name__ == "__main__":
    # 引数が渡されているか確認
    if len(sys.argv) > 1:
        search_query = sys.argv[1]
        search_shortcut(search_query)
    else:
        print("使い方: python search_shortcut.py 検索ワード")