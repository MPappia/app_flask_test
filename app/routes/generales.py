from ..app import app
from flask import render_template


@app.route("/")
def accueil():
    return render_template("/home.html")

#REV-2
@app.route("/division/<int:numerateur>/<int:denominateur>", methods=['GET'])
def division(numerateur, denominateur) : 
    resultat = numerateur/denominateur
    return str(resultat)

#REV-3
@app.route("/parcs_eoliens")
def parcs_eoliens():
    données_json=[
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"5800903acd0e5e4975490ae016641ed745aa6705",
      "fields":{
         "nom_reg":"Pays de la Loire",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200071678,
         "nom_dept":"Maine-et-Loire",
         "count":1,
         "dep":"49",
         "date_des_donnees":"2019-12",
         "coordonnees":[
            47.0185766256,
            -0.768134737511
         ],
         "f_commune_pdl":"Maul\u00e9vrier",
         "libepci":"CA du Choletais",
         "reg":52,
         "f_code_insee_pdl":"49192"
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -0.768134737511,
            47.0185766256
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"047d6e3bfdc66903731f2cd6c87bb7bc9a09e467",
      "fields":{
         "nom_reg":"Occitanie",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":243200458,
         "nom_dept":"Gers",
         "count":1,
         "dep":"32",
         "date_des_donnees":"2019-12",
         "coordonnees":[
            43.8431026932,
            -0.129777631526
         ],
         "f_commune_pdl":"Maupas",
         "libepci":"CC du Grand Armagnac",
         "reg":76,
         "f_code_insee_pdl":"32246"
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -0.129777631526,
            43.8431026932
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"e9094eed2ade4e614bd5646187eac5f0114fe662",
      "fields":{
         "dep":"35",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":6000.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Maxent",
         "libepci":"CC de Broc\u00e9liande",
         "reg":53,
         "f_code_insee_pdl":"35169",
         "nom_reg":"Bretagne",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":243500618,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Ille-et-Vilaine",
         "count":1,
         "coordonnees":[
            47.9788328525,
            -2.01519596065
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -2.01519596065,
            47.9788328525
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"414d71d325d408e54e47ef40a8c4bdb899a33546",
      "fields":{
         "dep":"02",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":27500.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Mayot",
         "libepci":"CA Chauny-Tergnier-La F\u00e8re",
         "reg":32,
         "f_code_insee_pdl":"02473",
         "nom_reg":"Hauts-de-France",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200071785,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Aisne",
         "count":2,
         "coordonnees":[
            49.7090117255,
            3.39804766077
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            3.39804766077,
            49.7090117255
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"da80e3928ddd562c377db15a35dc766b3c9baf4b",
      "fields":{
         "dep":"17",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":12000.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Mazeray",
         "libepci":"CC des Vals de Saintonge Communaut\u00e9",
         "reg":75,
         "f_code_insee_pdl":"17226",
         "nom_reg":"Nouvelle-Aquitaine",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200041689,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Charente-Maritime",
         "count":1,
         "coordonnees":[
            45.9158199464,
            -0.559708232455
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -0.559708232455,
            45.9158199464
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"1cd3aa116a0a5ad965ddb1643870a59ceebc92b9",
      "fields":{
         "nom_reg":"Nouvelle-Aquitaine",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200072049,
         "nom_dept":"Charente",
         "count":1,
         "dep":"16",
         "date_des_donnees":"2019-12",
         "coordonnees":[
            45.740251316,
            0.520413334007
         ],
         "f_commune_pdl":"Mazerolles",
         "libepci":"CC de Charente Limousine",
         "reg":75,
         "f_code_insee_pdl":"16213"
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            0.520413334007,
            45.740251316
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"3d94a15ca65fd95d9ca560d94ad5ef4cb3ba7170",
      "fields":{
         "dep":"22",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":5600.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Ma\u00ebl-Pestivien",
         "libepci":"CA Guingamp-Paimpol Agglom\u00e9ration de l'Armor \u00e0 l'Argoat",
         "reg":53,
         "f_code_insee_pdl":"22138",
         "nom_reg":"Bretagne",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200067981,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"C\u00f4tes-d'Armor",
         "count":1,
         "coordonnees":[
            48.4041439455,
            -3.29047753101
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -3.29047753101,
            48.4041439455
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"8f61987355f96fbe25fe7e3e117b285703ed13b8",
      "fields":{
         "dep":"29",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":6000.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Melgven",
         "libepci":"CA Concarneau Cornouaille Agglom\u00e9ration",
         "reg":53,
         "f_code_insee_pdl":"29146",
         "nom_reg":"Bretagne",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":242900769,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Finist\u00e8re",
         "count":1,
         "coordonnees":[
            47.9129471121,
            -3.84206992486
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -3.84206992486,
            47.9129471121
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"08252ebfc2e016ef8aeaf69f09d0d916fbda09e2",
      "fields":{
         "dep":"79",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":47400.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Melle",
         "libepci":"CC Mellois-en-Poitou",
         "reg":75,
         "f_code_insee_pdl":"79174",
         "nom_reg":"Nouvelle-Aquitaine",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200069755,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Deux-S\u00e8vres",
         "count":4,
         "coordonnees":[
            46.2309583731,
            -0.147888712984
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -0.147888712984,
            46.2309583731
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"85f7ceb826105b0c22200694a9218a5ba36d3630",
      "fields":{
         "nom_reg":"Bretagne",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200067460,
         "nom_dept":"C\u00f4tes-d'Armor",
         "count":2,
         "dep":"22",
         "date_des_donnees":"2019-12",
         "coordonnees":[
            48.1936252026,
            -2.39598361343
         ],
         "f_commune_pdl":"Merdrignac",
         "libepci":"CC Loud\u00e9ac Communaut\u00e9 - Bretagne Centre",
         "reg":53,
         "f_code_insee_pdl":"22147"
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -2.39598361343,
            48.1936252026
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"621ef11cfb403ed67055fcb2d40beed1bf93a475",
      "fields":{
         "dep":"10",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":12000.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Mergey",
         "libepci":"CA Troyes Champagne M\u00e9tropole",
         "reg":44,
         "f_code_insee_pdl":"10230",
         "nom_reg":"Grand Est",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200069250,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Aube",
         "count":1,
         "coordonnees":[
            48.395565383,
            4.03305791455
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            4.03305791455,
            48.395565383
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"0324e6629300a07a68475d27c8e187c2afe65433",
      "fields":{
         "dep":"57",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":10000.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Merten",
         "libepci":"CC Houve-Pays Boulageois",
         "reg":44,
         "f_code_insee_pdl":"57460",
         "nom_reg":"Grand Est",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200067650,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Moselle",
         "count":1,
         "coordonnees":[
            49.2468555754,
            6.66349016101
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            6.66349016101,
            49.2468555754
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"cff9a6567537b59456fa7ef61de680d4c0694072",
      "fields":{
         "dep":"27",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":10000.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Mesnils-sur-Iton",
         "libepci":"CC Interco Normandie Sud Eure",
         "reg":28,
         "f_code_insee_pdl":"27198",
         "nom_reg":"Normandie",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200066462,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Eure",
         "count":1,
         "coordonnees":[
            48.8643668138,
            1.08042048322
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            1.08042048322,
            48.8643668138
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"8e53f2d361a1ddb70e0df27765fc24d758b09872",
      "fields":{
         "nom_reg":"Nouvelle-Aquitaine",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200041523,
         "nom_dept":"Charente-Maritime",
         "count":1,
         "dep":"17",
         "date_des_donnees":"2019-12",
         "coordonnees":[
            45.3464492913,
            -0.313416526888
         ],
         "f_commune_pdl":"Messac",
         "libepci":"CC de la Haute-Saintonge",
         "reg":75,
         "f_code_insee_pdl":"17231"
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            -0.313416526888,
            45.3464492913
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"a3d775290aa2f2aa3d5cabe1ffb6cea00ce783e6",
      "fields":{
         "nom_reg":"Nouvelle-Aquitaine",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200069854,
         "nom_dept":"Vienne",
         "count":1,
         "dep":"86",
         "date_des_donnees":"2019-12",
         "coordonnees":[
            46.5483807431,
            0.415961339413
         ],
         "f_commune_pdl":"Mignaloux-Beauvoir",
         "libepci":"CU du Grand Poitiers",
         "reg":75,
         "f_code_insee_pdl":"86157"
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            0.415961339413,
            46.5483807431
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   },
   {
      "datasetid":"installations-de-production-eolien-par-commune",
      "recordid":"239cfcbf0a9bf25eae193aff66f3e7cb18be31e5",
      "fields":{
         "dep":"89",
         "sum_3_prod_e_kw_puissance_de_raccordement_injection":10250.0,
         "date_des_donnees":"2019-12",
         "f_commune_pdl":"Mig\u00e9",
         "libepci":"CC de Puisaye-Forterre",
         "reg":27,
         "f_code_insee_pdl":"89256",
         "nom_reg":"Bourgogne-Franche-Comt\u00e9",
         "s_3_prod_d_filiere":"\u00c9olien",
         "code_epci":200067130,
         "s_3_prod_i_regime_d_exploitation":"Realised",
         "nom_dept":"Yonne",
         "count":1,
         "coordonnees":[
            47.676526095,
            3.53286271854
         ]
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            3.53286271854,
            47.676526095
         ]
      },
      "record_timestamp":"2021-09-29T14:09:49.445+02:00"
   }
]
    return render_template('parcs_eoliens.html', données_json=données_json)

# Retour cours
@app.route("/pays/<string:nom>")
def pays(nom):
    return render_template("pages/pays.html", pays=nom)