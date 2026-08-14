import os
import google.generativeai as genai


class GeminiEngine:

    def __init__(self):

        self.api_key = os.getenv(
            "GEMINI_API_KEY",
            ""
        )

        self.model = None

        if self.api_key:

            genai.configure(
                api_key=self.api_key
            )

            try:

                self.model = genai.GenerativeModel(
                    "gemini-1.5-flash"
                )

            except Exception:
                self.model = None

    def available(self):

        return self.model is not None

    def generate(
        self,
        prompt,
        temperature=0.3
    ):

        if not self.available():

            return {
                "success": False,
                "response": "AI service unavailable."
            }

        try:

            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": temperature
                }
            )

            return {
                "success": True,
                "response": response.text
            }

        except Exception as error:

            return {
                "success": False,
                "response": str(error)
            }

    def explain_interaction(
        self,
        medicines,
        interaction_text
    ):

        prompt = f"""
You are a clinical medication safety assistant.

Medicines:
{", ".join(medicines)}

Interaction Information:
{interaction_text}

Explain:

1. What this interaction means
2. Possible risks
3. Symptoms to watch for
4. When to contact a doctor

Keep language simple and patient friendly.
"""

        return self.generate(prompt)

    def medicine_information(
        self,
        medicine_name
    ):

        prompt = f"""
Provide patient-friendly information about:

Medicine: {medicine_name}

Include:

- Purpose
- Common uses
- Common side effects
- Important precautions
- Storage instructions

Keep response concise.
"""

        return self.generate(prompt)

    def explain_prescription(
        self,
        prescription_text
    ):

        prompt = f"""
Explain this prescription in simple language.

Prescription:

{prescription_text}

Provide:

1. Medicines found
2. What each medicine is used for
3. Important precautions
4. Patient guidance
"""

        return self.generate(prompt)

    def allergy_warning(
        self,
        allergies,
        medicines
    ):

        prompt = f"""
Patient Allergies:
{allergies}

Medicines:
{medicines}

Check for possible allergy concerns.

Return:

- Risk assessment
- Explanation
- Recommendation
"""

        return self.generate(prompt)

    def patient_counselling(
        self,
        medicines
    ):

        prompt = f"""
Provide medication counselling.

Medicines:
{medicines}

Include:

- Dos and Don'ts
- Lifestyle advice
- Food precautions
- Follow-up recommendations
"""

        return self.generate(prompt)

    def summarize_report(
        self,
        report_text
    ):

        prompt = f"""
Summarize the following medication safety report.

Report:
{report_text}

Create:

- Executive Summary
- Risk Level
- Key Findings
- Recommendations
"""

        return self.generate(prompt)

    def chatbot(
        self,
        question
    ):

        prompt = f"""
You are MediSafe AI.

Answer the user's medicine-related question.

Question:
{question}

Provide accurate and concise guidance.
"""

        return self.generate(prompt)

    def emergency_guidance(
        self,
        symptoms
    ):

        prompt = f"""
Symptoms:
{symptoms}

Determine:

- Possible urgency level
- Immediate safety actions
- When emergency care may be required

Do not diagnose diseases.
"""

        return self.generate(prompt)


gemini_engine = GeminiEngine()


if __name__ == "__main__":

    result = gemini_engine.chatbot(
        "Can I take aspirin with warfarin?"
    )

    print(result)
