from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def generate_report_id():

    timestamp = datetime.now().strftime(
        "%Y%m%d%H%M%S"
    )

    return f"REPORT_{timestamp}"


def create_pdf_report(
    patient_name,
    medicines,
    interaction_result,
    ai_summary=None
):

    report_id = generate_report_id()

    pdf_path = REPORT_DIR / f"{report_id}.pdf"

    document = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Smart Medicine Safety Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"<b>Report ID:</b> {report_id}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Patient:</b> {patient_name}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now()}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Medicine List",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    for medicine in medicines:

        content.append(
            Paragraph(
                f"• {medicine}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Interaction Analysis",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    interactions = interaction_result.get(
        "interactions",
        []
    )

    if not interactions:

        content.append(
            Paragraph(
                "No interaction information detected.",
                styles["BodyText"]
            )
        )

    else:

        content.append(
            Paragraph(
                f"Total Interactions Found: {len(interactions)}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        for index, item in enumerate(
            interactions,
            start=1
        ):

            description = item.get(
                "description",
                ""
            )

            severity = item.get(
                "severity",
                "Unknown"
            )

            content.append(
                Paragraph(
                    f"<b>{index}.</b> Severity: {severity}",
                    styles["BodyText"]
                )
            )

            content.append(
                Paragraph(
                    description,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 8)
            )

    if ai_summary:

        content.append(
            PageBreak()
        )

        content.append(
            Paragraph(
                "AI Clinical Summary",
                styles["Heading1"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                ai_summary,
                styles["BodyText"]
            )
        )

    document.build(
        content
    )

    return {
        "success": True,
        "report_id": report_id,
        "file_path": str(pdf_path)
    }


def create_patient_report(
    patient_name,
    medicines,
    interaction_result
):

    return create_pdf_report(
        patient_name=patient_name,
        medicines=medicines,
        interaction_result=interaction_result
    )


def create_ai_report(
    patient_name,
    medicines,
    interaction_result,
    ai_summary
):

    return create_pdf_report(
        patient_name=patient_name,
        medicines=medicines,
        interaction_result=interaction_result,
        ai_summary=ai_summary
    )


if __name__ == "__main__":

    sample_result = {
        "interactions": [
            {
                "severity": "High",
                "description":
                "Potential bleeding risk when combined."
            }
        ]
    }

    report = create_pdf_report(
        patient_name="Demo User",
        medicines=[
            "Warfarin",
            "Aspirin"
        ],
        interaction_result=sample_result,
        ai_summary="Monitor patient closely."
    )

    print(report)
