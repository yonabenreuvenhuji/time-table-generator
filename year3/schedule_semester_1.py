from time_table_types import Schedule

mand_semester_1: Schedule = [
    {
        "course": 83320,
        "type": "class",
        "points": 5,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 1, "start_time": 9, "hours": 3},
                ],
            },
        ],
    },
    {
        "course": 83320,
        "type": "exercise",
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 3, "start_time": 9, "hours": 2},
                ],
            },
            {
                "number": 2,
                "times": [
                    {"day": 1, "start_time": 15, "hours": 2},
                ],
            },
        ],
    },
    {
        "course": 83882,
        "type": "class",
        "points": 5,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 1, "start_time": 12, "hours": 3},
                ],
            },
        ],
    },
    {
        "course": 83882,
        "type": "exercise",
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 3, "start_time": 12, "hours": 2},
                ],
            },
            {
                "number": 2,
                "times": [
                    {"day": 4, "start_time": 14, "hours": 2},
                ],
            },
        ],
    },
    {
        "course": 83510,
        "type": "class",
        "points": 5,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 3, "start_time": 15, "hours": 2},
                    {"day": 4, "start_time": 9, "hours": 2},
                ],
            },
        ],
    },
    {
        "course": 83510,
        "type": "exercise",
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 4, "start_time": 11, "hours": 1},
                ],
            },
            {
                "number": 2,
                "times": [
                    {"day": 4, "start_time": 13, "hours": 1},
                ],
            },
        ],
    },
    {
        "course": 83340,
        "type": "lab",
        "points": 3,
        "groups": [
            {
                "number": 1,
                "times": [
                    {"day": 5, "start_time": 13, "hours": 3},
                ],
            },
            {
                "number": 2,
                "times": [
                    {"day": 5, "start_time": 16, "hours": 3},
                ],
            },
            {
                "number": 3,
                "times": [
                    {"day": 2, "start_time": 9, "hours": 3},
                ],
            },
            {
                "number": 4,
                "times": [
                    {"day": 2, "start_time": 16, "hours": 3},
                ],
            },
        ],
    },
]

spick_semester_1: Schedule = [
    # {
    #     "course": 83922,
    #     "type": "class",
    #     "points": 3,
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 5, "start_time": 9, "hours": 2},
    #             ],
    #         },
    #     ],
    # },
    # {
    #     "course": 83922,
    #     "type": "exercise",
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 5, "start_time": 8, "hours": 1},
    #             ],
    #         },
    #     ],
    # },
    # {
    #     "course": 77693,
    #     "type": "class",
    #     "points": 3,
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 5, "start_time": 11, "hours": 3},
    #             ],
    #         },
    #     ],
    # },
    # {
    #     "course": 83860,
    #     "type": "class",
    #     "points": 3,
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 2, "start_time": 12, "hours": 2},
    #             ],
    #         },
    #     ],
    # },
    # {
    #     "course": 83860,
    #     "type": "exercise",
    #     "groups": [
    #         {
    #             "number": 1,
    #             "times": [
    #                 {"day": 2, "start_time": 14, "hours": 1},
    #             ],
    #         },
    #     ],
    # },
]

pick_semester_1: Schedule = [
    {
        "course": 83413,
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
]

schedule_semester_1 = [
    *mand_semester_1,
    *spick_semester_1,
    *pick_semester_1,
]
