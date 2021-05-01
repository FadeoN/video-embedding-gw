from application.command.index_exercise_video_command import IndexExerciseVideoCommand
from application.external import image_embedding_api, pose_estimation_api, similarity_api


async def handle(command: IndexExerciseVideoCommand):

    video_keypoint_dto = await pose_estimation_api.get_pose_estimations(command.url)

    video_embedding_response = await image_embedding_api.get_video_embeddings(width=video_keypoint_dto.width,
                                                                     height=video_keypoint_dto.height,
                                                                     frames=video_keypoint_dto.frames)

    index_response = await similarity_api.index_video(exerciseId=command.exerciseId,
                                                      exerciseName=command.exerciseName,
                                                      url=command.url,
                                                      tag=command.tag,
                                                      frameVectorPairs=video_embedding_response.frameVectorPairs,
                                                      index=command.index)

    return index_response
