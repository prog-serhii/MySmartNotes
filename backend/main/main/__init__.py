from dependency_injector import containers, providers

from main.settings import Settings
from foundation import CommandBus
from text_ocr import TextOCRContainer


__all__ = [
    # container
    'ApplicationContainer',
    # settings
    'Settings'
]

settings = Settings()


def override_providers(providers_config):
    ovveride_providers = {}

    for provider_name, provider_info in providers_config.items():
        provided_cls = provider_info['class']
        provider_cls = getattr(providers, provider_info['provider_class'])
        ovveride_providers[provider_name] = provider_cls(provided_cls)

    return ovveride_providers


class ApplicationContainer(containers.DeclarativeContainer):

    config = providers.Configuration(pydantic_settings=[settings])
    # config.from_pydantic(settings, exclude={'text_ocr_package_overriders'})
    command_bus = providers.Singleton(CommandBus)

    text_ocr_package = providers.Container(
        TextOCRContainer, **override_providers(settings.text_ocr_package_overriders)
    )
