import asyncio
from collections import defaultdict
from typing import List

from application.command.find_video_similarity_command import FindVideoSimilarityCommand
from application.external import image_embedding_api, similarity_api
from application.external.model.exercise_counter import ExerciseStage, ExerciseCounter
from application.external.model.similarity import FrameSimilarityDTO
from infrastructure.util import gather_with_concurrency


def find_highest_scored_tag(frameSimilarities: List[FrameSimilarityDTO]) -> FrameSimilarityDTO:  # TODO: should we use score threshold
    score_exercise_map = defaultdict(float)
    for similarity in frameSimilarities:
        score_exercise_map[similarity] += similarity.score

    max_score = -1 * float("inf")
    tagging_data = None
    for data, score in score_exercise_map.items():
        if score > max_score:
            max_score = score
            tagging_data = FrameSimilarityDTO(exerciseId=data.exerciseId,
                                              exerciseName=data.exerciseName,
                                              score=max_score,
                                              tag=data.tag,
                                              order=data.order)

    return tagging_data


def find_window_tags(frameSimilarities: List[FrameSimilarityDTO], size: int = 5) -> List[FrameSimilarityDTO]:
    n = len(frameSimilarities)
    idx = 0

    windowSimilarities = []
    while idx < n:
        windowSimilarities.append(find_highest_scored_tag(frameSimilarities[idx: idx + size]))
        idx += size

    return windowSimilarities


def count_correct_exercises(exerciseId: int, windowSimilarities: List[FrameSimilarityDTO]) -> int:

    exerciseCounter = ExerciseCounter(exerciseId)

    for similarity in windowSimilarities:

        if similarity.tag == "1":
            exerciseCounter.__next__(ExerciseStage.BEGINNING)
        elif similarity.tag == "2":
            exerciseCounter.__next__(ExerciseStage.END)

    return exerciseCounter.count


async def handle(command: FindVideoSimilarityCommand):
    command.frames = [frameKeypoints for frameKeypoints in command.frames if len(frameKeypoints.keypoints) != 0]

    video_embedding_response = await image_embedding_api.get_video_embeddings(width=command.width,
                                                                              height=command.height,
                                                                               frames=command.frames)

    frame_similarities = await gather_with_concurrency(100, *[
        similarity_api.search_frame_similarity(vector=pair.vector,
                                               k=command.k,
                                               size=command.size,
                                               index=command.index) for pair in video_embedding_response.frameVectorPairs
    ])

    frame_tags = [find_highest_scored_tag(frame_similarity.frameSimilarities) for frame_similarity in frame_similarities]

    return count_correct_exercises(command.exerciseId,
                                   frame_tags)


