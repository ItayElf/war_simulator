from typing import Dict
from events.battle_end_event import BattleEndEvent
from events.battle_progress_event import BattleProgressEvent
from events.battle_start_event import BattleStartEvent
from events.event import Event
from events.negative_event import NegativeEvent
from events.positive_event import PositiveEvent


WAR_EVENT_TABLE: Dict[range, Event] = {
    range(-25, -20): NegativeEvent("Ally leaves the alliance"),
    range(-20, -15): NegativeEvent("Civil unrest emerges"),
    range(-15, -10): NegativeEvent("Internal leadership conflict"),
    range(-10, -5): NegativeEvent("Supply disruption"),
    range(-5, 0): NegativeEvent("Strategic disagreement"),
    range(0, 5): BattleStartEvent(),
    range(5, 10): NegativeEvent("Public dissent grows"),
    range(10, 15): NegativeEvent("Religious tensions rise"),
    range(15, 20): NegativeEvent("Foreign sanctions imposed"),
    range(20, 25): NegativeEvent("Enemy infiltration succeeds"),
    range(25, 35): BattleStartEvent(),
    range(35, 70): BattleProgressEvent(),
    range(70, 75): BattleEndEvent(),
    range(75, 80): PositiveEvent("Foreign aid arrives"),
    range(80, 85): PositiveEvent("Cultural unity strengthens"),
    range(85, 90): PositiveEvent("Enemy official defects"),
    range(90, 95): PositiveEvent("New region joins the cause"),
    range(95, 100): PositiveEvent("Intelligence breakthrough"),
    range(100, 105): PositiveEvent("Public morale surges"),
    range(105, 110): BattleStartEvent(),
    range(110, 115): PositiveEvent("New leader rises"),
    range(115, 120): PositiveEvent("Diplomatic breakthrough"),
    range(120, 126): PositiveEvent("Crisis Averted"),
}

PEACE_OUTCOME_TABLE: Dict[range, str] = {
    range(1, 31): "stalemate: no side gains; both sides withdraw.",
    range(31, 61): "minor concessions: small territorial or trade shifts.",
    range(61, 91): "uneasy truce: tensions remain; limited restructuring.",
    range(91, 121): "favorable trade terms: winner gains economic control.",
    range(121, 141): "regional advantage: winner gets control over contested zone.",
    range(141, 161): "political shift: loser's alliances or leadership weaken.",
    range(161, 176): "strategic victory: winner secures major war goals.",
    range(176, 191): "dominant peace: victorious side imposes near-total terms.",
    range(191, 201): "decisive victory: winner gets complete political, military, and symbolic triumph.",
}
