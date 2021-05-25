from enum import Enum

class ExerciseStage(Enum):

    NONE = 0
    BEGINNING = 1
    END = 2


class ExerciseCounter:

    def __init__(self,
                 exerciseId: int):
        self.exerciseId = exerciseId
        self.count = 0
        self.current_stage = ExerciseStage.NONE

    def __next__(self, stage: ExerciseStage):

        if self.current_stage == ExerciseStage.BEGINNING and stage == ExerciseStage.END:
            self.current_stage = stage
        elif self.current_stage in [ExerciseStage.NONE, ExerciseStage.END] and stage == ExerciseStage.BEGINNING:
            self.current_stage = stage
            self.count += 1
