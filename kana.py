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
        ],
        templates=[
            {
                "name": "Hiragana",
                "qfmt": '<span lang="ja">{{Hiragana}}</span>',
                "afmt": '{{FrontSide}}<p><span lang="ja">{{Chinese}}</span> <span lang="zh">{{Chinese}}</span></p><p>{{romanization}}</p>{{audio}}',
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
                    f"[sound:{td.audio}]" if td.audio != "" else "",
                    td.romanization,
                ],
            )
            deck.add_note(note)
            if td.audio != "":
                audio_path = Path(td.audio)
                if not audio_path.is_file():
                    subprocess.run(
                        [
                            "wget",
                            f"https://commons.wikimedia.org/wiki/Special:FilePath/{td.audio}",
                        ],
                        check=True,
                        capture_output=True,
                        text=True,
                    )
                package.media_files.append(td.audio)
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
                    Td("安", "あ", "Ja-A.oga", "a"),
                    Td("以", "い", romanization="i"),
                    Td("宇", "う", "Ja-U.oga", "u"),
                    Td("衣", "え", "Ja-E.oga", "e"),
                    Td("於", "お", "Ja-O.oga", "o"),
                ],
            ),
            Row(
                "k",
                [
                    Td("加", "か", "Ja-ka.ogg", "ka"),
                    Td("幾", "き", romanization="ki"),
                    Td("久", "く", romanization="ku"),
                    Td("計", "け", romanization="ke"),
                    Td("己", "こ", romanization="ko"),
                ],
            ),
            Row(
                "s",
                [
                    Td("左", "さ", romanization="sa"),
                    Td("之", "し", "Ja-Shi.oga", "shi"),
                    Td("寸", "す", romanization="su"),
                    Td("世", "せ", romanization="se"),
                    Td("曽", "そ", romanization="so"),
                ],
            ),
            Row(
                "t",
                [
                    Td("太", "た", romanization="ta"),
                    Td("知", "ち", "Ja-Chi_2.oga", "chi"),
                    Td("川", "つ", "Ja-Tsu.oga", "tsu"),
                    Td("天", "て", romanization="te"),
                    Td("止", "と", romanization="to"),
                ],
            ),
            Row(
                "n",
                [
                    Td("奈", "な", romanization="na"),
                    Td("仁", "に", "Ja-2-ni.ogg", "ni"),
                    Td("奴", "ぬ", romanization="nu"),
                    Td("祢", "ね", romanization="ne"),
                    Td("乃", "の", romanization="no"),
                ],
            ),
            Row(
                "h",
                [
                    Td("波", "は", romanization="ha"),
                    Td("比", "ひ", "Ja-Hi.oga", "hi"),
                    Td("不", "ふ", "Ja-Fu.oga", "fu"),
                    Td("部", "へ", romanization="he"),
                    Td("保", "ほ", romanization="ho"),
                ],
            ),
            Row(
                "m",
                [
                    Td("末", "ま", romanization="ma"),
                    Td("美", "み", romanization="mi"),
                    Td("武", "む", romanization="mu"),
                    Td("女", "め", romanization="me"),
                    Td("毛", "も", romanization="mo"),
                ],
            ),
            Row(
                "y",
                [
                    Td("也", "や", romanization="ya"),
                    Td(),
                    Td("由", "ゆ", romanization="yu"),
                    Td(),
                    Td("与", "よ", romanization="yo"),
                ],
            ),
            Row(
                "r",
                [
                    Td("良", "ら", "Ja-Ra.oga", "ra"),
                    Td("利", "り", "Ja-Ri.oga", "ri"),
                    Td("留", "る", "Ja-Ru.oga", "ru"),
                    Td("礼", "れ", "Ja-Re.oga", "re"),
                    Td("呂", "ろ", "Ja-Ro.oga", "ro"),
                ],
            ),
            Row(
                "w",
                [
                    Td("和", "わ", romanization="wa"),
                    Td(),
                    Td("无", "ん", romanization="n"),
                    Td(),
                    Td("遠", "を", "Ja-O.oga", "o"),
                ],
            ),
        ]
        f.write(template.render(rows=rows))
        create_anki_deck(rows)
