from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(report_text, sample_images, thermal_images):

    output = "outputs/DDR_Report_Final.pdf"

    doc = SimpleDocTemplate(output, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Detailed Diagnostic Report", styles["Title"]))
    story.append(Spacer(1, 20))

    lines = report_text.split("\n")

    sample_index = 0
    thermal_index = 0

    for line in lines:

        line = line.replace("**", "").replace("###", "")

        if line.strip():
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 10))

            if any(word in line for word in ["Hall", "Bedroom", "Bathroom", "Parking"]):

                if sample_index < len(sample_images) and thermal_index < len(thermal_images):

                    try:
                        visual = Image(sample_images[sample_index], width=200, height=150)
                        thermal = Image(thermal_images[thermal_index], width=200, height=150)

                        table = Table([[thermal, visual]])

                        story.append(table)
                        story.append(Spacer(1, 15))

                        story.append(
                            Paragraph(
                                "Left: Thermal evidence | Right: Visual inspection",
                                styles["Italic"]
                            )
                        )

                        story.append(Spacer(1, 15))

                        sample_index += 1
                        thermal_index += 1

                    except:
                        pass

    doc.build(story)

    return output