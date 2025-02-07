from pathlib import Path
from dataclasses import dataclass

from jinja2 import Environment, PackageLoader, select_autoescape


if __name__ == "__main__":
    env = Environment(
        loader=PackageLoader("kana"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("hiragana.html")

    @dataclass
    class Td:
        chinese: str = ""
        hiragana: str = ""
        audio: str = ""
        colspan: str = ""

    @dataclass
    class Row:
        th: str
        td_list: list[Td]

    Path("_site").mkdir(exist_ok=True)
    with open("_site/hiragana.html", "w", encoding="utf-8") as f:
        f.write(
            template.render(
                rows=[
                    Row(
                        "",
                        [
                            Td("安", "あ", "Ja-A.oga"),
                            Td("以", "い"),
                            Td("宇", "う", "Ja-U.oga"),
                            Td("衣", "え", "Ja-E.oga"),
                            Td("於", "お", "Ja-O.oga"),
                        ],
                    ),
                    Row(
                        "k",
                        [
                            Td("加", "か", "Ja-ka.ogg"),
                            Td("幾", "き"),
                            Td("久", "く"),
                            Td("計", "け"),
                            Td("己", "こ"),
                        ],
                    ),
                    Row(
                        "s",
                        [
                            Td("左", "さ"),
                            Td("之", "し", "Ja-Shi.oga"),
                            Td("寸", "す"),
                            Td("世", "せ"),
                            Td("曽", "そ"),
                        ],
                    ),
                    Row(
                        "t",
                        [
                            Td("太", "た"),
                            Td("知", "ち", "Ja-Chi_2.oga"),
                            Td("川", "つ", "Ja-Tsu.oga"),
                            Td("天", "て"),
                            Td("止", "と"),
                        ],
                    ),
                    Row(
                        "n",
                        [
                            Td("奈", "な"),
                            Td("仁", "に"),
                            Td("奴", "ぬ"),
                            Td("祢", "ね"),
                            Td("乃", "の"),
                        ],
                    ),
                    Row(
                        "h",
                        [
                            Td("波", "は"),
                            Td("比", "ひ", "Ja-Hi.oga"),
                            Td("不", "ふ", "Ja-Fu.oga"),
                            Td("部", "へ"),
                            Td("保", "ほ"),
                        ],
                    ),
                    Row(
                        "m",
                        [
                            Td("末", "ま"),
                            Td("美", "み"),
                            Td("武", "む"),
                            Td("女", "め"),
                            Td("毛", "も"),
                        ],
                    ),
                    Row(
                        "y",
                        [
                            Td("也", "や"),
                            Td(),
                            Td("由", "ゆ"),
                            Td(),
                            Td("与", "よ"),
                        ],
                    ),
                    Row(
                        "r",
                        [
                            Td("良", "ら", "Ja-Ra.oga"),
                            Td("利", "り", "Ja-Ri.oga"),
                            Td("留", "る", "Ja-Ru.oga"),
                            Td("礼", "れ", "Ja-Re.oga"),
                            Td("呂", "ろ", "Ja-Ro.oga"),
                        ],
                    ),
                    Row(
                        "w",
                        [
                            Td("和", "わ"),
                            Td(),
                            Td("无", "ん"),
                            Td(),
                            Td("遠", "を", "Ja-O.oga"),
                        ],
                    ),
                ]
            )
        )
