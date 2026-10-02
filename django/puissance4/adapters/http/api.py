# puissance4/adapters/http/api.py
from ninja import NinjaAPI

from puissance4.application.use_cases import GameNotFound
from puissance4.domain.errors import InvalidMove

from .routes import router

api = NinjaAPI(title="Puissance 4")
api.add_router("/games/", router)


@api.exception_handler(GameNotFound)
def on_game_not_found(request, exc):
    return api.create_response(request, {"detail": "Game not found"}, status=404)


@api.exception_handler(InvalidMove)
def on_invalid_move(request, exc):
    return api.create_response(request, {"detail": str(exc)}, status=409)