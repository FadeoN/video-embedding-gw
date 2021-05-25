from fastapi import APIRouter
from starlette import status

from application.command import find_video_similarity_command_handler
from application.command.find_video_similarity_command import FindVideoSimilarityCommand
from application.external.model.similarity import FrameSimilarityResponse
from infrastructure.controller.request.video_similarity_request import VideoSimilarityRequest

router = APIRouter()


@router.post("/video", status_code=status.HTTP_200_OK)
async def find_video_similarity(request: VideoSimilarityRequest) -> FrameSimilarityResponse:
    try:
        return await find_video_similarity_command_handler.handle(FindVideoSimilarityCommand(
            exerciseId=request.exerciseId,
            width=request.width,
            height=request.height,
            frames=request.frames,
            k=request.k,
            size=request.size,
            index=request.index
        ))
    except Exception as e:
        raise e
