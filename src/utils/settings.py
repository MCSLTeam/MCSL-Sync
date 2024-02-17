from orjson import loads, dumps, OPT_INDENT_2
from os import path as osp, makedirs
from .logger import SyncLogger

SyncLogger.info("Reading settings...")
config_template = {"fast_loading": True, "debug": True}
cfg = config_template.copy()  # type: dict
makedirs("data", exist_ok=True)
makedirs("logs", exist_ok=True)


if not osp.exists("data/settings.json"):
    with open(
        file="data/settings.json",
        mode="wb+",
    ) as newConfig:
        newConfig.write(dumps(config_template, option=OPT_INDENT_2))
else:
    pass
with open(file="data/settings.json", mode="r", encoding="utf-8") as f:
    cfg = loads(f.read())
