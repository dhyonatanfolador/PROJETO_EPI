from django.shortcuts import render
from django.http import FileResponse
from django.views.generic import View

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm

import io
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt

from app_emprestimo.models import Emprestimo
from app_colaborador.models import Colaborador
from app_equipamento.models import Equipamento


def relatorio_emprestimos_view(request):
    emprestimos = Emprestimo.objects.select_related(
        "id_colaborador", "id_equipamento"
    ).all()

    colaboradores = Colaborador.objects.all()

    # Filtros do relatório principal
    colaborador_id = request.GET.get("colaborador")
    equipamento_id = request.GET.get("equipamento")
    status = request.GET.get("status")

    if colaborador_id:
        emprestimos = emprestimos.filter(id_colaborador__id=colaborador_id)

    if equipamento_id:
        emprestimos = emprestimos.filter(id_equipamento__id=equipamento_id)

    if status:
        emprestimos = emprestimos.filter(status=status)

    # Filtro da busca no modal (q)
    q_colaborador = request.GET.get("q_colaborador")
    q_equipamento = request.GET.get("q_equipamento")

    if q_colaborador:
        colaboradores = colaboradores.filter(nome__icontains=q_colaborador)

    if q_equipamento is not None:
        equipamentos = Equipamento.objects.filter(nome__icontains=q_equipamento)
    else:
        equipamentos = Equipamento.objects.all()

    context = {
        "emprestimos": emprestimos,
        "colaboradores": colaboradores,
        "equipamentos": equipamentos,
        "status_choices": Emprestimo.STATUS_CHOICES,
    }

    return render(request, "app_relatorio/pages/relatorio.html", context)


# View para gerar e retornar o PDF
@method_decorator(xframe_options_exempt, name="dispatch")
class GerarPdfView(View):
    def get(self, request, *args, **kwargs):
        buffer = io.BytesIO()
        status = request.GET.get("status")
        colaborador_id = request.GET.get("colaborador")
        equipamento_id = request.GET.get("equipamento")

        # Filtro específico: apenas um colaborador
        if colaborador_id:
            try:
                colaborador = Colaborador.objects.get(pk=colaborador_id)
            except Colaborador.DoesNotExist:
                return self._render_error_pdf(
                    buffer, f"Colaborador com ID {colaborador_id} não encontrado."
                )

            emprestimos = Emprestimo.objects.select_related(
                "id_colaborador", "id_equipamento"
            ).filter(id_colaborador=colaborador)

            if status:
                emprestimos = emprestimos.filter(status=status)
            if equipamento_id:
                emprestimos = emprestimos.filter(id_equipamento__id=equipamento_id)

            return self._gerar_pdf_individual(
                buffer, colaborador, emprestimos, status, equipamento_id
            )

        # Nenhum colaborador especificado — listar todos com seus empréstimos
        return self._gerar_pdf_todos(buffer, status, equipamento_id)

    def _gerar_pdf_individual(
        self, buffer, colaborador, emprestimos, status, equipamento_id
    ):
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            leftMargin=15 * mm,
            rightMargin=15 * mm,
            topMargin=15 * mm,
            bottomMargin=15 * mm,
        )

        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "title", parent=styles["Heading1"], alignment=1, fontSize=14
        )
        normal_small = ParagraphStyle(
            "normal_small", parent=styles["Normal"], fontSize=9, leading=11
        )

        elements = []

        elements.append(Paragraph("Relatório de Empréstimos", title_style))
        elements.append(Spacer(1, 6))
        elements.append(Paragraph(f"Colaborador: {colaborador.nome}", normal_small))
        if status:
            elements.append(Paragraph(f"Status: {status}", normal_small))
        if equipamento_id:
            try:
                equipamento = Equipamento.objects.get(pk=equipamento_id)
                elements.append(
                    Paragraph(f"Equipamento: {equipamento.nome}", normal_small)
                )
            except Equipamento.DoesNotExist:
                elements.append(Paragraph("Equipamento não encontrado.", normal_small))
        elements.append(Spacer(1, 6))

        elements.extend(self._build_tabela_emprestimos(emprestimos, normal_small))

        doc.build(elements)
        buffer.seek(0)
        return FileResponse(
            buffer, filename="Relatorio_Emprestimos.pdf", content_type="application/pdf"
        )

    def _gerar_pdf_todos(self, buffer, status, equipamento_id):
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            leftMargin=15 * mm,
            rightMargin=15 * mm,
            topMargin=15 * mm,
            bottomMargin=15 * mm,
        )

        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "title", parent=styles["Heading1"], alignment=1, fontSize=14
        )
        normal_small = ParagraphStyle(
            "normal_small", parent=styles["Normal"], fontSize=9, leading=11
        )

        elements = []
        elements.append(Paragraph("Relatório Geral de Empréstimos", title_style))
        if status:
            elements.append(Paragraph(f"Status: {status}", normal_small))
        if equipamento_id:
            try:
                equipamento = Equipamento.objects.get(pk=equipamento_id)
                elements.append(
                    Paragraph(f"Equipamento: {equipamento.nome}", normal_small)
                )
            except Equipamento.DoesNotExist:
                elements.append(Paragraph("Equipamento não encontrado.", normal_small))
        elements.append(Spacer(1, 10))

        colaboradores = Colaborador.objects.all().order_by("nome")
        for colaborador in colaboradores:
            emprestimos = Emprestimo.objects.select_related(
                "id_colaborador", "id_equipamento"
            ).filter(id_colaborador=colaborador)

            if status:
                emprestimos = emprestimos.filter(status=status)
            if equipamento_id:
                emprestimos = emprestimos.filter(id_equipamento__id=equipamento_id)

            elements.append(
                Paragraph(f"<b>Colaborador:</b> {colaborador.nome}", normal_small)
            )
            elements.append(Spacer(1, 4))
            elements.extend(self._build_tabela_emprestimos(emprestimos, normal_small))
            elements.append(Spacer(1, 12))

        doc.build(elements)
        buffer.seek(0)
        return FileResponse(
            buffer,
            filename="Relatorio_Todos_Emprestimos.pdf",
            content_type="application/pdf",
        )

    def _build_tabela_emprestimos(self, emprestimos, style):
        data = [["ID", "Equipamento", "Data Entrega", "Data Devolução", "Status"]]
        for e in emprestimos:
            equipamento_descr = (
                getattr(e.id_equipamento, "descricao", "")
                or getattr(e.id_equipamento, "nome", "")
                or ""
            )
            data.append(
                [
                    str(e.id),
                    Paragraph(equipamento_descr, style),
                    e.data_entrega.strftime("%d/%m/%Y %H:%M") if e.data_entrega else "",
                    e.devolucao.strftime("%d/%m/%Y %H:%M") if e.devolucao else "",
                    e.get_status_display(),
                ]
            )

        if len(data) == 1:
            return [Paragraph("Nenhum empréstimo encontrado.", style)]

        page_width, _ = A4
        usable_width = page_width - (15 * mm + 15 * mm)
        col_widths = [
            20 * mm,
            70 * mm,
            35 * mm,
            35 * mm,
            usable_width - (20 * mm + 70 * mm + 35 * mm + 35 * mm),
        ]

        table = Table(data, colWidths=col_widths, repeatRows=1)
        table_style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.black),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ]
        )
        table.setStyle(table_style)
        return [table]

    def _render_error_pdf(self, buffer, message):
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            leftMargin=30,
            rightMargin=30,
            topMargin=50,
            bottomMargin=50,
        )

        styles = getSampleStyleSheet()
        elements = [
            Paragraph("Erro ao gerar PDF", styles["Title"]),
            Spacer(1, 20),
            Paragraph(message, styles["Normal"]),
        ]

        doc.build(elements)
        buffer.seek(0)
        return FileResponse(
            buffer, filename="Erro_Relatorio.pdf", content_type="application/pdf"
        )
