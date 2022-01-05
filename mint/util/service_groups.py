from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "mint_harvester mint_timelord_launcher mint_timelord mint_farmer mint_full_node mint_wallet".split(),
    "node": "mint_full_node".split(),
    "harvester": "mint_harvester".split(),
    "farmer": "mint_harvester mint_farmer mint_full_node mint_wallet".split(),
    "farmer-no-wallet": "mint_harvester mint_farmer mint_full_node".split(),
    "farmer-only": "mint_farmer".split(),
    "timelord": "mint_timelord_launcher mint_timelord mint_full_node".split(),
    "timelord-only": "mint_timelord".split(),
    "timelord-launcher-only": "mint_timelord_launcher".split(),
    "wallet": "mint_wallet mint_full_node".split(),
    "wallet-only": "mint_wallet".split(),
    "introducer": "mint_introducer".split(),
    "simulator": "mint_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
