# Auto generated from linkml_assembly_submission.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-07-02T16:50:26
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


class DnaSequence(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "dna_sequence"
    type_model_uri = LINKML_ASSEMBLY_SUBMISSION.DnaSequence


# Class references
class CategoryId(extended_str):
    pass


class AddGenePlasmidAddgeneId(extended_str):
    pass


class OligoName(extended_str):
    pass


class OligoPairName(extended_str):
    pass


@dataclass
class Category(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Category"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Category

    id: Union[str, CategoryId] = None
    title: str = None
    description: Optional[str] = None
    image: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CategoryId):
            self.id = CategoryId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
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

    addgene_url: Union[str, HttpsIdentifier] = None
    title: str = None
    description: str = None
    pmid: Optional[Union[str, PMIDIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.addgene_url):
            self.MissingRequiredField("addgene_url")
        if not isinstance(self.addgene_url, HttpsIdentifier):
            self.addgene_url = HttpsIdentifier(self.addgene_url)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.pmid is not None and not isinstance(self.pmid, PMIDIdentifier):
            self.pmid = PMIDIdentifier(self.pmid)

        super().__post_init__(**kwargs)


@dataclass
class Sequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Sequence"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Sequence

    name: str = None
    category: Union[str, CategoryId] = None
    description: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, CategoryId):
            self.category = CategoryId(self.category)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class AddGenePlasmid(Sequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["AddGenePlasmid"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:AddGenePlasmid"
    class_name: ClassVar[str] = "AddGenePlasmid"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.AddGenePlasmid

    addgene_id: Union[str, AddGenePlasmidAddgeneId] = None
    name: str = None
    category: Union[str, CategoryId] = None
    resistance: Optional[str] = None
    well: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.addgene_id):
            self.MissingRequiredField("addgene_id")
        if not isinstance(self.addgene_id, AddGenePlasmidAddgeneId):
            self.addgene_id = AddGenePlasmidAddgeneId(self.addgene_id)

        if self.resistance is not None and not isinstance(self.resistance, str):
            self.resistance = str(self.resistance)

        if self.well is not None and not isinstance(self.well, str):
            self.well = str(self.well)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Submitter(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Submitter"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Submitter"
    class_name: ClassVar[str] = "Submitter"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Submitter

    full_name: str = None
    orcid: Optional[Union[str, OrcidIdentifier]] = None
    github_username: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.full_name):
            self.MissingRequiredField("full_name")
        if not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self.orcid is not None and not isinstance(self.orcid, OrcidIdentifier):
            self.orcid = OrcidIdentifier(self.orcid)

        if self.github_username is not None and not isinstance(self.github_username, str):
            self.github_username = str(self.github_username)

        super().__post_init__(**kwargs)


@dataclass
class Oligo(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Oligo"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Oligo"
    class_name: ClassVar[str] = "Oligo"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Oligo

    name: Union[str, OligoName] = None
    sequence: Union[str, DnaSequence] = None
    id: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, OligoName):
            self.name = OligoName(self.name)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, DnaSequence):
            self.sequence = DnaSequence(self.sequence)

        if self.id is not None and not isinstance(self.id, int):
            self.id = int(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OligoPair(Sequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["OligoPair"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:OligoPair"
    class_name: ClassVar[str] = "OligoPair"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.OligoPair

    name: Union[str, OligoPairName] = None
    category: Union[str, CategoryId] = None
    forward_oligo: Union[str, OligoName] = None
    reverse_oligo: Union[str, OligoName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, OligoPairName):
            self.name = OligoPairName(self.name)

        if self._is_empty(self.forward_oligo):
            self.MissingRequiredField("forward_oligo")
        if not isinstance(self.forward_oligo, OligoName):
            self.forward_oligo = OligoName(self.forward_oligo)

        if self._is_empty(self.reverse_oligo):
            self.MissingRequiredField("reverse_oligo")
        if not isinstance(self.reverse_oligo, OligoName):
            self.reverse_oligo = OligoName(self.reverse_oligo)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Assembly(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Assembly"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Assembly"
    class_name: ClassVar[str] = "Assembly"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Assembly

    title: str = None
    description: Optional[str] = None
    fragment_order: Optional[Union[Union[str, CategoryId], List[Union[str, CategoryId]]]] = empty_list()
    template_file: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.fragment_order, list):
            self.fragment_order = [self.fragment_order] if self.fragment_order is not None else []
        self.fragment_order = [v if isinstance(v, CategoryId) else CategoryId(v) for v in self.fragment_order]

        if self.template_file is not None and not isinstance(self.template_file, str):
            self.template_file = str(self.template_file)

        super().__post_init__(**kwargs)


@dataclass
class Submission(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION["Submission"]
    class_class_curie: ClassVar[str] = "linkml_assembly_submission:Submission"
    class_name: ClassVar[str] = "Submission"
    class_model_uri: ClassVar[URIRef] = LINKML_ASSEMBLY_SUBMISSION.Submission

    submitters: Union[Union[dict, Submitter], List[Union[dict, Submitter]]] = None
    kit: Union[dict, Kit] = None
    sequences: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    categories: Union[Dict[Union[str, CategoryId], Union[dict, Category]], List[Union[dict, Category]]] = empty_dict()
    assemblies: Union[Union[dict, Assembly], List[Union[dict, Assembly]]] = None
    oligos: Optional[Union[Dict[Union[str, OligoName], Union[dict, Oligo]], List[Union[dict, Oligo]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.submitters):
            self.MissingRequiredField("submitters")
        if not isinstance(self.submitters, list):
            self.submitters = [self.submitters] if self.submitters is not None else []
        self.submitters = [v if isinstance(v, Submitter) else Submitter(**as_dict(v)) for v in self.submitters]

        if self._is_empty(self.kit):
            self.MissingRequiredField("kit")
        if not isinstance(self.kit, Kit):
            self.kit = Kit(**as_dict(self.kit))

        if self._is_empty(self.sequences):
            self.MissingRequiredField("sequences")
        if not isinstance(self.sequences, list):
            self.sequences = [self.sequences] if self.sequences is not None else []
        self.sequences = [v if isinstance(v, Sequence) else Sequence(**as_dict(v)) for v in self.sequences]

        if self._is_empty(self.categories):
            self.MissingRequiredField("categories")
        self._normalize_inlined_as_list(slot_name="categories", slot_type=Category, key_name="id", keyed=True)

        if self._is_empty(self.assemblies):
            self.MissingRequiredField("assemblies")
        if not isinstance(self.assemblies, list):
            self.assemblies = [self.assemblies] if self.assemblies is not None else []
        self.assemblies = [v if isinstance(v, Assembly) else Assembly(**as_dict(v)) for v in self.assemblies]

        self._normalize_inlined_as_list(slot_name="oligos", slot_type=Oligo, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.id, name="id", curie=LINKML_ASSEMBLY_SUBMISSION.curie('id'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.id, domain=None, range=URIRef)

slots.title = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.title, name="title", curie=LINKML_ASSEMBLY_SUBMISSION.curie('title'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.title, domain=None, range=str)

slots.description = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.description, name="description", curie=LINKML_ASSEMBLY_SUBMISSION.curie('description'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.description, domain=None, range=Optional[str])

slots.image = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.image, name="image", curie=LINKML_ASSEMBLY_SUBMISSION.curie('image'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.image, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_\-\.]+\.(png|jpg|jpeg|gif|svg)$'))

slots.pmid = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.pmid, name="pmid", curie=LINKML_ASSEMBLY_SUBMISSION.curie('pmid'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.pmid, domain=None, range=Optional[Union[str, PMIDIdentifier]],
                   pattern=re.compile(r'^PMID:\d+$'))

slots.addgene_url = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.addgene_url, name="addgene_url", curie=LINKML_ASSEMBLY_SUBMISSION.curie('addgene_url'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.addgene_url, domain=None, range=Union[str, HttpsIdentifier],
                   pattern=re.compile(r'^https://www.addgene.org/.+$'))

slots.name = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.name, name="name", curie=LINKML_ASSEMBLY_SUBMISSION.curie('name'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.name, domain=None, range=str)

slots.addgene_id = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.addgene_id, name="addgene_id", curie=LINKML_ASSEMBLY_SUBMISSION.curie('addgene_id'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.addgene_id, domain=None, range=URIRef,
                   pattern=re.compile(r'^\d+$'))

slots.category = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.category, name="category", curie=LINKML_ASSEMBLY_SUBMISSION.curie('category'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.category, domain=None, range=Union[str, CategoryId])

slots.resistance = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.resistance, name="resistance", curie=LINKML_ASSEMBLY_SUBMISSION.curie('resistance'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.resistance, domain=None, range=Optional[str])

slots.well = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.well, name="well", curie=LINKML_ASSEMBLY_SUBMISSION.curie('well'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.well, domain=None, range=Optional[str])

slots.full_name = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.full_name, name="full_name", curie=LINKML_ASSEMBLY_SUBMISSION.curie('full_name'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.full_name, domain=None, range=str)

slots.orcid = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.orcid, name="orcid", curie=LINKML_ASSEMBLY_SUBMISSION.curie('orcid'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.orcid, domain=None, range=Optional[Union[str, OrcidIdentifier]],
                   pattern=re.compile(r'^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$'))

slots.github_username = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.github_username, name="github_username", curie=LINKML_ASSEMBLY_SUBMISSION.curie('github_username'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.github_username, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9-]+$'))

slots.type = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.type, name="type", curie=LINKML_ASSEMBLY_SUBMISSION.curie('type'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.type, domain=None, range=Optional[str])

slots.oligo__id = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.id, name="oligo__id", curie=LINKML_ASSEMBLY_SUBMISSION.curie('id'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.oligo__id, domain=None, range=Optional[int])

slots.oligo__sequence = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.sequence, name="oligo__sequence", curie=LINKML_ASSEMBLY_SUBMISSION.curie('sequence'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.oligo__sequence, domain=None, range=Union[str, DnaSequence])

slots.oligoPair__forward_oligo = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.forward_oligo, name="oligoPair__forward_oligo", curie=LINKML_ASSEMBLY_SUBMISSION.curie('forward_oligo'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.oligoPair__forward_oligo, domain=None, range=Union[str, OligoName])

slots.oligoPair__reverse_oligo = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.reverse_oligo, name="oligoPair__reverse_oligo", curie=LINKML_ASSEMBLY_SUBMISSION.curie('reverse_oligo'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.oligoPair__reverse_oligo, domain=None, range=Union[str, OligoName])

slots.assembly__fragment_order = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.fragment_order, name="assembly__fragment_order", curie=LINKML_ASSEMBLY_SUBMISSION.curie('fragment_order'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.assembly__fragment_order, domain=None, range=Optional[Union[Union[str, CategoryId], List[Union[str, CategoryId]]]])

slots.assembly__template_file = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.template_file, name="assembly__template_file", curie=LINKML_ASSEMBLY_SUBMISSION.curie('template_file'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.assembly__template_file, domain=None, range=Optional[str],
                   pattern=re.compile(r'^.*.json$'))

slots.submission__submitters = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.submitters, name="submission__submitters", curie=LINKML_ASSEMBLY_SUBMISSION.curie('submitters'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.submission__submitters, domain=None, range=Union[Union[dict, Submitter], List[Union[dict, Submitter]]])

slots.submission__kit = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.kit, name="submission__kit", curie=LINKML_ASSEMBLY_SUBMISSION.curie('kit'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.submission__kit, domain=None, range=Union[dict, Kit])

slots.submission__sequences = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.sequences, name="submission__sequences", curie=LINKML_ASSEMBLY_SUBMISSION.curie('sequences'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.submission__sequences, domain=None, range=Union[Union[dict, Sequence], List[Union[dict, Sequence]]])

slots.submission__categories = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.categories, name="submission__categories", curie=LINKML_ASSEMBLY_SUBMISSION.curie('categories'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.submission__categories, domain=None, range=Union[Dict[Union[str, CategoryId], Union[dict, Category]], List[Union[dict, Category]]])

slots.submission__assemblies = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.assemblies, name="submission__assemblies", curie=LINKML_ASSEMBLY_SUBMISSION.curie('assemblies'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.submission__assemblies, domain=None, range=Union[Union[dict, Assembly], List[Union[dict, Assembly]]])

slots.submission__oligos = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.oligos, name="submission__oligos", curie=LINKML_ASSEMBLY_SUBMISSION.curie('oligos'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.submission__oligos, domain=None, range=Optional[Union[Dict[Union[str, OligoName], Union[dict, Oligo]], List[Union[dict, Oligo]]]])

slots.Kit_description = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.description, name="Kit_description", curie=LINKML_ASSEMBLY_SUBMISSION.curie('description'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.Kit_description, domain=Kit, range=str)

slots.Oligo_name = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.name, name="Oligo_name", curie=LINKML_ASSEMBLY_SUBMISSION.curie('name'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.Oligo_name, domain=Oligo, range=Union[str, OligoName])

slots.OligoPair_name = Slot(uri=LINKML_ASSEMBLY_SUBMISSION.name, name="OligoPair_name", curie=LINKML_ASSEMBLY_SUBMISSION.curie('name'),
                   model_uri=LINKML_ASSEMBLY_SUBMISSION.OligoPair_name, domain=OligoPair, range=Union[str, OligoPairName])