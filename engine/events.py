from typing import Dict
from events.event import Event
from events.negative_event import NegativeEvent
from events.positive_event import PositiveEvent


WAR_EVENT_TABLE: Dict[range, Event] = {
    range(-25, -20): NegativeEvent("Ally leaves the alliance"),
    range(-20, -15): NegativeEvent("Civil unrest emerges"),
    range(-15, -10): NegativeEvent("Internal leadership conflict"),
    range(-10, -5): NegativeEvent("Supply disruption"),
    range(-5, 0): NegativeEvent("Strategic disagreement"),
    range(0, 5): NegativeEvent("Propaganda mishap"),
    range(5, 10): NegativeEvent("Public dissent grows"),
    range(10, 15): NegativeEvent("Religious tensions rise"),
    range(15, 20): NegativeEvent("Foreign sanctions imposed"),
    range(20, 25): NegativeEvent("Enemy infiltration succeeds"),
    range(25, 35): NegativeEvent("Battle starts"),
    range(35, 60): NegativeEvent("Battle progresses"),
    range(60, 75): NegativeEvent("Battle ends"),
    range(75, 80): PositiveEvent("Foreign aid arrives"),
    range(80, 85): PositiveEvent("Cultural unity strengthens"),
    range(85, 90): PositiveEvent("Enemy official defects"),
    range(90, 95): PositiveEvent("New region joins the cause"),
    range(95, 100): PositiveEvent("Intelligence breakthrough"),
    range(100, 105): PositiveEvent("Public morale surges"),
    range(105, 110): PositiveEvent("Strategic region secured"),
    range(110, 115): PositiveEvent("New leader rises"),
    range(115, 120): PositiveEvent("Diplomatic breakthrough"),
    range(120, 126): PositiveEvent("Crisis Averted"),
}
