import re
import cv2
import easyocr
import numpy as np

reader = easyocr.Reader(
    ["en"],
    gpu=False
)


def load_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            "Unable to load image."
        )

    return image


def preprocess_image(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return threshold


def extract_text(image_path):

    image = load_image(
        image_path
    )

    processed = preprocess_image(
        image
    )

    results = reader.readtext(
        processed
    )

    lines = []

    for result in results:

        text = result[1].strip()

        if text:
            lines.append(text)

    return "\n".join(lines)


def extract_lines(image_path):

    text = extract_text(
        image_path
    )

    return [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]


def clean_medicine_name(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s\-]",
        "",
        text
    )

    text = text.strip()

    return text


def extract_possible_medicines(image_path):

    lines = extract_lines(
        image_path
    )

    medicines = []

    for line in lines:

        cleaned = clean_medicine_name(
            line
        )

        if len(cleaned) < 3:
            continue

        if any(
            char.isalpha()
            for char in cleaned
        ):
            medicines.append(
                cleaned
            )

    unique = []

    for medicine in medicines:

        if medicine not in unique:
            unique.append(
                medicine
            )

    return unique


def extract_prescription_data(
    image_path
):

    raw_text = extract_text(
        image_path
    )

    medicines = extract_possible_medicines(
        image_path
    )

    return {
        "success": True,
        "raw_text": raw_text,
        "medicines": medicines,
        "medicine_count": len(
            medicines
        )
    }


def detect_prescription(
    image_path
):

    try:

        result = extract_prescription_data(
            image_path
        )

        return result

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }


def prescription_summary(
    image_path
):

    result = detect_prescription(
        image_path
    )

    if not result["success"]:

        return {
            "success": False,
            "summary": result["error"]
        }

    medicines = result["medicines"]

    return {
        "success": True,
        "summary": (
            f"{len(medicines)} possible medicines detected."
        ),
        "medicines": medicines
    }


if __name__ == "__main__":

    image_path = "sample_prescription.jpg"

    try:

        result = detect_prescription(
            image_path
        )

        print(result)

    except Exception as error:

        print(error)
