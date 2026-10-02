# puissance4/adapters/http/routes.py
from uuid import UUID

from ninja import Router

# from puissance4 import container

# from .schemas import GameOut, MoveIn

router = Router(tags=["games"])

@router.get("/", response={201: dict})
def hello_world(request):
    return 201, {"message" : "Hello world"}

# @router.post("/", response={201, dict})
# def create_game(request):
#     return 201, { "message": "Hello world"}


# @router.post("/{game_id}/moves", response=GameOut)
# def play_move(request, game_id: UUID, payload: MoveIn):
#     return container.play_move.execute(game_id, payload.column)