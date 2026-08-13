import uuid
from datetime import datetime, timezone

import bcrypt

from .storage import (
    create_user,
    find_user_by_email,
    find_user_by_id,
)


SESSIONS = {}


def hash_password(password):
    if not password:
        raise ValueError("Password cannot be empty.")

    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")


def verify_password(password, password_hash):
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8"),
        )
    except Exception:
        return False


def validate_email(email):
    email = email.strip().lower()

    return (
        "@" in email
        and "." in email.split("@")[-1]
        and len(email) >= 5
    )


def validate_password(password):
    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    if not any(char.isupper() for char in password):
        return False, "Password must contain an uppercase letter."

    if not any(char.islower() for char in password):
        return False, "Password must contain a lowercase letter."

    if not any(char.isdigit() for char in password):
        return False, "Password must contain a number."

    return True, "Password accepted."


def register_user(full_name, email, password):
    full_name = full_name.strip()
    email = email.strip().lower()

    if not full_name:
        return {
            "success": False,
            "message": "Full name is required.",
        }

    if not validate_email(email):
        return {
            "success": False,
            "message": "Please enter a valid email address.",
        }

    valid, message = validate_password(password)

    if not valid:
        return {
            "success": False,
            "message": message,
        }

    if find_user_by_email(email):
        return {
            "success": False,
            "message": "An account with this email already exists.",
        }

    user_id = str(uuid.uuid4())

    user = {
        "id": user_id,
        "full_name": full_name,
        "email": email,
        "password_hash": hash_password(password),
        "role": "patient",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    create_user(user)

    return {
        "success": True,
        "message": "Account created successfully.",
        "user_id": user_id,
    }


def login_user(email, password):
    email = email.strip().lower()

    user = find_user_by_email(email)

    if not user:
        return {
            "success": False,
            "message": "Invalid email or password.",
        }

    if not verify_password(
        password,
        user.get("password_hash", ""),
    ):
        return {
            "success": False,
            "message": "Invalid email or password.",
        }

    token = str(uuid.uuid4())

    SESSIONS[token] = {
        "user_id": user["id"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    return {
        "success": True,
        "message": "Login successful.",
        "session_token": token,
        "user_id": user["id"],
        "name": user["full_name"],
        "email": user["email"],
        "role": user.get("role", "patient"),
    }


def validate_session(session_token):
    session = SESSIONS.get(session_token)

    if not session:
        return None

    user = find_user_by_id(session["user_id"])

    if not user:
        return None

    return {
        "user_id": user["id"],
        "full_name": user["full_name"],
        "email": user["email"],
        "role": user.get("role", "patient"),
    }


def logout_user(session_token):
    return SESSIONS.pop(session_token, None) is not None
