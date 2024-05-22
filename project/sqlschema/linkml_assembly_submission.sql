-- # Class: "Category" Description: ""
--     * Slot: id Description: The identifier for the object
--     * Slot: title Description: A title for the representation of the object
--     * Slot: description Description: A description of the object
--     * Slot: image Description: Path to an image of the object
-- # Class: "Kit" Description: ""
--     * Slot: pmid Description: The PubMed ID for the object
--     * Slot: addgene_url Description: The Addgene URL for the object
-- # Class: "Sequence" Description: ""
--     * Slot: plasmid_name Description: 
--     * Slot: addgene_id Description: 
--     * Slot: category Description: 
--     * Slot: resistance Description: 
--     * Slot: well Description: The well where a plasmid is located in a plate
--     * Slot: description Description: A description of the object
-- # Class: "Submitter" Description: ""
--     * Slot: id Description: 
--     * Slot: full_name Description: The full name of the submitter, will be ignored if the name can be taken from ORCID
--     * Slot: orcid Description: The ORCID of the submitter
--     * Slot: github_username Description: The GitHub username of the submitter

CREATE TABLE "Category" (
	id TEXT NOT NULL, 
	title TEXT, 
	description TEXT, 
	image TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Kit" (
	pmid TEXT NOT NULL, 
	addgene_url TEXT, 
	PRIMARY KEY (pmid), 
	UNIQUE (addgene_url)
);
CREATE TABLE "Submitter" (
	id INTEGER NOT NULL, 
	full_name TEXT, 
	orcid TEXT, 
	github_username TEXT, 
	PRIMARY KEY (id), 
	UNIQUE (orcid), 
	UNIQUE (github_username)
);
CREATE TABLE "Sequence" (
	plasmid_name TEXT, 
	addgene_id INTEGER NOT NULL, 
	category TEXT, 
	resistance TEXT, 
	well TEXT, 
	description TEXT, 
	PRIMARY KEY (addgene_id), 
	UNIQUE (addgene_id), 
	FOREIGN KEY(category) REFERENCES "Category" (id)
);