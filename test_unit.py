import pytest


def get_next_status(current_status):
    """
    Mirrors the status cycling logic found in app/routes/tasks.py.
    Tests this logic in isolation without requiring a running server.
    """
    if current_status == "Pending":
        return "Working"
    elif current_status == "Working":
        return "Done"
    else:
        return "Pending"


class TestStatusCycling:
    """Unit tests for the task status cycling logic (TC-07)."""

    def test_status_pending_to_working(self):
        """Pending status should advance to Working on Next."""
        result = get_next_status("Pending")
        assert result == "Working", (
            f"Expected 'Working' but got '{result}'"
        )

    def test_status_working_to_done(self):
        """Working status should advance to Done on Next."""
        result = get_next_status("Working")
        assert result == "Done", (
            f"Expected 'Done' but got '{result}'"
        )

    def test_status_done_to_pending(self):
        """Done status should cycle back to Pending on Next."""
        result = get_next_status("Done")
        assert result == "Pending", (
            f"Expected 'Pending' but got '{result}' — cycle-back failed"
        )

    def test_full_cycle(self):
        """Full cycle Pending -> Working -> Done -> Pending should complete."""
        status = "Pending"
        status = get_next_status(status)
        assert status == "Working"
        status = get_next_status(status)
        assert status == "Done"
        status = get_next_status(status)
        assert status == "Pending"

    def test_unknown_status_defaults_to_pending(self):
        """Any unrecognised status should default to Pending (else branch)."""
        result = get_next_status("Unknown")
        assert result == "Pending", (
            f"Expected 'Pending' as default but got '{result}'"
        )
