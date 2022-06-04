from fastapi import Depends, FastAPI, APIRouter
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

from settings import settings

router = APIRouter(prefix="/user", tags=["User"])

fief = FiefAsync(
    settings.FIEF_API_DOMAIN,
    settings.FIEF_API_CLIENT_ID,
    settings.FIEF_API_CLIENT_SECRET,
)

scheme = OAuth2AuthorizationCodeBearer(
    f"{settings.FIEF_API_DOMAIN}/authorize",
    f"{settings.FIEF_API_DOMAIN}/api/token",
    scopes={"openid": "openid", "required_scope": "required_scope"},
)

auth = FiefAuth(fief, scheme)


@router.get("")
async def get_user(
    access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated(["openid", "required_scope"])),
):
    return access_token_info


@router.get("/auth_url")
async def auth_url():
    redirect_url = await fief.auth_url(settings.redirect_url(), scope=["openid", "required_scope"])
    from fastapi.logger import logger
    logger.warning(redirect_url)
    return {
        "auth_url": redirect_url,
    }
