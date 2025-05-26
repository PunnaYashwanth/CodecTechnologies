import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_entities(text):
    doc = nlp(text)
    name = None
    skills = []
    education = []

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not name:
            name = ent.text
        if ent.label_ in ["ORG", "EDUCATION"]:
            education.append(ent.text)

    print("Extracted Name:", name)
    print("Education Info:", list(set(education)))

# Example usage
file_path = "sample_resume.pdf"  # <-- Put your PDF file name here
resume_text = extract_text_from_pdf(file_path)
extract_entities(resume_text)
