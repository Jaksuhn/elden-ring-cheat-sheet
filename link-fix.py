import re


def convert_spaces(match_obj):
    fextra = "https://eldenring.wiki.fextralife.com/"
    category = match_obj.group(1)
    num = match_obj.group(2)
    item = match_obj.group(3)
    item_fix = item
    if item.endswith(" +1") or item.endswith(" +2"):
        item_fix = item[: -len(" +1")]
    return f'<li data-id="{category}_{num}"><a href="{fextra + item_fix.replace(" ", "+")}">{item}</a></li>'


with open("index.html") as r:
    data = re.sub(
        r'<li data-id="([a-z]*)_(.*)"><a href="">(.*)<\/a><\/li>',
        convert_spaces,
        r.read(),
    )

with open("index.html", "w") as w:
    w.write(data)
