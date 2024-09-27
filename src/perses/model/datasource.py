from typing import Annotated, Literal, Optional, Union

from pydantic import Field

from perses.model.common import BaseModel, Display, HTTPProxy, ObjectMetadata


class PrometheusDatasourceSpec(BaseModel):
    direct_url: Optional[str] = None
    proxy: Optional[HTTPProxy] = None
    scrape_interval: Optional[str] = Field(
        pattern=r"^(?:(\\d+)y)?(?:(\\d+)w)?(?:(\\d+)d)?(?:(\\d+)h)?(?:(\\d+)m)?(?:(\\d+)s)?(?:(\\d+)ms)?$",
        default=None,
    )


class PrometheusDatasource(BaseModel):
    kind: Literal["PrometheusDatasource"] = "PrometheusDatasource"
    spec: PrometheusDatasourceSpec


class TempoDatasourceSpec(BaseModel):
    direct_url: Optional[str] = None
    proxy: Optional[HTTPProxy] = None


class TempoDatasource(BaseModel):
    kind: Literal["TempoDatasource"] = "TempoDatasource"
    spec: TempoDatasourceSpec


DatasourcePlugin = Annotated[Union[PrometheusDatasource, TempoDatasource], Field(discriminator="kind")]


class DatasourceSpec(BaseModel):
    plugin: DatasourcePlugin
    display: Display = Field(default_factory=Display)
    default: bool = False


class Datasource(BaseModel):
    kind: Literal["Datasource"] = "Datasource"
    metadata: ObjectMetadata
    spec: DatasourceSpec


class GlobalDatasource(BaseModel):
    kind: Literal["GlobalDatasource"] = "GlobalDatasource"
    metadata: ObjectMetadata
