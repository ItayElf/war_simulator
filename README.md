# War Simulation Engine v0.1.1

> A narrative-first engine for dynamic world events, focused on simulating wars, battles, and their narrative consequences.
> 

---

# Core Mechanics

### 🎯 War Score

A number between –100 and +100, starting at 0. 
Represents the overall momentum of the war.

### 🛡️ Initiative

- One side controls the war's momentum.
- The **side with initiative** rolls for events.
- Initiative flips on **certain** **negative outcomes**.

### ⏳ Time

- Each event advances time.
- Battle progress duration is based on **battle severity** (see table below).

# Simulation Flow

- **Start at War Score 0**, with one faction holding **initiative**.
- The side with initiative rolls **1d100 ± the current War Score** (Side B multiplies the score by -1).
- Compare the result to the [**War Event Table**](#war-event-table) to determine what happens:
- **Apply changes** to war score, battle scores, or time passed.
- If a **negative outcome** occurs, initiative may flip, and a **Peace Offer** might happen based on the number of days that have passed**.**
- **Repeat** the process until one side gets to a score of 100 — the story evolves turn by turn.

##### **War Event Table**

| Range      | Event                        | Next Roll                                       |
| ---------- | ---------------------------- | ----------------------------------------------- |
| –25 to –21 | Ally leaves the alliance     | [Negative Event Table](#negative-event-table)   |
| –20 to –16 | Civil unrest emerges         | [Negative Event Table](#negative-event-table)   |
| –15 to –11 | Internal leadership conflict | [Negative Event Table](#negative-event-table)   |
| –10 to –6  | Supply disruption            | [Negative Event Table](#negative-event-table)   |
| -5 to 5    | Battle progresses            | [Battle Progress Table](#battle-progress-table) |
| 5 to 9     | Strategic disagreement       | [Negative Event Table](#negative-event-table)   |
| 10 to 14   | Battle starts                | [Battle Starts Table](#battle-start-table)      |
| 15 to 19   | Public dissent grows         | [Negative Event Table](#negative-event-table)   |
| 20 to 24   | Religious tensions rise      | [Negative Event Table](#negative-event-table)   |
| 25 to 29   | Foreign sanctions imposed    | [Negative Event Table](#negative-event-table)   |
| 30 to 34   | Enemy infiltration succeeds  | [Negative Event Table](#negative-event-table)   |
| 35 to 44   | Battle starts                | [Battle Starts Table](#battle-start-table)      |
| 45 to 59   | Battle progresses            | [Battle Progress Table](#battle-progress-table) |
| 60 to 64   | Battle ends                  | [Battle End Table](#battle-end-table)           |
| 65 to 69   | Foreign aid arrives          | [Positive Event Table](#positive-event-table)   |
| 70 to 74   | Cultural unity strengthens   | [Positive Event Table](#positive-event-table)   |
| 75 to 79   | Enemy official defects       | [Positive Event Table](#positive-event-table)   |
| 80 to 84   | New region joins the cause   | [Positive Event Table](#positive-event-table)   |
| 85 to 94   | Battle progresses            | [Battle Progress Table](#battle-progress-table) |
| 95 to 99   | Intelligence breakthrough    | [Positive Event Table](#positive-event-table)   |
| 100 to 104 | Public morale surges         | [Positive Event Table](#positive-event-table)   |
| 105 to 109 | Strategic region secured     | [Positive Event Table](#positive-event-table)   |
| 110 to 114 | New leader rises             | [Positive Event Table](#positive-event-table)   |
| 115 to 119 | Diplomatic breakthrough      | [Positive Event Table](#positive-event-table)   |
| 120 to 125 | Crisis Averted               | [Positive Event Table](#positive-event-table)   |

# Non-Battle Events

##### **Positive Event Table**

| Roll (1d10) | Severity Level       | Score Increase | Time Pass   |
| ----------- | -------------------- | -------------- | ----------- |
| 1–3         | Minor gain           | +1             | 1d10 days   |
| 4–6         | Moderate development | +3             | 1d10+2 days |
| 7–8         | Strong advantage     | +5             | 1d10+4 days |
| 9           | Major breakthrough   | +10            | 1d10+6 days |
| 10          | Transformative shift | +15            | 1d10+8 days |

##### **Negative Event Table**

| Roll (1d10) | Severity Level       | Score Decrease | Initiative Flip? | Time Pass   |
| ----------- | -------------------- | -------------- | ---------------- | ----------- |
| 1–3         | Minor setback        | -1             | No               | 1d10 days   |
| 4–6         | Moderate disruption  | –3             | No               | 1d10+2 days |
| 7–8         | Major collapse       | –5             | Yes              | 1d10+4 days |
| 9           | Strategic unraveling | –10            | Yes              | 1d10+6 days |
| 10          | Systemic catastrophe | –15            | Yes              | 1d10+8 days |

# Battles

### Battle Start

- Triggered by a "Battle Starts" event on the main [**War Event Table**](#war-event-table).
- Roll **1d10** on the **Battle Severity Table** to determine the battle’s scale.
- Create a new battle track with a [**Battle Score**](#battle-start-table) starting at 0 (range –10 to 10).
- The battle will progress by rolling on the [**Battle Progress Table**](#battle-progress-table) (when a **Battle Progress** event is triggered) until a battle end occurs.
- **Battle Start** does not increase the days passed.

##### **Battle Start Table**

| Roll | Severity       | Days per Progress | Momentum Impact (Δ to Battle Score) | Score Threshold |
| ---- | -------------- | ----------------- | ----------------------------------- | --------------- |
| 1–3  | Skirmish       | 1–3 days          | ±5                                  | ±3              |
| 4–7  | Engagement     | 4–8 days          | ±10                                 | ±6              |
| 8–9  | Campaign       | 9–14 days         | ±15                                 | ±10             |
| 10   | Decisive Clash | 15–20 days        | ±20                                 | ±15             |

### Battle Progress

- Each "Battle Progress" event triggers a roll on the [**Battle Progress Table**](#battle-progress-table) with **2d10 + current Battle Score**.
- Outcomes modify the battle score (from –3 to +3) and may flip initiative.
- Initiative flips only on negative major outcomes (Collapse or Catastrophic Collapse).
- If the initiative changes, roll on the [**Fallout Table**](#fallout-table) to get a narrative for another thing that might happen.
- The battle to progress is chosen randomly

###### **Battle Progress Table**

| Roll  | Outcome               | Δ Battle Score | Initiative Flip? |
| ----- | --------------------- | -------------- | ---------------- |
| ≤1    | Catastrophic Collapse | –3             | Yes              |
| 2–3   | Collapse              | –2             | Yes              |
| 4–6   | Major Setback         | –1             | 50% chance       |
| 7–10  | Minor Setback         | –1             | 25% chance       |
| 11–13 | Stalemate             | 0              | No               |
| 14–17 | Minor Advance         | +1             | No               |
| 18–20 | Major Advance         | +1             | No               |
| 21–22 | Critical Push         | +2             | No               |
| 23–24 | Crushing Blow         | +3             | No               |
| 25+   | Annihilation (opt.)   | +3             | No               |

###### **Fallout Table**

| Roll | Fallout                 | Thematic Options (Choose or improvise)                                                                   |
| ---- | ----------------------- | -------------------------------------------------------------------------------------------------------- |
| 1    | A hero dies in vain     | A champion falls on the battlefield, or a beloved leader loses hope                                      |
| 2    | The banner falls        | A physical banner is captured or destroyed, or a symbol of hope is shattered (e.g., flag, statue, ideal) |
| 3    | Shame clings like smoke | A scandal erupts within the ranks, or cultural shame weakens morale                                      |
| 4    | The people turn         | Civilians rebel, or key allies withdraw support or lose faith                                            |
| 5    | A fortress is lost      | A real fortress is captured, or a spiritual sanctuary, safe haven, or safe trade route is compromised    |
| 6    | A leader cracks         | A commander is injured or slain, or a political leader suffers mental breakdown or betrayal              |
| 7    | Faith is shaken         | Religious fervor wanes, or ideological conviction falters among troops                                   |
| 8    | Rumors of betrayal      | Actual traitors or spies revealed, or distrust and paranoia spread                                       |
| 9    | Haunted by the dead     | Ghosts or curses plague the area, or past failures weigh heavily on morale                               |
| 10   | A new division forms    | Factions splinter off, or dissent grows within a population or army                                      |

### Battle End

- The battle concludes when the Battle Score reaches its [**threshold**](#battle-start-table) or by the **Battle End** event.
- Roll on the [**Battle End Table**](#battle-end-table) to narrate why the battle ended, **only if it was ended by an event**.
- Determine the victor by the sign of the Battle Score.
- If a battle ends when neither side has at least 4 progress, no momentum is gained.

###### **Battle End Table**

| Roll | Reason                              |
| ---- | ----------------------------------- |
| 1    | Third party intervention            |
| 2    | Exhaustion of forces                |
| 3    | Reinforcements arrive               |
| 4    | Disease outbreak                    |
| 5    | Command failure or death            |
| 6    | Strategic withdrawal                |
| 7    | Weather or terrain intervention     |
| 8    | A prophetic sign or religious event |
| 9    | Supply lines cut                    |
| 10   | Rebellion                           |

# Peace

- A peace offer can only occur after at least 50 days of fighting.
- To determine if a peace offer happens, roll on the [**Peace Offer Chance Table**](#piece-offer-chance-table) when the initiative goes to the leading side.

###### **Piece Offer Chance Table**

| Roll Range | Does Peace Happen |
| ---------- | ----------------- |
| 1-2        | If days > 1000    |
| 3-4        | If days >500      |
| 5-6        | If days > 250     |
| 7-8        | If days >100      |
| 9-10       | If days > 50      |

##### **Peace Outcome Table**

| Roll Range | Outcome                                                               |
| ---------- | --------------------------------------------------------------------- |
| 1–30       | Stalemate: No side gains; both sides withdraw.                        |
| 31–60      | Minor Concessions: Small territorial or trade shifts.                 |
| 61–90      | Uneasy Truce: Tensions remain; limited restructuring.                 |
| 91–120     | Favorable Trade Terms: One side gains economic control.               |
| 121–140    | Regional Advantage: Control over contested zone gained.               |
| 141–160    | Political Shift: Enemy's alliances or leadership weaken.              |
| 161–175    | Strategic Victory: One side secures major war goals.                  |
| 176–190    | Dominant Peace: Victorious side imposes near-total terms.             |
| 191–200    | Decisive Victory: Complete political, military, and symbolic triumph. |