-- # Class: "Category" Description: ""
--     * Slot: id Description: The identifier for the object
--     * Slot: title Description: A title for the representation of the object
--     * Slot: description Description: A description of the object
--     * Slot: image Description: File name of an image for the object
--     * Slot: Submission_id Description: Autocreated FK slot
-- # Class: "Kit" Description: ""
--     * Slot: id Description: 
--     * Slot: pmid Description: The PubMed ID for the object
--     * Slot: addgene_url Description: The Addgene URL for the kit
--     * Slot: title Description: A title for the representation of the object
--     * Slot: description Description: A description of the object
-- # Class: "Sequence" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: The name of a thing
--     * Slot: category Description: 
--     * Slot: description Description: A description of the object
--     * Slot: type Description: The type of sequence
--     * Slot: Submission_id Description: Autocreated FK slot
-- # Class: "AddGenePlasmid" Description: ""
--     * Slot: addgene_id Description: The Addgene ID for the plasmid
--     * Slot: resistance Description: 
--     * Slot: well Description: The well where a plasmid is located in a plate
--     * Slot: description Description: A description of the object
--     * Slot: name Description: The name of a thing
--     * Slot: category Description: 
--     * Slot: type Description: The type of sequence
-- # Class: "Submitter" Description: ""
--     * Slot: id Description: 
--     * Slot: full_name Description: The full name of the submitter, will be ignored if the name can be taken from ORCID
--     * Slot: orcid Description: The ORCID of the submitter
--     * Slot: github_username Description: The GitHub username of the submitter
--     * Slot: Submission_id Description: Autocreated FK slot
-- # Class: "Oligo" Description: ""
--     * Slot: name Description: The name of a thing
--     * Slot: id Description: 
--     * Slot: sequence Description: 
--     * Slot: Submission_id Description: Autocreated FK slot
-- # Class: "OligoPair" Description: ""
--     * Slot: forward_oligo Description: 
--     * Slot: reverse_oligo Description: 
--     * Slot: name Description: The name of a thing
--     * Slot: category Description: 
--     * Slot: description Description: A description of the object
--     * Slot: type Description: The type of sequence
-- # Class: "Assembly" Description: ""
--     * Slot: id Description: 
--     * Slot: title Description: A title for the representation of the object
--     * Slot: description Description: A description of the object
--     * Slot: template_file Description: 
--     * Slot: Submission_id Description: Autocreated FK slot
-- # Class: "Submission" Description: ""
--     * Slot: id Description: 
--     * Slot: kit_id Description: 
-- # Class: "Assembly_fragment_order" Description: ""
--     * Slot: Assembly_id Description: Autocreated FK slot
--     * Slot: fragment_order_id Description: 

CREATE TABLE "Kit" (
	id INTEGER NOT NULL, 
	pmid TEXT, 
	addgene_url TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (addgene_url)
);
CREATE TABLE "Submission" (
	id INTEGER NOT NULL, 
	kit_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(kit_id) REFERENCES "Kit" (id)
);
CREATE TABLE "Category" (
	id TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	image TEXT, 
	"Submission_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Submission_id") REFERENCES "Submission" (id)
);
CREATE TABLE "Submitter" (
	id INTEGER NOT NULL, 
	full_name TEXT NOT NULL, 
	orcid TEXT, 
	github_username TEXT, 
	"Submission_id" INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (orcid), 
	UNIQUE (github_username), 
	FOREIGN KEY("Submission_id") REFERENCES "Submission" (id)
);
CREATE TABLE "Oligo" (
	name TEXT NOT NULL, 
	id INTEGER, 
	sequence TEXT NOT NULL, 
	"Submission_id" INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("Submission_id") REFERENCES "Submission" (id)
);
CREATE TABLE "Assembly" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	template_file TEXT, 
	"Submission_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Submission_id") REFERENCES "Submission" (id)
);
CREATE TABLE "Sequence" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	category TEXT NOT NULL, 
	description TEXT, 
	type TEXT, 
	"Submission_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category) REFERENCES "Category" (id), 
	FOREIGN KEY("Submission_id") REFERENCES "Submission" (id)
);
CREATE TABLE "AddGenePlasmid" (
	addgene_id TEXT NOT NULL, 
	resistance TEXT, 
	well TEXT, 
	description TEXT, 
	name TEXT NOT NULL, 
	category TEXT NOT NULL, 
	type TEXT, 
	PRIMARY KEY (addgene_id), 
	UNIQUE (addgene_id), 
	FOREIGN KEY(category) REFERENCES "Category" (id)
);
CREATE TABLE "OligoPair" (
	forward_oligo TEXT NOT NULL, 
	reverse_oligo TEXT NOT NULL, 
	name TEXT NOT NULL, 
	category TEXT NOT NULL, 
	description TEXT, 
	type TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY(forward_oligo) REFERENCES "Oligo" (name), 
	FOREIGN KEY(reverse_oligo) REFERENCES "Oligo" (name), 
	FOREIGN KEY(category) REFERENCES "Category" (id)
);
CREATE TABLE "Assembly_fragment_order" (
	"Assembly_id" INTEGER, 
	fragment_order_id TEXT, 
	PRIMARY KEY ("Assembly_id", fragment_order_id), 
	FOREIGN KEY("Assembly_id") REFERENCES "Assembly" (id), 
	FOREIGN KEY(fragment_order_id) REFERENCES "Category" (id)
);