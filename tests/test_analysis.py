from core.analysis import assess_ewaste_inventory, compare_recovery_options, plan_responsible_handling


def test_inventory_missing_fields():
    result = assess_ewaste_inventory([{"device_type": "laptop"}])
    assert "quantity" in result["items"][0]["missing_fields"]


def test_inventory_flags_battery():
    result = assess_ewaste_inventory([{"device_type": "phone", "battery_present": True}])
    assert result["items"][0]["handling_review_flags"]


def test_inventory_empty():
    assert assess_ewaste_inventory([])["item_count"] == 0


def test_options_missing_authorization_evidence():
    result = compare_recovery_options([{"name": "Recycler", "route": "recycling"}])
    assert "evidence_of_authorization" in result["options"][0]["missing_information"]


def test_options_count():
    assert compare_recovery_options([{}, {}])["option_count"] == 2


def test_handling_destination_gaps():
    result = plan_responsible_handling([], {}, [])
    assert "authorization_evidence" in result["destination_information_gaps"]


def test_handling_defaults():
    result = plan_responsible_handling([{"device_type": "laptop"}], {"handler_name": "Handler"}, [{"task": "Confirm pickup"}])
    assert result["checklist"][0]["owner"] == "Unspecified"
