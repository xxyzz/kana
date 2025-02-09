import subprocess
from pathlib import Path
from dataclasses import dataclass

from jinja2 import Environment, PackageLoader, select_autoescape
import genanki


@dataclass
class Td:
    chinese: str = ""
    hiragana: str = ""
    audio: str = ""
    romanization: str = ""
    stroke_order: str = ""


@dataclass
class Row:
    th: str
    td_list: list[Td]


def create_anki_deck(rows: list[Row]) -> None:
    model = genanki.Model(
        2145308593,
        "Hiragana",
        fields=[
            {"name": "Chinese"},
            {"name": "Hiragana"},
            {"name": "audio"},
            {"name": "romanization"},
            {"name": "stroke_order"},
        ],
        templates=[
            {
                "name": "Hiragana",
                "qfmt": '<span lang="ja">{{Hiragana}}</span>',
                "afmt": '{{FrontSide}}<p><span lang="ja">{{Chinese}}</span> <span lang="zh">{{Chinese}}</span></p><p>{{romanization}}</p><p>{{audio}}</p><p>{{stroke_order}}</p>',
            }
        ],
        css="""
@font-face {
  font-family: "hengshancaoshu";
  src: url("_HengShanMaoBiCaoShu-2.ttf");
}

@font-face {
  font-family: "Klee One";
  src: url("_KleeOne-Regular.ttf");
}

.card {
  font-size: xxx-large;
  text-align: center;
}

p {
  margin: auto;
}

span[lang="ja"] {
  font-family: "Klee One", serif;
  font-weight: 400;
  font-style: normal;
}

span[lang="zh"] {
  font-family: "hengshancaoshu", serif;
  font-weight: 400;
  font-style: normal;
}
""",
    )
    deck = genanki.Deck(2013441022, "Hiragana")
    package = genanki.Package(deck)
    for row in rows:
        for td in row.td_list:
            if td.chinese == "":
                continue
            note = genanki.Note(
                model=model,
                fields=[
                    td.chinese,
                    td.hiragana,
                    f"[sound:sounds/{td.audio}]" if td.audio != "" else "",
                    td.romanization,
                    f'<img src="images/{td.stroke_order}">' if td.stroke_order != "" else "",
                ],
            )
            deck.add_note(note)

    package.media_files.extend(
        ["fonts/_HengShanMaoBiCaoShu-2.ttf", "fonts/_KleeOne-Regular.ttf"]
    )
    package.write_to_file("hiragana.apkg")


if __name__ == "__main__":
    env = Environment(
        loader=PackageLoader("kana"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("hiragana.html")

    Path("_site").mkdir(exist_ok=True)
    with open("_site/hiragana.html", "w", encoding="utf-8") as f:
        rows = [
            Row(
                "",
                [
                    Td("安", "あ", "Ja-A.oga", "a", "あ-bw.svg"),
                    Td("以", "い", "", "i", "い-bw.svg"),
                    Td("宇", "う", "Ja-U.oga", "u", "う-bw.svg"),
                    Td("衣", "え", "Ja-E.oga", "e", "え-bw.svg"),
                    Td("於", "お", "Ja-O.oga", "o", "お-bw.svg"),
                ],
            ),
            Row(
                "k",
                [
                    Td("加", "か", "Ja-ka.ogg", "ka", "か-bw.svg"),
                    Td("幾", "き", "", "ki", "き-bw.svg"),
                    Td("久", "く", "", "ku", "く-bw.svg"),
                    Td("計", "け", "", "ke", "け-bw.svg"),
                    Td("己", "こ", "", "ko", "こ-bw.svg"),
                ],
            ),
            Row(
                "s",
                [
                    Td("左", "さ", "", "sa", "さ-bw.png"),
                    Td("之", "し", "Ja-Shi.oga", "shi", "し-bw.png"),
                    Td("寸", "す", "", "su", "す-bw.png"),
                    Td("世", "せ", "", "se", "せ-bw.png"),
                    Td("曽", "そ", "", "so", "そ-bw.png"),
                ],
            ),
            Row(
                "t",
                [
                    Td("太", "た", "", "ta", "た-bw.png"),
                    Td("知", "ち", "Ja-Chi_2.oga", "chi", "ち-bw.png"),
                    Td("川", "つ", "Ja-Tsu.oga", "tsu", "つ-bw.png"),
                    Td("天", "て", "", "te", "て-bw.png"),
                    Td("止", "と", "", "to", "と-bw.png"),
                ],
            ),
            Row(
                "n",
                [
                    Td("奈", "な", "", "na", "な-bw.png"),
                    Td("仁", "に", "Ja-2-ni.ogg", "ni", "に-bw.png"),
                    Td("奴", "ぬ", "", "nu", "ぬ-bw.png"),
                    Td("祢", "ね", "", "ne", "ね-bw.png"),
                    Td("乃", "の", "", "no", "の-bw.png"),
                ],
            ),
            Row(
                "h",
                [
                    Td("波", "は", "", "ha", "は-bw.png"),
                    Td("比", "ひ", "Ja-Hi.oga", "hi", "ひ-bw.png"),
                    Td("不", "ふ", "Ja-Fu.oga", "fu", "ふ-bw.png"),
                    Td("部", "へ", "", "he", "へ-bw.png"),
                    Td("保", "ほ", "", "ho", "ほ-bw.png"),
                ],
            ),
            Row(
                "m",
                [
                    Td("末", "ま", "", "ma", "ま-bw.png"),
                    Td("美", "み", "", "mi", "み-bw.png"),
                    Td("武", "む", "", "mu", "む-bw.png"),
                    Td("女", "め", "", "me", "め-bw.png"),
                    Td("毛", "も", "", "mo", "も-bw.png"),
                ],
            ),
            Row(
                "y",
                [
                    Td("也", "や", "", "ya", "や-bw.png"),
                    Td(),
                    Td("由", "ゆ", "", "yu", "ゆ-bw.png"),
                    Td(),
                    Td("与", "よ", "", "yo", "よ-bw.svg"),
                ],
            ),
            Row(
                "r",
                [
                    Td("良", "ら", "Ja-Ra.oga", "ra", "ら-bw.png"),
                    Td("利", "り", "Ja-Ri.oga", "ri", "り-bw.png"),
                    Td("留", "る", "Ja-Ru.oga", "ru", "る-bw.png"),
                    Td("礼", "れ", "Ja-Re.oga", "re", "れ-bw.png"),
                    Td("呂", "ろ", "Ja-Ro.oga", "ro", "ろ-bw.png"),
                ],
            ),
            Row(
                "w",
                [
                    Td("和", "わ", "", "wa", "わ-bw.png"),
                    Td(),
                    Td("无", "ん", "", "n", "ん-bw.png"),
                    Td(),
                    Td("遠", "を", "Ja-O.oga", "o", "を-bw.png"),
                ],
            ),
        ]
        f.write(template.render(rows=rows))
        create_anki_deck(rows)
