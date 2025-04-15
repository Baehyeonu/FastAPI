from fastapi import APIRouter

from app.dtos.create_metting_reponse import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Metting"], redirect_slashes=False)
mysql_router = APIRouter(prefix="/v1/mysql/mettings", tags=["Meeting"], redirect_slashes=False)
# 원래는 어떤 DB를 쓰는지 URL에 적을 필요는 없습니다.
# 강의에서만 이렇게 적습니다.
# 실전에서는 db 이름을 url에 넣지 마세요


@edgedb_router.post(
    "",
    description="meeting을 생성합니다",
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post(
    "",
    description="meeting을 생성 합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
