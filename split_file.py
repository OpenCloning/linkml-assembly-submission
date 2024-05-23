from pandas import read_excel
from dummy import (
    Sequence as _Sequence,
    Submission as _Submission,
    Category as _Category,
    Assembly as _Assembly,
)


from pydantic import ConfigDict
import numpy as np
from linkml_runtime.loaders import (
    CSVLoader,
    JSONLoader,
    RDFLibLoader,
    TSVLoader,
    YAMLLoader,
)
from linkml_runtime import SchemaView
from pydantic import BaseModel
import json

# TODO: validation of categories in sequences and assemblies
# TODO: validate images
# TODO: allow specify enzyme and whether it is or not a Golden Gate assembly


class Sequence(_Sequence):
    """Allow extra fields and custom model dump"""

    model_config = ConfigDict(extra="allow")

    def to_source_option(self):
        info = dict()
        # All fields that are not part of the source
        for k, v in self.model_dump().items():
            # Drop category
            if k == "category":
                continue
            if k not in ["addgene_id"]:
                info[k] = v
        if self.description:
            option_name = f"{self.description} - {self.plasmid_name}"
        else:
            option_name = self.plasmid_name
        return {
            "name": option_name,
            "source": {
                "type": "AddGeneIdSource",
                "repository_name": "addgene",
                "repository_id": self.addgene_id,
            },
            "info": info,
        }


class Category(_Category):
    def to_source(self, source_id: int, options: list[Sequence]):
        return {
            "id": source_id,
            "input": [],
            "output": source_id + 1,
            "is_template": True,
            "type": "CollectionSource",
            "category_id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "options": [s.to_source_option() for s in options if s.category == self.id],
        }


class Assembly(_Assembly):
    def to_template(self, categories: list[Category], sequences: list[Sequence]):
        sources = list()
        dummy_sequences = list()
        source_id = 1
        final_assembly_inputs = list()
        for category_id in self.fragment_order:

            # A category-derived source
            if category_id:
                category = next(c for c in categories if c.id == category_id)
                sources.append(category.to_source(source_id, sequences))
            # An empty slot
            else:
                sources.append(
                    {
                        "id": source_id,
                        "input": [],
                        "output": source_id + 1,
                        "is_template": True,
                    }
                )
                dummy_sequences.append(
                    {"id": source_id + 1, "type": "TemplateSequence"}
                )
                source_id += 2
                sources.append(
                    {
                        "id": source_id,
                        "input": [source_id - 1],
                        "output": source_id + 1,
                        "is_template": True,
                        "type": "PCRSource",
                    }
                )
            final_assembly_inputs.append(source_id + 1)
            dummy_sequences.append({"id": source_id + 1, "type": "TemplateSequence"})
            source_id += 2

        sources.append(
            {
                "id": source_id,
                "input": final_assembly_inputs,
                "output": source_id + 1,
                "is_template": True,
                "type": "RestrictionAndLigationSource",
            }
        )
        dummy_sequences.append(
            {
                "id": source_id + 1,
                "type": "TemplateSequence",
            }
        )

        return {
            "sources": sources,
            "sequences": dummy_sequences,
            "description": f"{self.title}\n\n{self.description}",
        }


class Submission(_Submission):
    """Allow extra fields and custom model dump"""

    sequences: list[Sequence]
    categories: list[Category]
    assemblies: list[Assembly]

    def to_template_list(self):
        return [
            a.to_template(self.categories, self.sequences)
            for i, a in enumerate(self.assemblies)
        ]


def sheet_reader(sheet_name):

    return (
        read_excel("test_join.xlsx", sheet_name=sheet_name, dtype=str)
        .fillna(np.nan)
        .replace([np.nan], [None])
        # .to_dict("records")
    )


sequences = sheet_reader("Sequence")
categories = sheet_reader("Category")
kits = sheet_reader("Kit")
submitters = sheet_reader("Submitter")
assemblies = sheet_reader("Assembly")
submitters = sheet_reader("Submitter")


submission = Submission.model_validate(
    {
        "sequences": sequences,
        "categories": categories,
        "kit": kits[0],
        "submitters": submitters,
        "assemblies": assemblies,
    }
)

with open("submission.json", "w") as f:
    json.dump(submission.model_dump(), f, indent=2)


for i, template in enumerate(submission.to_template_list()):
    with open(f"templates/template_{i}.json", "w") as f:
        json.dump(template, f, indent=2)

# schema_view = SchemaView(
#     "src/linkml_assembly_submission/schema/linkml_assembly_submission.yaml"
# )

# Get type of fields in Sequence model
# print(Sequence.model_fields["category"].annotation)

# class SequenceContainer(BaseModel):
#     sequences: list[Sequence]


# if len(kits) != 1:
#     raise ValueError("Expected 1 kit, got {}".format(len(kits)))
# loader = TSVLoader()

# sequences.to_csv("blah.tsv", sep="\t")

# loader.load(
#     "blah.tsv", SequenceContainer, schemaview=schema_view, index_slot="sequences"
# )
