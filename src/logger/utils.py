from typing import Optional

from fastapi.requests import Request
from starlette.routing import Match


def get_route_template(request: Request) -> str:
    for route in request.app.routes:
        match, child_scope = route.matches(request.scope)
        if match == Match.FULL:
            return route.path

    return request.url.path


def get_user_agent(request: Request) -> Optional[str]:
    headers = request.headers
    if not headers:
        return None

    key = "user-agent"
    if key in headers:
        return headers.get(key)

    return None
