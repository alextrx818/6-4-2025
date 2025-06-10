#!/usr/bin/env python3
"""
Simple test to verify constants module works correctly
"""

from constants import MATCH_STATUS_DESCRIPTIONS, IN_PLAY_STATUS_IDS, MATCH_STATUS_SHORT

def test_constants():
    print("Testing constants module...")
    
    assert len(MATCH_STATUS_DESCRIPTIONS) > 0, "MATCH_STATUS_DESCRIPTIONS should not be empty"
    assert len(IN_PLAY_STATUS_IDS) > 0, "IN_PLAY_STATUS_IDS should not be empty"
    assert len(MATCH_STATUS_SHORT) > 0, "MATCH_STATUS_SHORT should not be empty"
    
    assert MATCH_STATUS_DESCRIPTIONS[2] == "First half", "Status 2 should be 'First half'"
    assert 2 in IN_PLAY_STATUS_IDS, "Status 2 should be in IN_PLAY_STATUS_IDS"
    assert MATCH_STATUS_SHORT[8] == "End", "Status 8 should be 'End'"
    
    print("✓ All constants tests passed!")
    print(f"✓ Status 2: {MATCH_STATUS_DESCRIPTIONS[2]}")
    print(f"✓ In-play IDs: {sorted(IN_PLAY_STATUS_IDS)}")
    print(f"✓ Total status descriptions: {len(MATCH_STATUS_DESCRIPTIONS)}")

if __name__ == "__main__":
    test_constants()
