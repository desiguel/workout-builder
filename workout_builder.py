import random
import datetime as dt


class WorkoutBuilder(object):
    execises = {
        0:{"name": "DB bench", "exercise_type": "weights"},
        1:{"name": "DB rows", "exercise_type": "weights"},
        2:{"name": "DB front squat", "exercise_type": "weights"},
        3:{"name": "DB reverse flys", "exercise_type": "weights"},
        4:{"name": "DB walking lunge", "exercise_type": "weights"},
        5:{"name": "DB OH squat", "exercise_type": "weights"},
        6:{"name": "DB step ups", "exercise_type": "weights"},
        7:{"name": "DB deadlift", "exercise_type": "weights"},
        8:{"name": "DB curl and press", "exercise_type": "weights"},
        9:{"name": "pullups", "exercise_type": "hard weights"},
        10:{"name": "chinups", "exercise_type": "hard weights"},
        11:{"name": "tri-dip", "exercise_type": "hard weights"},
        12:{"name": "step knee-ups", "exercise_type": "dynamic"},
        13:{"name": "squats", "exercise_type": "dynamic"},
        14:{"name": "sumo squats", "exercise_type": "dynamic"},
        15:{"name": "jump squats", "exercise_type": "dynamic"},
        16:{"name": "split squat", "exercise_type": "dynamic"},
        17:{"name": "burpees", "exercise_type": "hard dynamic"},
        18:{"name": "lunges", "exercise_type": "dynamic"},
        19:{"name": "sideways lunges", "exercise_type": "dynamic"},
        20:{"name": "high knees", "exercise_type": "dynamic"},
        21:{"name": "broad jump", "exercise_type": "hard dynamic"},
        22:{"name": "mountain climbers", "exercise_type": "dynamic"},
        23:{"name": "box jumps", "exercise_type": "hard dynamic"},
        24:{"name": "skipping", "exercise_type": "time"},
        25:{"name": "commandos", "exercise_type": "hard dynamic"},
        26:{"name": "plank", "exercise_type": "time"},
        27:{"name": "bridges", "exercise_type": "dynamic"},
        28:{"name": "superman", "exercise_type": "dynamic"},
        29:{"name": "quadrupeds", "exercise_type": "dynamic"},
        30:{"name": "pushups", "exercise_type": "hard dynamic"},
        31:{"name": "hanging leg raises", "exercise_type": "dynamic"},
        32:{"name": "crunches", "exercise_type": "dynamic"},
        33:{"name": "ab-bikes", "exercise_type": "dynamic"},
        34:{"name": "russian twists", "exercise_type": "dynamic"},

    }

    incompatibility_lists = {
        0: [25, 26, 30, ],
        1: [],
        2: [5, 13, 14, 16, ],
        3: [],
        4: [18, ],
        5: [2, 8, 13, 14, 16, ],
        6: [12, ],
        7: [],
        8: [5, 10, ],
        9: [10, ],
        10: [8, 9, ],
        11: [],
        12: [6, ],
        13: [2, 5, 14, 16, ],
        14: [2, 5, 13, 16, ],
        15: [16, 23, ],
        16: [2, 5, 13, 14, 15, ],
        17: [22, 25, 30, ],
        18: [4, ],
        19: [],
        20: [23, 25, 31, ],
        21: [23, 31, ],
        22: [17, 25, 26, 30, ],
        23: [15, 20, 21, ],
        24: [],
        25: [0, 17, 20, 22, 26, 30, ],
        26: [0, 22, 25, 30, 33, 34, ],
        27: [],
        28: [29, ],
        29: [28, ],
        30: [0, 17, 22, 25, 26, ],
        31: [20, 21, ],
        32: [33, 34, ],
        33: [26, 32, 34, ],
        34: [26, 32, 33, ],

    }

    def build_random_workout(self, num_exercises=4, num_circuits=2):

        workout_index = list(self.execises.keys())

        weights_reps_list = [i + 1 for i in range(4, 8)]
        hard_weights_reps_list = [i + 1 for i in range(2, 4)]
        time_seconds_list = [45, 60, 80]
        dynamic_reps_list = [15, 20, 25]
        hard_dynamic_reps_list = [15]

        random.seed(dt.datetime.now())
        weights_reps = random.choice(weights_reps_list)
        hard_weights_reps = random.choice(hard_weights_reps_list)
        time_seconds = random.choice(time_seconds_list)
        dynamic_reps = random.choice(dynamic_reps_list)
        hard_dynamic_reps = random.choice(hard_dynamic_reps_list)

        for circuit_num in range(0, num_circuits):

            print("Circuit {}:\n".format(circuit_num + 1))

            for workout_num in range(0, num_exercises):

                random.seed(dt.datetime.now())
                workout_selection = random.choice(workout_index)

                # Remove incompatible execises
                for incompatible_execise_index in self.incompatibility_lists[workout_selection]:
                    if incompatible_execise_index in workout_index:
                        workout_index.remove(incompatible_execise_index)

                # Remove original selection
                workout_index.remove(workout_selection)

                if self.execises[workout_selection]["exercise_type"] == "time":
                    reps_statement = " for {} seconds".format(time_seconds)
                elif self.execises[workout_selection]["exercise_type"] == "weights":
                    reps_statement = " x {} reps".format(weights_reps)
                elif self.execises[workout_selection]["exercise_type"] == "hard weights":
                    reps_statement = " x {} reps".format(hard_weights_reps)
                elif self.execises[workout_selection]["exercise_type"] == "hard dynamic":
                    reps_statement = " x {} reps".format(hard_dynamic_reps)
                else:
                    reps_statement = " x {} reps".format(dynamic_reps)

                print("{}".format(self.execises[workout_selection]["name"], ) + reps_statement)

            print("\n")


if __name__ == "__main__":
    workout_builder = WorkoutBuilder()
    workout_builder.build_random_workout()
