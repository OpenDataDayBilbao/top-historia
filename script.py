import requests
import json
import csv
query='''select distinct str(?label) AS ?name ?lat ?lon str(?desc) AS ?description ?date str(?casualties) AS ?causalties  where {
?s rdf:type <http://schema.org/Event> .
{
?s dcterms:subject <http://dbpedia.org/resource/Category:Battles_of_World_War_I_involving_Serbia> .
} UNION {
?s dcterms:subject <http://dbpedia.org/resource/Category:Battles_of_World_War_I_involving_Austria-Hungary> .
} UNION {
?s dcterms:subject <http://dbpedia.org/resource/Category:Battles_of_World_War_I_involving_France> .
} UNION {
?s dcterms:subject <http://dbpedia.org/resource/Category:Battles_of_World_War_I_involving_Germany> .
}
?s rdfs:label ?label .
?s geo:lat ?lat .
?s geo:long ?lon .
?s rdfs:comment ?desc .
?s dbpedia-owl:date ?date .
OPTIONAL {?s dbpedia-owl:causalties ?casualties} .
FILTER (LANG(?label)='en' && LANG(?desc)='en')}'''

battles=json.loads(r.text)

with open('battles.csv','wb') as fp:
	file_writer = csv.writer(fp)
	file_writer.writerow(['Title','Start','End','Description','Web Page','Media','Media Caption','Media Credit','Tags','Place','Location','Source','Source URL'])
	for battle in battles['results']['bindings']:
		title=battle['name']['value']
		lat=battle['lat']['value']
		lon=battle['lon']['value']
		description=battle['description']['value']
		date=battle['date']['value']
		casualties=''
		if 'causalties' in battle.keys():
			casualties=battle['causalties']['value']
		file_writer.writerow([title.encode('utf-8'),date.encode('utf-8'),'',description.encode('utf-8'),'','','','','','','%s,%s'%(lat,lon),'',''])

