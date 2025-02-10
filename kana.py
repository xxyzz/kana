from pathlib import Path
from dataclasses import dataclass

from jinja2 import Environment, PackageLoader, select_autoescape
import genanki


@dataclass
class Td:
    chinese: str = ""
    kana: str = ""
    audio: str = ""
    romanization: str = ""
    stroke_order: str = ""


@dataclass
class Row:
    th: str
    td_list: list[Td]


def create_hiragana_deck(rows: list[Row]) -> None:
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
                    td.kana,
                    f"[sound:{td.audio}]" if td.audio != "" else "",
                    td.romanization,
                    f'<img src="{td.stroke_order}">' if td.stroke_order != "" else "",
                ],
            )
            deck.add_note(note)
            if td.audio != "":
                package.media_files.append(f"sounds/{td.audio}")
            if td.stroke_order != "":
                package.media_files.append(f"images/{td.stroke_order}")

    package.media_files.extend(
        ["fonts/_HengShanMaoBiCaoShu-2.ttf", "fonts/_KleeOne-Regular.ttf"]
    )
    package.write_to_file("_site/hiragana.apkg")


def create_hiragana_files(env):
    hiragana_template = env.get_template("hiragana.html")
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
        f.write(hiragana_template.render(rows=rows))
        create_hiragana_deck(rows)


def create_katakana_files(env):
    katakana_template = env.get_template("katakana.html")
    with open("_site/katakana.html", "w", encoding="utf-8") as f:
        rows = [
            Row(
                "",
                [
                    Td("阿", "ア", "Ja-A.oga", "a", "ア-bw.svg"),
                    Td("伊", "イ", "", "i", "イ-bw.svg"),
                    Td("宇", "ウ", "Ja-U.oga", "u", "ウ-bw.svg"),
                    Td("江", "エ", "Ja-E.oga", "e", "エ-bw.svg"),
                    Td("於", "オ", "Ja-O.oga", "o", "オ-bw.svg"),
                ],
            ),
            Row(
                "k",
                [
                    Td("加", "カ", "Ja-ka.ogg", "ka", "カ-bw.svg"),
                    Td("幾", "キ", "", "ki", "キ-bw.svg"),
                    Td("久", "ク", "", "ku", "ク-bw.svg"),
                    Td("介", "ケ", "", "ke", "ケ-bw.svg"),
                    Td("己", "コ", "", "ko", "コ-bw.svg"),
                ],
            ),
            Row(
                "s",
                [
                    Td("散", "サ", "", "sa", "サ-bw.png"),
                    Td("之", "シ", "Ja-Shi.oga", "shi", "シ-bw.png"),
                    Td("須", "ス", "", "su", "ス-bw.png"),
                    Td("世", "セ", "", "se", "セ-bw.png"),
                    Td("曽", "ソ", "", "so", "ソ-bw.png"),
                ],
            ),
            Row(
                "t",
                [
                    Td("多", "タ", "", "ta", "タ-bw.png"),
                    Td("千", "チ", "Ja-Chi_2.oga", "chi", "チ-bw.png"),
                    Td("川", "ツ", "Ja-Tsu.oga", "tsu", "ツ-bw.png"),
                    Td("天", "テ", "", "te", "テ-bw.png"),
                    Td("止", "ト", "", "to", "ト-bw.png"),
                ],
            ),
            Row(
                "n",
                [
                    Td("奈", "ナ", "", "na", "ナ-bw.png"),
                    Td("仁", "ニ", "Ja-2-ni.ogg", "ni", "ニ-bw.png"),
                    Td("奴", "ヌ", "", "nu", "ヌ-bw.png"),
                    Td("祢", "ネ", "", "ne", "ネ-bw.png"),
                    Td("乃", "ノ", "", "no", "ノ-bw.png"),
                ],
            ),
            Row(
                "h",
                [
                    Td("八", "ハ", "", "ha", "ハ-bw.png"),
                    Td("比", "ヒ", "Ja-Hi.oga", "hi", "ヒ-bw.png"),
                    Td("不", "フ", "Ja-Fu.oga", "fu", "フ-bw.png"),
                    Td("部", "ヘ", "", "he", "ヘ-bw.png"),
                    Td("保", "ホ", "", "ho", "ホ-bw.png"),
                ],
            ),
            Row(
                "m",
                [
                    Td("末", "マ", "", "ma", "マ-bw.png"),
                    Td("三", "ミ", "", "mi", "ミ-bw.png"),
                    Td("牟", "ム", "", "mu", "ム-bw.png"),
                    Td("女", "メ", "", "me", "メ-bw.png"),
                    Td("毛", "モ", "", "mo", "モ-bw.png"),
                ],
            ),
            Row(
                "y",
                [
                    Td("也", "ヤ", "", "ya", "ヤ-bw.png"),
                    Td(),
                    Td("由", "ユ", "", "yu", "ユ-bw.png"),
                    Td(),
                    Td("與", "ヨ", "", "yo", "ヨ-bw.png"),
                ],
            ),
            Row(
                "r",
                [
                    Td("良", "ラ", "Ja-Ra.oga", "ra", "ラ-bw.png"),
                    Td("利", "リ", "Ja-Ri.oga", "ri", "リ-bw.png"),
                    Td("流", "ル", "Ja-Ru.oga", "ru", "ル-bw.png"),
                    Td("礼", "レ", "Ja-Re.oga", "re", "レ-bw.png"),
                    Td("呂", "ロ", "Ja-Ro.oga", "ro", "ロ-bw.png"),
                ],
            ),
            Row(
                "w",
                [
                    Td("和", "ワ", "", "wa", "ワ-bw.png"),
                    Td(""),
                    Td("尓", "ン", "", "n", "ン-bw.png"),
                    Td(),
                    Td("乎", "ヲ", "Ja-O.oga", "o", "ヲ-bw.png"),
                ],
            ),
        ]
        f.write(katakana_template.render(rows=rows))
        create_katakana_deck(rows)


def create_katakana_deck(rows: list[Row]) -> None:
    model = genanki.Model(
        1630224618,
        "Katakana",
        fields=[
            {"name": "Chinese"},
            {"name": "Chinese_svg"},
            {"name": "Katakana"},
            {"name": "audio"},
            {"name": "romanization"},
            {"name": "stroke_order"},
        ],
        templates=[
            {
                "name": "Katakana",
                "qfmt": '<span lang="ja">{{Katakana}}</span>',
                "afmt": '{{FrontSide}}<p>{{Chinese_svg}} <span lang="zh">{{Chinese}}</span></p><p>{{romanization}}</p><p>{{audio}}</p><p>{{stroke_order}}</p>',
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

.zh-svg {
  width: 3rem;
}
""",
    )
    deck = genanki.Deck(1492529969, "Katakana")
    package = genanki.Package(deck)
    for row in rows:
        for td in row.td_list:
            if td.chinese == "":
                continue
            note = genanki.Note(
                model=model,
                fields=[
                    td.chinese,
                    f'<img class="zh-svg" src="{td.chinese}_KleeOne-Regular.svg">',
                    td.kana,
                    f"[sound:{td.audio}]" if td.audio != "" else "",
                    td.romanization,
                    f'<img src="{td.stroke_order}">' if td.stroke_order != "" else "",
                ],
            )
            deck.add_note(note)
            package.media_files.append(f"images/{td.chinese}_KleeOne-Regular.svg")
            if td.audio != "":
                package.media_files.append(f"sounds/{td.audio}")
            if td.stroke_order != "":
                package.media_files.append(f"images/{td.stroke_order}")

    package.media_files.extend(
        ["fonts/_HengShanMaoBiCaoShu-2.ttf", "fonts/_KleeOne-Regular.ttf"]
    )
    package.write_to_file("_site/katakana.apkg")


if __name__ == "__main__":
    env = Environment(
        loader=PackageLoader("kana"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    Path("_site").mkdir(exist_ok=True)
    create_hiragana_files(env)
    create_katakana_files(env)
