import json
import uuid
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path.cwd()

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"
UPLOAD_DIR = BASE_DIR / "uploads"

DATA_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
UPLOAD_DIR.mkdir(exist_ok=True)

USERS_FILE = DATA_DIR / "users.json"

MEDICATIONS_FILE = DATA_DIR / "medications.json"

INTERACTIONS_FILE = DATA_DIR / "interaction_history.json"

ALLERGIES_FILE = DATA_DIR / "allergies.json"

REPORTS_FILE = DATA_DIR / "reports.json"

REMINDERS_FILE = DATA_DIR / "reminders.json"

def generate_id():
    return str(uuid.uuid4())


def utc_now():
    return datetime.now(timezone.utc).isoformat()

def save_json(file_path, data):
    """
    Save JSON data safely.
    """

    temp_file = Path(str(file_path) + ".tmp")

    with open(
        temp_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    temp_file.replace(file_path)


def load_json(file_path, default=None):
    """
    Load JSON data safely.
    """

    if default is None:
        default = []

    try:

        if not file_path.exists():

            save_json(
                file_path,
                default
            )

            return default

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return default
      FILES = [
    USERS_FILE,
    MEDICATIONS_FILE,
    INTERACTIONS_FILE,
    ALLERGIES_FILE,
    REPORTS_FILE,
    REMINDERS_FILE
]

for file in FILES:

    if not file.exists():

        save_json(
            file,
            []
        )

def get_all_users():

    return load_json(
        USERS_FILE
    )


def save_all_users(users):

    save_json(
        USERS_FILE,
        users
    )


def find_user_by_email(email):

    email = email.strip().lower()

    users = get_all_users()

    for user in users:

        if user.get("email") == email:

            return user

    return None


def find_user_by_id(user_id):

    users = get_all_users()

    for user in users:

        if user.get("id") == user_id:

            return user

    return None


def create_user(user_data):

    users = get_all_users()

    user_data["id"] = generate_id()

    user_data["created_at"] = utc_now()

    users.append(user_data)

    save_all_users(users)

    return user_data


def update_user(user_id, updates):

    users = get_all_users()

    updated = False

    for user in users:

        if user["id"] == user_id:

            user.update(updates)

            user["updated_at"] = utc_now()

            updated = True

            break

    if updated:

        save_all_users(users)

    return updated


# GENERIC RECORD OPERATIONS

def add_record(
    file_path,
    user_id,
    record
):

    data = load_json(file_path)

    new_record = dict(record)

    new_record["id"] = generate_id()

    new_record["user_id"] = user_id

    new_record["created_at"] = utc_now()MED

    data.append(new_record)

    save_json(
        file_path,
        data
    )

    return new_record


def get_user_records(
    file_path,
    user_id
):

    records = load_json(file_path)

    return [
        record
        for record in records
        if record.get("user_id") == user_id
    ]



#MEDICATION

def save_medication(
    user_id,
    medication_data
):

    return add_record(
        MEDICATIONS_FILE,
        user_id,
        medication_data
    )


def get_user_medications(
    user_id
):

    return get_user_records(
        MEDICATIONS_FILE,
        user_id
)


# ALLERGIES


def save_allergy(
    user_id,
    allergy_data
):

    return add_record(
        ALLERGIES_FILE,
        user_id,
        allergy_data
    )


def get_user_allergies(
    user_id
):

    return get_user_records(
        ALLERGIES_FILE,
        user_id
    )

# INTERACTION HISTORY
def save_interaction(
    user_id,
    interaction_data
):

    return add_record(
        INTERACTIONS_FILE,
        user_id,
        interaction_data
    )


def get_interaction_history(
    user_id
):

    records = get_user_records(
        INTERACTIONS_FILE,
        user_id
    )

    return sorted(
        records,
        key=lambda x: x.get(
            "created_at",
            ""
        ),
        reverse=True
    )


#PDF REPORTS

def save_report(
    user_id,
    report_data
):

    return add_record(
        REPORTS_FILE,
        user_id,
        report_data
    )


def get_user_reports(
    user_id
):

    return get_user_records(
        REPORTS_FILE,
        user_id
    )

#REMINDERS

def save_reminder(
    user_id,
    reminder_data
):

    return add_record(
        REMINDERS_FILE,
        user_id,
        reminder_data
    )


def get_user_reminders(
    user_id
):

    return get_user_records(
        REMINDERS_FILE,
        user_id
    )

# DASHBOARD STATISTICS

def get_system_statistics():

    return {
        "users": len(load_json(USERS_FILE)),
        "medications": len(load_json(MEDICATIONS_FILE)),
        "interactions": len(load_json(INTERACTIONS_FILE)),
        "allergies": len(load_json(ALLERGIES_FILE)),
        "reports": len(load_json(REPORTS_FILE)),
        "reminders": len(load_json(REMINDERS_FILE))
    }

#TESTS

if __name__ == "__main__":

    print("=" * 60)
    print("LOCAL STORAGE MODULE")
    print("=" * 60)

    stats = get_system_statistics()

    for key, value in stats.items():

        print(f"{key}: {value}")

    print("\nStorage module loaded successfully.")
