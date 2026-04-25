import os
from groq import Groq
from dotenv import load_dotenv
from utils import split_chunks

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_ddr(sample_text, thermal_text):

    sample_text = sample_text[:4000]
    thermal_text = thermal_text[:3000]

    prompt = f"""
You are a professional building diagnostic engineer.

Generate a Detailed Diagnostic Report.

STRICT RULES:
- Must combine inspection findings + thermal evidence
- Mention temperature anomalies where relevant
- Avoid duplicate observations
- Mention conflicts if found
- Missing info = Not Available
- Simple client-friendly language

Required sections:

1 Property Issue Summary
2 Area-wise Observations
3 Probable Root Cause
4 Severity Assessment with reasoning
5 Recommended Actions
6 Additional Notes
7 Missing or Unclear Information

Inspection Report:
{sample_text}

Thermal Report:
{thermal_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content