from dagster import Definitions, load_assets_from_modules
from . import resources
from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "database": resources.database_resource
    },
)
