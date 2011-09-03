-- P31A. HOUSEHOLD TYPE BY RELATIONSHIP FOR THE POPULATION UNDER 18 YEARS (WHITE ALONE)
-- designed to work with the IRE Census bulk data exports
-- see http://census.ire.org/data/bulkdata.html
CREATE TABLE ire_p31a (
	geoid VARCHAR(11) NOT NULL, 
	sumlev VARCHAR(3) NOT NULL, 
	state VARCHAR(2) NOT NULL, 
	county VARCHAR(3), 
	cbsa VARCHAR(5), 
	csa VARCHAR(3), 
	necta VARCHAR(5), 
	cnecta VARCHAR(3), 
	name VARCHAR(90) NOT NULL, 
	pop100 INTEGER NOT NULL, 
	hu100 INTEGER NOT NULL, 
	pop100_2000 INTEGER, 
	hu100_2000 INTEGER, 
	p031a001 INTEGER, 
	p031a001_2000 INTEGER, 
	p031a002 INTEGER, 
	p031a002_2000 INTEGER, 
	p031a003 INTEGER, 
	p031a003_2000 INTEGER, 
	p031a004 INTEGER, 
	p031a004_2000 INTEGER, 
	p031a005 INTEGER, 
	p031a005_2000 INTEGER, 
	p031a006 INTEGER, 
	p031a006_2000 INTEGER, 
	p031a007 INTEGER, 
	p031a007_2000 INTEGER, 
	p031a008 INTEGER, 
	p031a008_2000 INTEGER, 
	p031a009 INTEGER, 
	p031a009_2000 INTEGER, 
	p031a010 INTEGER, 
	p031a010_2000 INTEGER, 
	p031a011 INTEGER, 
	p031a011_2000 INTEGER, 
	p031a012 INTEGER, 
	p031a012_2000 INTEGER, 
	p031a013 INTEGER, 
	p031a013_2000 INTEGER, 
	p031a014 INTEGER, 
	p031a014_2000 INTEGER, 
	p031a015 INTEGER, 
	p031a015_2000 INTEGER, 
	p031a016 INTEGER, 
	p031a016_2000 INTEGER, 
	PRIMARY KEY (geoid)
);