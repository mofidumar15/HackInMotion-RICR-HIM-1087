import streamlit as st
from pathlib import Path

from backend.auth import (
    register_user,
    login_user
)

from backend.rxnorm_engine import (
    search_medicine,
    check_interactions,
    generate_safety_summary
)

from backend.gemini_engine import (
    gemini_engine
)

from backend.ocr_engine import (
    detect_prescription
)

from backend.report_generator import (
    create_pdf_report
)

st.set_page_config(
    page_title="Smart Medicine Safety Assistant",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(
    exist_ok=True
)

UPLOADS_DIR = Path("uploads")
UPLOADS_DIR.mkdir(
    exist_ok=True
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

st.markdown(
    """
    <style>

    .main-title{
        font-size:42px;
        font-weight:700;
        color:#1565C0;
    }

    .subtitle{
        font-size:18px;
        color:#666666;
    }

    .card{
        padding:20px;
        border-radius:12px;
        border:1px solid #E0E0E0;
        background-color:#FAFAFA;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='main-title'>
    Smart Medicine Safety Assistant
    </div>

    <div class='subtitle'>
    AI-Powered Medication Analysis Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

if not st.session_state.authenticated:

    auth_tab_1, auth_tab_2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    with auth_tab_1:

        st.subheader(
            "User Login"
        )

        login_email = st.text_input(
            "Email",
            key="login_email"
        )

        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        login_button = st.button(
            "Login",
            use_container_width=True
        )

        if login_button:

            result = login_user(
                login_email,
                login_password
            )

            if result["success"]:

                st.session_state.authenticated = True
                st.session_state.user = result["user"]

                st.success(
                    "Login successful"
                )

                st.rerun()

            else:

                st.error(
                    result["message"]
                )

    with auth_tab_2:

        st.subheader(
            "Create Account"
        )

        full_name = st.text_input(
            "Full Name"
        )

        register_email = st.text_input(
            "Email Address"
        )

        register_password = st.text_input(
            "Password",
            type="password"
        )

        register_button = st.button(
            "Create Account",
            use_container_width=True
        )

        if register_button:

            result = register_user(
                full_name,
                register_email,
                register_password
            )

            if result["success"]:

                st.success(
                    "Registration successful. Please login."
                )

            else:

                st.error(
                    result["message"]
                )

    st.stop()

with st.sidebar:

    st.title(
        "Navigation"
    )

    st.write(
        f"Welcome, {st.session_state.user['full_name']}"
    )

    selected_page = st.radio(
        "Select Module",
        [
            "Dashboard",
            "Medicine Search",
            "Drug Interaction Checker",
            "Prescription OCR",
            "AI Assistant",
            "Reports"
        ]
    )

    st.session_state.page = selected_page

    st.divider()

    if st.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.authenticated = False
        st.session_state.user = None

        st.rerun()

page = st.session_state.page

if page == "Dashboard":

    st.header(
        "Dashboard"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Medicine Search",
            "Available"
        )

    with col2:
        st.metric(
            "Interaction Analysis",
            "Available"
        )

    with col3:
        st.metric(
            "OCR Prescription Scan",
            "Available"
        )

    st.info(
        "Select a module from the sidebar to begin."
          )
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if not st.session_state.authenticated:

    st.markdown(
        """
        <div class="hero-card">
            <h1>Smart Medicine Safety Assistant</h1>
            <p>AI-powered medication safety, interaction screening, OCR recognition, allergy monitoring, reminders, and patient guidance.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    auth_tab_1, auth_tab_2 = st.tabs(
        ["Login", "Register"]
    )

    with auth_tab_1:

        st.subheader("User Login")

        login_email = st.text_input(
            "Email",
            key="login_email"
        )

        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            result = authenticate_user(
                login_email,
                login_password
            )

            if result["success"]:

                st.session_state.authenticated = True

                st.session_state.user = result["user"]

                st.success(
                    "Login successful"
                )

                st.rerun()

            else:

                st.error(
                    result["message"]
                )

    with auth_tab_2:

        st.subheader("Create Account")

        register_name = st.text_input(
            "Full Name"
        )

        register_email = st.text_input(
            "Email Address"
        )

        register_password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            result = register_user(
                register_name,
                register_email,
                register_password
            )

            if result["success"]:

                st.success(
                    "Account created successfully"
                )

            else:

                st.error(
                    result["message"]
                )

    st.stop()

user = st.session_state.user

with st.sidebar:

    st.title("MediSafe AI")

    st.caption(
        f"Welcome {user['full_name']}"
    )

    st.divider()

    selected_page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Medicine Search",
            "Drug Interaction Check",
            "OCR Medicine Scanner",
            "Allergy Checker",
            "Medication Reminders",
            "AI Assistant",
            "Reports",
            "Profile"
        ]
    )

    st.session_state.page = selected_page

    st.divider()

    if st.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.authenticated = False

        st.session_state.user = None

        st.rerun()

page = st.session_state.page

st.markdown(
    f"""
    <div class="glass-card">
        <h2>{page}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

if page == "Dashboard":

    medications = get_user_medications(
        user["id"]
    )

    allergies = get_user_allergies(
        user["id"]
    )

    reminders = get_user_reminders(
        user["id"]
    )

    reports = get_user_reports(
        user["id"]
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Medicines",
            len(medications)
        )

    with c2:
        st.metric(
            "Allergies",
            len(allergies)
        )

    with c3:
        st.metric(
            "Reminders",
            len(reminders)
        )

    with c4:
        st.metric(
            "Reports",
            len(reports)
        )

    st.markdown("---")

    st.subheader(
        "Recent Medications"
    )

    if medications:

        st.dataframe(
            medications,
            use_container_width=True
        )

    else:

        st.info(
            "No medicines added yet."
  )

