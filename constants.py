#!/usr/bin/env python3
"""
Constants module for sports data fetching system.
Centralizes commonly used mappings and constants to eliminate code duplication.
"""

MATCH_STATUS_DESCRIPTIONS = {
    0: "Abnormal (suggest hiding)",
    1: "Not started", 
    2: "First half",
    3: "Half-time",
    4: "Second half",
    5: "Overtime",
    6: "Overtime (deprecated)",
    7: "Penalty Shoot-out",
    8: "End",
    9: "Delay",
    10: "Interrupt",
    11: "Cut in half",
    12: "Cancel",
    13: "To be determined"
}

IN_PLAY_STATUS_IDS = {2, 3, 4, 5, 6, 7}

MATCH_STATUS_SHORT = {
    0: "Abnormal",
    1: "Not started", 
    2: "First half",
    3: "Half-time",
    4: "Second half",
    5: "Overtime",
    6: "Overtime (deprecated)",
    7: "Penalty Shoot-out",
    8: "End",
    9: "Delay",
    10: "Interrupt",
    11: "Cut in half",
    12: "Cancel",
    13: "To be determined"
}
