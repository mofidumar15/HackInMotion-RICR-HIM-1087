

import re
import uuid
import bcrypt
from datetime import datetime, timezone

from storage import (
    load_json,
    save_json,
    USERS_FILE
)



def generate_user_id():
    return str(uuid.uuid4())


def current_timestamp():
    return datetime.now(timezone.utc).isoformat()

#PASSWORD SECURITY 

def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8")
        )
    except Exception:
        return False



def validate_email(email: str) -> bool:

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(
        re.match(pattern, email)
    )


def validate_password(password: str):

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."

    return True, "Valid password."




def get_all_users():

    return load_json(
        USERS_FILE,
        []
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

        if user["email"] == email:
            return user

    return None


def find_user_by_id(user_id):

    users = get_all_users()

    for user in users:

        if user["user_id"] == user_id:
            return user

    return None


# REGISTER USER

def register_user(
    full_name,
    email,
    password
):

    email = email.strip().lower()

    if not full_name.strip():
        return {
            "success": False,
            "message": "Full name is required."
        }

    if not validate_email(email):
        return {
            "success": False,
            "message": "Invalid email address."
        }

    valid_password, message = validate_password(password)

    if not valid_password:
        return {
            "success": False,
            "message": message
        }

    existing_user = find_user_by_email(email)

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered."
        }

    users = get_all_users()

    user = {
        "user_id": generate_user_id(),
        "full_name": full_name,
        "email": email,
        "password_hash": hash_password(password),
        "role": "patient",
        "created_at": current_timestamp(),
        "last_login": None
    }

    users.append(user)

    save_all_users(users)

    return {
        "success": True,
        "message": "Registration successful.",
        "user": user
    }


# ==========================================================
# LOGIN USER
# ==========================================================

def login_user(
    email,
    password
):

    user = find_user_by_email(email)

    if not user:
        return {
            "success": False,
            "message": "Invalid credentials."
        }

    if not verify_password(
        password,
        user["password_hash"]
    ):
        return {
            "success": False,
            "message": "Invalid credentials."
        }

    users = get_all_users()

    for item in users:

        if item["user_id"] == user["user_id"]:

            item["last_login"] = current_timestamp()
            break

    save_all_users(users)

    return {
        "success": True,
        "message": "Login successful.",
        "user": user
    }



# PROFILE


def get_user_profile(user_id):

    user = find_user_by_id(user_id)

    if not user:
        return None

    return {
        "user_id": user["user_id"],
        "full_name": user["full_name"],
        "email": user["email"],
        "role": user["role"],
        "created_at": user["created_at"],
        "last_login": user["last_login"]
    }


# UPDATE PROFILE


def update_profile(
    user_id,
    full_name=None
):

    users = get_all_users()

    updated = False

    for user in users:

        if user["user_id"] == user_id:

            if full_name:
                user["full_name"] = full_name

            updated = True
            break

    if updated:
        save_all_users(users)

    return updated



# CHANGE PASSWORD


def change_password(
    user_id,
    current_password,
    new_password
):

    users = get_all_users()

    for user in users:

        if user["user_id"] == user_id:

            if not verify_password(
                current_password,
                user["password_hash"]
            ):
                return False, "Current password incorrect."

            valid, message = validate_password(
                new_password
            )

            if not valid:
                return False, message

            user["password_hash"] = hash_password(
                new_password
            )

            save_all_users(users)

            return True, "Password updated."

    return False, "User not found."



# DELETE USER


def delete_user(user_id):

    users = get_all_users()

    filtered_users = [
        user
        for user in users
        if user["user_id"] != user_id
    ]

    save_all_users(
        filtered_users
    )

    return True



# ADMIN STATS


def total_users():

    return len(
        get_all_users()
    )



# TEST


if __name__ == "__main__":

    print("=" * 60)
    print("AUTH MODULE TEST")
    print("=" * 60)

    result = register_user(
        "Demo User",
        "demo@test.com",
        "DemoPass123"
    )

    print(result)

    login = login_user(
        "demo@test.com",
        "DemoPass123"
    )

    print(login)

    print("=" * 60)
    print("AUTH MODULE READY")
    print("=" * 60)
