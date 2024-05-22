# Auto generated from linkml_assembly_submission.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-22T14:39:52
# Schema: linkml-assembly-submission
#
# id: https://w3id.org/genestorian/linkml-assembly-submission
# description: A linkml model for submissions of assemblies for ShareYourCloning templates
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_ASSEMBLY_SUBMISSION = CurieNamespace('linkml_assembly_submission', 'https://w3id.org/genestorian/linkml-assembly-submission/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = LINKML_ASSEMBLY_SUBMISSION


# Types
class PMIDIdentifier(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PMID identifier"
    type_model_uri = LINKML_ASSEMBLY_SUBMISSION.PMIDIdentifier


class HttpsIdentifier(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "https identifier"
    type_model_uri = LINKML_ASSEMBLY_SUBMISSION.HttpsIdentifier


class OrcidIdentifier(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "orcid identifier"
    type_model_uri = LINKML_ASSEMBLY_SUBMISSION.OrcidIdentifier


# Class references
class CategoryId(extended_str):
    pass


class KitPmid(PMIDIdentifier):
    pass


class SequenceAddgeneId(extended_int):
    pass


@dataclass
class Category(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Category"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Category

    id: Union[str, CategoryId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CategoryId):
            self.id = CategoryId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.image is not None and not isinstance(self.image, str):
            self.image = str(self.image)

        super().__post_init__(**kwargs)


@dataclass
class Kit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Kit"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Kit"
    class_name: ClassVar[str] = "Kit"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Kit

    pmid: Union[str, KitPmid] = None
    addgene_url: Optional[Union[str, HttpsIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.pmid):
            self.MissingRequiredField("pmid")
        if not isinstance(self.pmid, KitPmid):
            self.pmid = KitPmid(self.pmid)

        if self.addgene_url is not None and not isinstance(self.addgene_url, HttpsIdentifier):
            self.addgene_url = HttpsIdentifier(self.addgene_url)

        super().__post_init__(**kwargs)


@dataclass
class Sequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Sequence"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Sequence

    addgene_id: Union[int, SequenceAddgeneId] = None
    plasmid_name: Optional[str] = None
    category: Optional[Union[str, CategoryId]] = None
    resistance: Optional[str] = None
    well: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.addgene_id):
            self.MissingRequiredField("addgene_id")
        if not isinstance(self.addgene_id, SequenceAddgeneId):
            self.addgene_id = SequenceAddgeneId(self.addgene_id)

        if self.plasmid_name is not None and not isinstance(self.plasmid_name, str):
            self.plasmid_name = str(self.plasmid_name)

        if self.category is not None and not isinstance(self.category, CategoryId):
            self.category = CategoryId(self.category)

        if self.resistance is not None and not isinstance(self.resistance, str):
            self.resistance = str(self.resistance)

        if self.well is not None and not isinstance(self.well, str):
            self.well = str(self.well)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Submitter(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Submitter"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Submitter"
    class_name: ClassVar[str] = "Submitter"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Submitter

    full_name: Optional[str] = None
    orcid: Optional[Union[str, OrcidIdentifier]] = None
    github_username: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.full_name is not None and not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self.orcid is not None and not isinstance(self.orcid, OrcidIdentifier):
            self.orcid = OrcidIdentifier(self.orcid)

        if self.github_username is not None and not isinstance(self.github_username, str):
            self.github_username = str(self.github_username)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.id, name="id", curie=LINKML_ASSEMBLY_SUBMISSION.curie('id'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.id, domain=None, range=URIRef)

slots.title = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.title, name="title", curie=LINKML_ASSEMBLY_SUBMISSION.curie('title'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.title, domain=None, range=Optional[str])

slots.description = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.description, name="description", curie=LINKML_ASSEMBLY_SUBMISSION.curie('description'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.description, domain=None, range=Optional[str])

slots.image = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.image, name="image", curie=LINKML_ASSEMBLY_SUBMISSION.curie('image'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.image, domain=None, range=Optional[str])

slots.pmid = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.pmid, name="pmid", curie=LINKML_ASSEMBLY_SUBMISSION.curie('pmid'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.pmid, domain=None, range=URIRef)

slots.addgene_url = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.addgene_url, name="addgene_url", curie=LINKML_ASSEMBLY_SUBMISSION.curie('addgene_url'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.addgene_url, domain=None, range=Optional[Union[str, HttpsIdentifier]])

slots.plasmid_name = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.plasmid_name, name="plasmid_name", curie=LINKML_ASSEMBLY_SUBMISSION.curie('plasmid_name'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.plasmid_name, domain=None, range=Optional[str])

slots.addgene_id = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.addgene_id, name="addgene_id", curie=LINKML_ASSEMBLY_SUBMISSION.curie('addgene_id'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.addgene_id, domain=None, range=URIRef)

slots.category = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.category, name="category", curie=LINKML_ASSEMBLY_SUBMISSION.curie('category'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.category, domain=None, range=Optional[Union[str, CategoryId]])

slots.resistance = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.resistance, name="resistance", curie=LINKML_ASSEMBLY_SUBMISSION.curie('resistance'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.resistance, domain=None, range=Optional[str])

slots.well = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.well, name="well", curie=LINKML_ASSEMBLY_SUBMISSION.curie('well'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.well, domain=None, range=Optional[str])

slots.full_name = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.full_name, name="full_name", curie=LINKML_ASSEMBLY_SUBMISSION.curie('full_name'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.full_name, domain=None, range=Optional[str])

slots.orcid = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.orcid, name="orcid", curie=LINKML_ASSEMBLY_SUBMISSION.curie('orcid'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.orcid, domain=None, range=Optional[Union[str, OrcidIdentifier]])

slots.github_username = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.github_username, name="github_username", curie=LINKML_ASSEMBLY_SUBMISSION.curie('github_username'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.github_username, domain=None, range=Optional[str])