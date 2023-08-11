from time_table_types import Schedule

# Schedule = list
mand_semester_2: Schedule = [
    {
        "course": 83519,
        "type": "workshop",
        "points": 2,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 4, "start_time": 10, "hours": 2},
                ],
            }
        ],
    },
    {
        "course": 67653,
        "type": "class",
        "points":4,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 2, "start_time": 16, "hours": 2},
                ],
            }
        ],
    },
    {
        "course": 67653,
        "type": "exercise",
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 3, "start_time": 17, "hours": 2},
                ],
            },
            {
                "number": 2,
                "times": [
                    {"day": 3, "start_time": 8, "hours": 2},
                ],
            },
        ],
    },
    {
        "course": 83394,
        "type": "lab",
        "points": 4,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 1, "start_time": 15, "hours": 4},
                ],
            },
            {
                "number": 2,
                "times": [
                    {"day": 5, "start_time": 15, "hours": 4},
                ],
            },
            {
                "number": 3,
                "times": [
                    {"day": 1, "start_time": 8, "hours": 4},
                ],
            },
        ],
    },
    {
        "course": 83879,
        "type": "class",
        "points":5,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 2, "start_time": 8, "hours": 3},
                ],
            }
        ],
    },
    {
        "course": 83879,
        "type": "exercise",
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 1, "start_time": 12, "hours": 2},
                ],
            },
        ],
    },
]

spick_semester_2: Schedule = [
    {
        "course": 83839,
        "type": "class",
        "points": 3,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 2, "start_time": 12, "hours": 2},
                    # {"day": 4, "start_time": 10, "hours": 2},
                ],
            }
        ],
    },
    {
        "course": 83836,
        "type": "class",
        "points": 3,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 3, "start_time": 9, "hours": 2},
                    {"day": 3, "start_time": 11, "hours": 1},
                ],
            }
        ],
    },
]

pick_semester_2: Schedule = [ 
    # {
    #     "course": 83812,
    #     "type": "class",
    #     "points": 5,
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 3, "start_time": 14, "hours": 2},
    #                 {"day": 2, "start_time": 14, "hours": 2},
    #             ],
    #         },
    #     ],
    # },
    # {
    #     "course": 83812,
    #     "type": "exercise",
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 2, "start_time": 11, "hours": 1},
    #             ],
    #         },
    #         # {
    #         #     "number": 2,
    #         #     "times": [
    #         #         {"day": 2, "start_time": 12, "hours": 1},
    #         #     ],
    #         # },
    #     ],
    # },
    {
        "course": 83414,
        "type": "class",
        "points": 4,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 5, "start_time": 8, "hours": 4},
                ],
            },
        ],
    },
    # {
    #     "course": 83915,
    #     "type": "class",
    #     "points": 3,
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 4, "start_time": 16, "hours": 2},
    #             ],
    #         },
    #     ],
    # },
    # {
    #     "course": 83915,
    #     "type": "exercise",
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 4, "start_time": 18, "hours": 2},
    #             ],
    #         },
    #     ],
    # },
]

schedule_semester_2 = [
    *mand_semester_2,
    *spick_semester_2,
    *pick_semester_2,
]


print(len(schedule_semester_2))