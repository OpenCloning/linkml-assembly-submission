from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class Category(ConfiguredBaseModel):
    id: str = Field(..., description="""The identifier for the object""")
    title: Optional[str] = Field(None, description="""A title for the representation of the object""")
    description: Optional[str] = Field(None, description="""A description of the object""")
    image: Optional[str] = Field(None, description="""Path to an image of the object""")


class Kit(ConfiguredBaseModel):
    pmid: str = Field(..., description="""The PubMed ID for the object""")
    addgene_url: Optional[str] = Field(None, description="""The Addgene URL for the object""")


class Sequence(ConfiguredBaseModel):
    plasmid_name: Optional[str] = Field(None)
    addgene_id: str = Field(..., description="""The Addgene ID for the plasmid""")
    category: Optional[str] = Field(None)
    resistance: Optional[str] = Field(None)
    well: Optional[str] = Field(None, description="""The well where a plasmid is located in a plate""")
    description: Optional[str] = Field(None, description="""A description of the object""")

    @field_validator('addgene_id')
    def pattern_addgene_id(cls, v):
        pattern=re.compile(r"^\d+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid addgene_id format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid addgene_id format: {v}")
        return v


class Submitter(ConfiguredBaseModel):
    full_name: Optional[str] = Field(None, description="""The full name of the submitter, will be ignored if the name can be taken from ORCID""")
    orcid: Optional[str] = Field(None, description="""The ORCID of the submitter""")
    github_username: Optional[str] = Field(None, description="""The GitHub username of the submitter""")


class Assembly(ConfiguredBaseModel):
    title: Optional[str] = Field(None, description="""A title for the representation of the object""")
    description: Optional[str] = Field(None, description="""A description of the object""")
    fragment_order: Optional[List[str]] = Field(default_factory=list)


class Submission(ConfiguredBaseModel):
    submitters: Optional[List[Submitter]] = Field(default_factory=list)
    kit: Optional[Kit] = Field(None)
    sequences: Optional[List[Sequence]] = Field(default_factory=list)
    categories: Optional[List[Category]] = Field(default_factory=list)
    assemblies: Optional[List[Assembly]] = Field(default_factory=list)


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Category.model_rebuild()
Kit.model_rebuild()
Sequence.model_rebuild()
Submitter.model_rebuild()
Assembly.model_rebuild()
Submission.model_rebuild()

