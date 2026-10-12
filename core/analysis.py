from typing import Any, Dict, List


def assess_ewaste_inventory(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    items = list(items or [])
    reviewed = []
    for index, raw in enumerate(items):
        item = dict(raw or {})
        missing = [
            key for key in ("device_type", "quantity", "condition", "destination")
            if item.get(key) is None or item.get(key) == ""
        ]
        notes = str(item.get("notes", "")).lower()
        flags = []
        if item.get("battery_present") is True or "battery" in notes:
            flags.append("Confirm safe collection and qualified handling for battery-containing items.")
        if item.get("damaged") is True or "damaged" in notes or "swollen" in notes:
            flags.append("Isolate from routine processing and consult qualified handling guidance.")
        reviewed.append({
            "item_id": item.get("id", f"item-{index + 1}"),
            "device_type": item.get("device_type", "Not supplied"),
            "quantity": item.get("quantity", "Unspecified"),
            "missing_fields": missing,
            "handling_review_flags": flags,
        })
    return {
        "item_count": len(reviewed),
        "items": reviewed,
        "note": "This is an information review, not a physical inspection or hazardous-material assessment.",
    }


def compare_recovery_options(options: List[Dict[str, Any]]) -> Dict[str, Any]:
    options = list(options or [])
    reviewed = []
    for index, raw in enumerate(options):
        option = dict(raw or {})
        missing = [
            key for key in ("name", "route", "cost", "evidence_of_authorization")
            if not option.get(key)
        ]
        reviewed.append({
            "option_id": option.get("id", f"option-{index + 1}"),
            "name": option.get("name", "Not supplied"),
            "route": option.get("route", "Unspecified"),
            "stated_benefits": list(option.get("benefits") or []),
            "stated_constraints": list(option.get("constraints") or []),
            "missing_information": missing,
        })
    return {
        "option_count": len(reviewed),
        "options": reviewed,
        "note": "No facility authorization, cost, or recovery yield has been independently verified.",
    }


def plan_responsible_handling(
    items: List[Dict[str, Any]],
    destination: Dict[str, Any],
    tasks: List[Dict[str, Any]],
) -> Dict[str, Any]:
    destination = dict(destination or {})
    tasks = list(tasks or [])
    gaps = [
        key for key in ("handler_name", "authorization_evidence", "local_requirements_checked")
        if not destination.get(key)
    ]
    checklist = []
    for index, raw in enumerate(tasks):
        task = dict(raw or {})
        task.setdefault("owner", "Unspecified")
        task.setdefault("status", "Needs review")
        checklist.append(task)
    return {
        "items_count": len(items or []),
        "destination": destination.get("handler_name", "Not supplied"),
        "destination_information_gaps": gaps,
        "checklist": checklist,
        "recommended_checks": [
            "Protect personal or business data on devices before transfer, where applicable.",
            "Confirm collection and transport requirements for batteries and damaged devices.",
            "Verify handler authorization and downstream destination before handoff.",
        ],
        "note": "Follow local rules and qualified handling guidance; do not dismantle hazardous components without appropriate training.",
    }
