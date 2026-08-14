import requests

RXNORM_BASE_URL = "https://rxnav.nlm.nih.gov/REST"


def rxnorm_request(endpoint, params=None):

    response = requests.get(
        f"{RXNORM_BASE_URL}/{endpoint}",
        params=params,
        timeout=20
    )

    response.raise_for_status()

    return response.json()


def search_medicine(name):

    try:

        result = rxnorm_request(
            "rxcui.json",
            {"name": name}
        )

        ids = (
            result
            .get("idGroup", {})
            .get("rxnormId", [])
        )

        if not ids:
            return None

        rxcui = str(ids[0])

        properties = rxnorm_request(
            f"rxcui/{rxcui}/properties.json"
        )

        medicine_name = (
            properties
            .get("properties", {})
            .get("name", name)
        )

        return {
            "success": True,
            "name": medicine_name,
            "rxcui": rxcui
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }


def approximate_search(term):

    try:

        data = rxnorm_request(
            "approximateTerm.json",
            {
                "term": term,
                "maxEntries": 10
            }
        )

        candidates = (
            data
            .get("approximateGroup", {})
            .get("candidate", [])
        )

        medicines = []

        for item in candidates:

            medicines.append({
                "name": item.get("name"),
                "rxcui": item.get("rxcui"),
                "score": item.get("score")
            })

        return medicines

    except Exception:

        return []


def resolve_medicine(name):

    exact = search_medicine(name)

    if exact and exact["success"]:
        exact["corrected"] = False
        return exact

    matches = approximate_search(name)

    if not matches:
        return None

    best = matches[0]

    return {
        "success": True,
        "name": best["name"],
        "rxcui": best["rxcui"],
        "corrected": True
    }


def get_medicine_properties(rxcui):

    try:

        data = rxnorm_request(
            f"rxcui/{rxcui}/properties.json"
        )

        return data.get(
            "properties",
            {}
        )

    except Exception:

        return {}


def get_related_drugs(rxcui):

    try:

        data = rxnorm_request(
            f"rxcui/{rxcui}/related.json"
        )

        return data

    except Exception:

        return {}


def check_drug_interactions(medicine_list):

    try:

        rxcuis = []

        for medicine in medicine_list:

            if isinstance(medicine, dict):

                rxcui = medicine.get("rxcui")

                if rxcui:
                    rxcuis.append(str(rxcui))

        if len(rxcuis) < 2:

            return {
                "success": True,
                "highest_risk": "NONE",
                "interactions_found": 0,
                "interactions": []
            }

        joined = "+".join(rxcuis)

        response = requests.get(
            f"{RXNORM_BASE_URL}/interaction/interaction.json",
            params={
                "rxcui": joined
            },
            timeout=20
        )

        data = response.json()

        interaction_groups = data.get(
            "interactionTypeGroup",
            []
        )

        interactions = []

        for group in interaction_groups:

            for interaction_type in group.get(
                "interactionType",
                []
            ):

                for pair in interaction_type.get(
                    "interactionPair",
                    []
                ):

                    interactions.append({
                        "description": pair.get(
                            "description",
                            ""
                        ),
                        "severity": pair.get(
                            "severity",
                            "Unknown"
                        ),
                        "source": group.get(
                            "sourceName",
                            "RxNorm"
                        )
                    })

        highest_risk = "LOW"

        for item in interactions:

            severity = str(
                item.get(
                    "severity",
                    ""
                )
            ).lower()

            if "contraindicated" in severity:
                highest_risk = "CRITICAL"
                break

            if "major" in severity:
                highest_risk = "HIGH"

            elif "moderate" in severity and highest_risk != "HIGH":
                highest_risk = "MEDIUM"

        return {
            "success": True,
            "highest_risk": highest_risk,
            "interactions_found": len(interactions),
            "interactions": interactions
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error),
            "highest_risk": "UNKNOWN",
            "interactions_found": 0,
            "interactions": []
        }


def analyze_medicines(medicine_names):

    medicines = []

    unresolved = []

    for name in medicine_names:

        result = resolve_medicine(name)

        if result:
            medicines.append(result)
        else:
            unresolved.append(name)

    interaction_result = check_drug_interactions(
        medicines
    )

    return {
        "medicines": medicines,
        "unresolved": unresolved,
        "interaction_result": interaction_result
    }


if __name__ == "__main__":

    test = analyze_medicines(
        [
            "warfarin",
            "aspirin"
        ]
    )

    print(test)
