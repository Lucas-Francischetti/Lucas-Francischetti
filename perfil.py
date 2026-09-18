"""
Perfil terminal de Lucas Francischetti Alvarenga.
Execute:  python perfil.py
Deps:     pip install rich
"""

from __future__ import annotations

import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    from rich.columns import Columns
    from rich.console import Console, Group
    from rich.padding import Padding
    from rich.panel import Panel
    from rich.rule import Rule
    from rich.table import Table
    from rich.text import Text
    from rich.theme import Theme
except ImportError:
    print("Este perfil usa a biblioteca 'rich'. Instale com:\n  pip install rich")
    sys.exit(1)

ACCENT = "#2E9EF7"
MUTED = "#8BA3B8"
SOFT = "#1E3A5F"
CHIP_BG = "#0F2744"

THEME = Theme(
    {
        "accent": ACCENT,
        "muted": MUTED,
        "title": "bold #F4F7FB",
        "label": "bold #7DD3FC",
        "kicker": "bold #5B7C99",
        "body": "#D5DEE8",
        "warn": "#FBBF24",
    }
)

console = Console(theme=THEME, highlight=False, legacy_windows=False)

NOME = "Lucas Francischetti Alvarenga"
KICKER = "Engenharia de computação  ·  DevOps  ·  Automação"
HEADLINE = "Do problema à solução, sem rodeios."
LEDE = (
    "Apps e fluxos no ecossistema Microsoft. "
    "Sexto período no CEFET-MG, em Belo Horizonte."
)

NARRATIVA = (
    "Estudo Engenharia de Computação no CEFET-MG e estagio na Sete Soluções "
    "e Tecnologia Ambiental, no setor de DevOps e Dados. O trabalho do dia a "
    "dia é transformar pedido em processo: conversar com quem solicita, "
    "entender o que realmente precisa ser feito, e colocar no ar aplicativos "
    "e automações que as pessoas usam — sem complicar o que pode ser simples."
)

COMO_TRABALHO = (
    "O que mais valorizo é o trecho entre o problema e a entrega: analisar "
    "o sistema antes de implementar, priorizar o que é útil de verdade, "
    "e traduzir o pedido na necessidade que está por trás dele."
)

AGORA = [
    ("Estudando", "Engenharia de Computação @ CEFET-MG"),
    ("Estagiando", "DevOps e Dados @ Sete Soluções"),
    ("Construindo", "Apps e fluxos no ecossistema Microsoft"),
    ("Aprendendo", "Requisitos, dados e entrega útil"),
]

HABILIDADES = {
    "Web": ["HTML5", "CSS3", "JavaScript", "TypeScript", "React", "Tailwind", "Vite", "PHP"],
    "Microsoft": ["Power Automate", "Power Apps"],
    "Fluxo": ["Git", "GitHub", "VS Code"],
}

PROJETOS = [
    {
        "sigla": "RF",
        "nome": "rforma-site",
        "tags": "Pessoal  ·  Em construção",
        "texto": (
            "Site pessoal ainda não publicado na web. "
            "O código já está no GitHub, em React, TypeScript e Tailwind."
        ),
        "url": "https://github.com/Lucas-Francischetti/rforma-site",
    },
    {
        "sigla": "FL",
        "nome": "Flumen Consultoria",
        "tags": "Institucional  ·  Parceria",
        "texto": (
            "Site da Flumen, com páginas de serviços, atuação, notícias e "
            "contato. Formulário em PHP, feito com Gabriel Galvão."
        ),
        "url": "https://github.com/gabrielgdrbandeira/FlumenConsultoria",
    },
]

LINKS = [
    ("LinkedIn", "https://www.linkedin.com/in/lucas-francischetti-865b90378/"),
    ("GitHub", "https://github.com/Lucas-Francischetti"),
]


def _blank() -> Text:
    return Text("")


def _kicker(texto: str) -> Padding:
    return Padding(Text(texto.upper(), style="kicker"), (1, 0, 0, 0))


def _chip(nome: str) -> Text:
    return Text.from_markup(f"[on {CHIP_BG}][accent] {nome} [/][/]")


def cabecalho() -> Group:
    return Group(
        Text(KICKER.upper(), style="kicker"),
        _blank(),
        Text(NOME, style="title"),
        Text(HEADLINE, style="bold white"),
        Text(LEDE, style="muted"),
        _blank(),
        Text(NARRATIVA, style="body"),
        _blank(),
        Text(COMO_TRABALHO, style="body"),
    )


def agora() -> Group:
    tabela = Table.grid(expand=True, padding=(0, 3, 1, 0))
    tabela.add_column(ratio=1)
    tabela.add_column(ratio=1)

    celulas = []
    for rotulo, valor in AGORA:
        bloco = Text()
        bloco.append(rotulo.upper() + "\n", style="kicker")
        bloco.append(valor, style="title")
        celulas.append(bloco)

    tabela.add_row(celulas[0], celulas[1])
    tabela.add_row(celulas[2], celulas[3])
    return Group(_kicker("Agora"), Rule(style=SOFT), tabela)


def ferramentas() -> Group:
    linhas = []
    for grupo, itens in HABILIDADES.items():
        linha = Text()
        linha.append(f"{grupo:<11}", style="kicker")
        for i, item in enumerate(itens):
            if i:
                linha.append("  ")
            linha.append_text(_chip(item))
        linhas.append(linha)

    caixa = Panel(
        Group(*linhas),
        border_style=SOFT,
        padding=(1, 1),
    )
    return Group(
        _kicker("Ferramentas"),
        Rule(style=SOFT),
        Text("O que uso quando preciso sair do papel e entregar.", style="muted"),
        _blank(),
        caixa,
    )


def card_projeto(projeto: dict) -> Panel:
    sigla = Text(f" {projeto['sigla']} ", style=f"bold {ACCENT} on {CHIP_BG}")
    corpo = Table.grid(expand=True, padding=(0, 0, 0, 0))
    corpo.add_column()
    corpo.add_row(sigla)
    corpo.add_row(_blank())
    corpo.add_row(Text(projeto["nome"], style="title"))
    corpo.add_row(Text(projeto["tags"].upper(), style="kicker"))
    corpo.add_row(_blank())
    corpo.add_row(Text(projeto["texto"], style="body"))
    corpo.add_row(_blank())
    corpo.add_row(Text(projeto["url"], style="muted"))
    return Panel(corpo, border_style=SOFT, padding=(1, 1), expand=True)


def construindo() -> Group:
    cards = [card_projeto(p) for p in PROJETOS]
    return Group(
        _kicker("Construindo"),
        Rule(style=SOFT),
        Text("Dois trabalhos em que o código já diz mais do que o currículo.", style="muted"),
        _blank(),
        Columns(cards, equal=True, expand=True),
    )


def rodape() -> Group:
    links = Text()
    for i, (nome, url) in enumerate(LINKS):
        if i:
            links.append("    ·    ", style="muted")
        links.append(nome, style="label")
        links.append("  " + url, style="muted")

    return Group(
        Rule(style=SOFT),
        Text("Obrigado pela visita. Os repositórios estão abertos.", style="muted"),
        links,
    )


def main() -> None:
    console.print()
    console.print(Padding(cabecalho(), (0, 1)))
    console.print()
    console.print(Padding(agora(), (0, 1)))
    console.print()
    console.print(Padding(ferramentas(), (0, 1)))
    console.print()
    console.print(Padding(construindo(), (0, 1)))
    console.print()
    console.print(Padding(rodape(), (0, 1)))
    console.print()


if __name__ == "__main__":
    main()
