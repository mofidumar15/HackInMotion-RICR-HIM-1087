import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"
UPLOAD_DIR = BASE_DIR / "uploads"

DATA_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


USERS_FILE = DATA_DIR / "users.json"
MEDICATIONS_FILE = DATA_DIR / "medications.json"
HISTORY_FILE = DATA_DIR / "interaction_history.json"
ALLERGIES_FILE = DATA_DIR / "allergies.json"
REMINDERS_FILE = DATA_DIR / "reminders.json"
REPORTS_FILE = DATA_DIR / "pdf_reports.json"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def generate_id():
    return str(uuid.uuid4())


def save_json(file_path, data):
    temporary_file = Path(str(file_path) + ".tmp")

    with open(temporary_file, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

    temporary_file.replace(file_path)


def load_json(file_path, default=None):
    if default is None:
        default = []

    try:
        if not file_path.exists():
            save_json(file_path, default)
            return default

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return default


def initialize_storage():
    files = [
        USERS_FILE,
        MEDICATIONS_FILE,
        HISTORY_FILE,
        ALLERGIES_FILE,
        REMINDERS_FILE,
        REPORTS_FILE,
    ]

    for file_path in files:
        if not file_path.exists():
            save_json(file_path, [])


def find_user_by_email(email):
    email = email.strip().lower()

    for user in load_json(USERS_FILE):
        if user.get("email") == email:
            return user

    return None


def find_user_by_id(user_id):
    for user in load_json(USERS_FILE):
        if user.get("id") == user_id:
            return user

    return None


def create_user(user):
    users = load_json(USERS_FILE)
    users.append(user)
    save_json(USERS_FILE, users)
    return user


def update_user(user_id, updates):
    users = load_json(USERS_FILE)

    for user in users:
        if user.get("id") == user_id:
            user.update(updates)
            save_json(USERS_FILE, users)
            return True

    return False


def add_user_record(file_path, user_id, record):
    records = load_json(file_path)

    new_record = dict(record)
    new_record["id"] = generate_id()
    new_record["user_id"] = user_id
    new_record["created_at"] = utc_now()

    records.append(new_record)

    save_json(file_path, records)

    return new_record


def get_user_records(file_path, user_id):
    return [
        record
        for record in load_json(file_path)
        if record.get("user_id") == user_id
    ]


def save_medication(user_id, medication):
    return add_user_record(
        MEDICATIONS_FILE,
        user_id,
        medication,
    )


def get_user_medications(user_id):
    return get_user_records(
        MEDICATIONS_FILE,
        user_id,
    )


def save_allergy(user_id, allergy):
    return add_user_record(
        ALLERGIES_FILE,
        user_id,
        allergy,
    )


def get_user_allergies(user_id):
    return get_user_records(
        ALLERGIES_FILE,
        user_id,
    )


def save_reminder(user_id, reminder):
    return add_user_record(
        REMINDERS_FILE,
        user_id,
        reminder,
    )


def get_user_reminders(user_id):
    return get_user_records(
        REMINDERS_FILE,
        user_id,
    )


def save_interaction(user_id, interaction):
    return add_user_record(
        HISTORY_FILE,
        user_id,
        interaction,
    )


def get_interaction_history(user_id):
    records = get_user_records(
        HISTORY_FILE,
        user_id,
    )

    return sorted(
        records,
        key=lambda item: item.get("created_at", ""),
        reverse=True,
    )


def save_report(user_id, report):
    return add_user_record(
        REPORTS_FILE,
        user_id,
        report,
    )


def get_user_reports(user_id):
    return get_user_records(
        REPORTS_FILE,
        user_id,
    )


initialize_storage()
