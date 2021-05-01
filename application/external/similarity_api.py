import json
from typing import List, Optional

import httpx

from application.external.model.keypoint import IndexExerciseVideoRequest, FrameVectorPair
from infrastructure.configuration import APP_OPTIONS


async def index_video(exerciseId: int, exerciseName: str, url: str, tag: str, frameVectorPairs: List[FrameVectorPair], index: Optional[str] = None):
    async with httpx.AsyncClient() as client:
        endpoint = f"{APP_OPTIONS.similarity_api_options.url}/index/exercise"
        request = IndexExerciseVideoRequest(exerciseId=exerciseId,
                                                  exerciseName=exerciseName,
                                                  url=url,
                                                  tag=tag,
                                                  frameVectorPairs=frameVectorPairs,
                                                  index=index)

        return await client.post(endpoint, data=request.json())

