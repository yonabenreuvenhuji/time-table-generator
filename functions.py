from copy import deepcopy

from time_table_types import Schedule, TimeTable


def generate_time_table() -> TimeTable:
    return [{i + 8: "_________" for i in range(12)} for _ in range(5)]


type_to_letter = {"class": "C", "exercise": "E", "lab": "L"}


def time_table_to_matrix(time_table: TimeTable) -> list[list[str]]:
    return [[time_table[j][i + 8] for j in range(5)] for i in range(12)]


def print_time_table(time_table: TimeTable) -> None:
    matrix = time_table_to_matrix(time_table)
    for i, row in enumerate(matrix):
        hour = str(i + 8).zfill(2)
        print(hour + ":00-" + hour + ":45  " + " ".join(row))
        print()


def create_time_tables_recursive(
    time_table: TimeTable,
    class_schedule: Schedule,
    min_start_time: int,
    max_end_time: int,
    time_tables: list[TimeTable],
) -> None:
    if len(class_schedule) == 0:
        time_tables.append(time_table)
        return
    exercise, *rest = class_schedule
    for group in exercise["groups"]:
        is_group_ok = True
        time_table_copy = deepcopy(time_table)
        for time in group["times"]:
            if (
                time["start_time"] < min_start_time
                or time["start_time"] + time["hours"] > max_end_time
            ):
                is_group_ok = False
            for index in range(time["hours"]):
                if (
                    time_table_copy[time["day"] - 1][time["start_time"] + index]
                    != "_________"
                ):
                    is_group_ok = False
                else:
                    time_table_copy[time["day"] - 1][
                        time["start_time"] + index
                    ] = (
                        str(exercise["course"])
                        + "_"
                        + type_to_letter[exercise["type"]]
                        + "_"
                        + str(group["number"])
                    )
        if is_group_ok:
            create_time_tables_recursive(
                time_table_copy, rest, min_start_time, max_end_time, time_tables
            )


def create_time_tables(
    class_schedule: Schedule, min_start_time: int = 0, max_end_time: int = 20
) -> list[TimeTable]:
    time_tables: list[TimeTable] = []
    time_table = generate_time_table()
    create_time_tables_recursive(
        time_table, class_schedule, min_start_time, max_end_time, time_tables
    )
    return time_tables


def get_hour_count(time_table: TimeTable):
    matrix = time_table_to_matrix(time_table)
    count = 0
    for index, row in enumerate(matrix):
        for column in row:
            if column != "_________":
                count += index
    return count


def get_daily_average_average(time_table: TimeTable):
    average_sum = 0
    for day in time_table:
        count = 0
        day_sum = 0
        for hour in day:
            if day[hour] != "_________":
                count += 1
                day_sum += hour
        if count != 0:
            average_sum += day_sum / count
    return average_sum / len(time_table)
