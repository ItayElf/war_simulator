from typing import Dict
from events.event import Event
from events.negative_event import NegativeEvent
from events.positive_event import PositiveEvent


WAR_EVENT_TABLE: Dict[range, Event] = {
    range(-25, -20): PositiveEvent("Ally leaves the alliance"),
    range(-20, -15): PositiveEvent("Civil unrest emerges"),
    range(-15, -10): PositiveEvent("Internal leadership conflict"),
    range(-10, -5): PositiveEvent("Supply disruption"),
    range(-5, 0): PositiveEvent("Strategic disagreement"),
    range(0, 5): PositiveEvent("Propaganda mishap"),
    range(5, 10): PositiveEvent("Public dissent grows"),
    range(10, 15): PositiveEvent("Religious tensions rise"),
    range(15, 20): PositiveEvent("Foreign sanctions imposed"),
    range(20, 25): PositiveEvent("Enemy infiltration succeeds"),
    range(25, 35): PositiveEvent("Battle starts"),
    range(35, 60): PositiveEvent("Battle progresses"),
    range(60, 75): PositiveEvent("Battle ends"),
    range(75, 80): NegativeEvent("Foreign aid arrives"),
    range(80, 85): NegativeEvent("Cultural unity strengthens"),
    range(85, 90): NegativeEvent("Enemy official defects"),
    range(90, 95): NegativeEvent("New region joins the cause"),
    range(95, 100): NegativeEvent("Intelligence breakthrough"),
    range(100, 105): NegativeEvent("Public morale surges"),
    range(105, 110): NegativeEvent("Strategic region secured"),
    range(110, 115): NegativeEvent("New leader rises"),
    range(115, 120): NegativeEvent("Diplomatic breakthrough"),
    range(120, 126): NegativeEvent("Crisis Averted"),
}
