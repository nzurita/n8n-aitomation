import sys, json, urllib.request

token = sys.argv[1]
for name in sys.argv[2:]:
    url = f"https://api.telegram.org/bot{token}/getStickerSet?name={name}"
    d = json.load(urllib.request.urlopen(url))
    if not d.get("ok"):
        print(f"// {name}: ERROR {d.get('description')}")
        continue
    r = d["result"]
    print(f"// {r['title']} ({name}) - {len(r['stickers'])} stickers")
    for st in r["stickers"]:
        print(f"  '{st['file_id']}', // {st.get('emoji', '')}")

