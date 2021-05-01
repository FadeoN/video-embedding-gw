import json

import httpx

from application.external.model.keypoint import VideoKeypointResponse, PredictVideoPoseRequest
from infrastructure.configuration import APP_OPTIONS


async def get_pose_estimations(url: str) -> VideoKeypointResponse:
    async with httpx.AsyncClient(timeout=APP_OPTIONS.pose_estimation_api_options.timeout) as client:
        endpoint = f"{APP_OPTIONS.pose_estimation_api_options.url}/pose-estimation/video"
        request = PredictVideoPoseRequest(url=url)
        response = await client.post(endpoint, data=request.json())

    return VideoKeypointResponse.parse_raw(response.content)
