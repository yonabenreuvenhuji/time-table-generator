from functions import (
    create_time_tables,
    get_daily_average_average,
    get_hour_count,
    print_time_table,
    get_points,
)
from year3.schedule_semester_1 import (
    schedule_semester_1,
    mand_semester_1,
    spick_semester_1,
    pick_semester_1,
)
from year3.schedule_semester_2 import (
    schedule_semester_2,
    mand_semester_2,
    spick_semester_2,
    pick_semester_2,
)

time_tables = create_time_tables(
    # min_start_time=9,
    # class_schedule=schedule_semester_1,
    # max_end_time=16,
    class_schedule=schedule_semester_2,
    # max_end_time=18,
)

func = get_hour_count
# func = get_daily_average_average


sorted_time_tables = sorted(time_tables, key=func, reverse=True)

for time_table in sorted_time_tables:
    print()
    print()
    print(func(time_table))
    print_time_table(time_table)

print(len(sorted_time_tables))

print("semester 1:")
print("mand: ", get_points(mand_semester_1))
print("spick: ", get_points(spick_semester_1))
print("pick: ", get_points(pick_semester_1))
print("total: ", get_points(schedule_semester_1))
print()
print()
print("semester 2:")
print("mand: ", get_points(mand_semester_2))
print("spick: ", get_points(spick_semester_2))
print("pick: ", get_points(pick_semester_2))
print("total: ", get_points(schedule_semester_2))
