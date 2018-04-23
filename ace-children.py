import sys
import traceback
import urllib, urllib2
import json

def query(q,epr,f='application/json'):
    try:
        params = {'query': q}
        params = urllib.urlencode(params)
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(epr+'?'+params)
        request.add_header('Accept', f)
        request.get_method = lambda: 'GET'
        url = opener.open(request)
        return url.read()
    except:
        e = sys.exc_info()[0]
        traceback.print_exc(file=sys.stdout)
        raise e

def main():
    argc = len(sys.argv)

    if argc == 1:
        print( "Error: no keyword given.")
        exit(0)

    keyword = sys.argv[1]

    myquery = """
        PREFIX w3t: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT DISTINCT ?y
        WHERE {
         {?y w3t:type umbel-rc:""" + keyword + """}
         UNION
         {?y w3t:type dbo:""" + keyword + """}
         UNION
         {?y w3t:type yago:""" + keyword + """}
         UNION
         {?y w3t:type dbr:""" + keyword + """}
         UNION
         {dbr:""" + keyword + """ dbo:class ?y}
        }

        """

    json_obj = query(myquery,"http://dbpedia.org/sparql")

    # work json magic then print the results
    json_data = json.loads(json_obj)
    results = json_data['results']
    results_data = results['bindings']
    for i in range(len(results_data)):
        current_index = results_data[i]
        current_obj = current_index['y']
        obj_type = current_obj['value']
        print '\t' + obj_type

    exit(0)



if __name__ == "__main__":
    main()
