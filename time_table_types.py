from typing import TypedDict


class Time(TypedDict):
    day: int
    start_time: int
    hours: int


class Group(TypedDict):
    number: int
    times: list[Time]


class Course(TypedDict):
    course: int
    type: str
    points: int
    groups: list[Group]


Schedule = list[Course]
TimeTable = list[dict[int, str]]
