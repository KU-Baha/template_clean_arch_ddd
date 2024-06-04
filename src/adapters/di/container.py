from gettext import gettext

from dependency_injector import containers, providers

from adapters.db.sessions import get_async_session
from application.users import UserRepository
from domain.user.services import UserService


class SessionContainer(containers.DeclarativeContainer):
    session = providers.Resource(get_async_session)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "application.apps.users.controllers",
    ])

    config = providers.Configuration(yaml_files=["config.yml"])

    user_repository = providers.Singleton(
        UserRepository,
        session=SessionContainer.session
    )

    user_service = providers.Singleton(
        UserService,
        user_repository=user_repository,
        gettext=gettext,
        logger=None
    )
