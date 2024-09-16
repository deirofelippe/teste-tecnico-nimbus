import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    KeepTogether,
)

width, height = A4  # 596, 842
margin = 35
margin_left_right = margin + margin
highlight_color = "#ff0000"
not_highlight_color = "#595959"

style_normal = ParagraphStyle(
    name="Normal",
    fontSize=10,
    spaceAfter=8,
    alignment=TA_JUSTIFY,
    fontName="Helvetica",
    textColor=HexColor("#000000"),
)

style_type = ParagraphStyle(
    name="Type",
    fontSize=12,
    spaceAfter=8,
    fontName="Helvetica-Bold",
    backColor=None,
    textColor=HexColor("#000000"),
)

style_phenomenon = ParagraphStyle(
    name="PhenomenonWithBackground",
    fontSize=10,
    spaceAfter=4,
    leading=15,
    leftIndent=0,
    rightIndent=350,
    fontName="Helvetica-Bold",
    backColor=HexColor(not_highlight_color),
    textColor=HexColor("#ffffff"),
)

style_phenomenon_highlight = ParagraphStyle(
    name="PhenomenonWithBackgroundhighlight",
    fontSize=10,
    spaceAfter=4,
    leading=15,
    leftIndent=0,
    rightIndent=350,
    fontName="Helvetica-Bold",
    backColor=HexColor(highlight_color),
    textColor=HexColor("#ffffff"),
)


def header_with_params(customer: str, date: str):
    def build_header(cvs, doc):
        margin = 40

        ### HEADER
        cvs.setFillColor(HexColor("#ffab40"))
        h = 45
        cvs.rect(x=0, y=height - h, width=width, height=h, stroke=0, fill=1)

        cvs.setFillColor(HexColor("#073763"))
        h = 40
        cvs.rect(x=0, y=height - h, width=width, height=h, stroke=0, fill=1)

        cvs.setFontSize(22)
        cvs.setFillColor(HexColor("#ffffff"))
        cvs.drawCentredString(width / 2, 815, "Relatório Meteorológico")

        ### HEADER INFOS
        p1 = Paragraph(
            f"""<font size="12" name='Helvetica'><b>Cliente:</b> {customer}</font>"""
        )
        p1.wrapOn(cvs, 270, 50)
        p1.drawOn(canvas=cvs, x=margin, y=780)

        p1 = Paragraph(
            f"""<font size="12" name='Helvetica'><b>Data de confecção:</b> {date}</font>"""
        )
        p1.wrapOn(cvs, 300, 50)
        p1.drawOn(canvas=cvs, x=320, y=780)

    return build_header


def generate_phenomenon_group(
    list_type_phenomenon,
):
    story = []

    for phenomenon in list_type_phenomenon["phenomena"]:
        style = (
            style_phenomenon_highlight
            if phenomenon["highlight"] == True
            else style_phenomenon
        )

        list_flow = [Paragraph(phenomenon["phenomenon"], style)]
        for info in phenomenon["infos"]:
            list_flow.append(
                Paragraph(f"""<b>{info["date"]}</b>  {info["message"]}""", style_normal)
            )

        story.append(KeepTogether([] + list_flow + [Spacer(width, 6)]))

    return story


def generate_report(header_info: dict, analysis: dict, forecast: dict):
    customer = header_info["customer"]
    customer = customer.title()[0:25]
    date = header_info["date"]

    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.getcwd() + f"/reports/Relatorio_Meteorologico_{now}.pdf"

    document = BaseDocTemplate(filename=filename, pagesize=A4)

    frame = Frame(margin, 100, width - margin_left_right, 9.2 * inch, id="main_frame")
    document.addPageTemplates(
        [
            PageTemplate(
                id="main_template",
                frames=[frame],
                onPage=header_with_params(customer, date),
            )
        ]
    )

    story = []

    story.append(Paragraph("Análise", style_type))
    story_analysis = generate_phenomenon_group(analysis)
    story = story + story_analysis

    story.append(PageBreak())

    story.append(Paragraph("Previsão", style_type))
    story_forecast = generate_phenomenon_group(forecast)
    story = story + story_forecast

    document.build(story)

    return filename
