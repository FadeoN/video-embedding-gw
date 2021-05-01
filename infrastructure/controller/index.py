
from fastapi import APIRouter
from starlette import status

from application.command import index_exercise_video_command_handler
from application.command.index_exercise_video_command import IndexExerciseVideoCommand
from infrastructure.controller.request.index_exercise_video_request import IndexExerciseVideoRequest

router = APIRouter()


@router.post("/exercise", status_code=status.HTTP_204_NO_CONTENT)
async def index_exercise_video(request: IndexExerciseVideoRequest):
    try:
        await index_exercise_video_command_handler.handle(IndexExerciseVideoCommand(
            exerciseId=request.exerciseId,
            exerciseName=request.exerciseName,
            url=request.url,
            tag=request.tag,
            index=request.index
        ))
        return
    except Exception as e:
        raise e