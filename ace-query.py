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
    if len(sys.argv) == 1:
        print( "Error: no keyword given.")
        exit(0)

    keyword = sys.argv[1]

    myquery = """
        PREFIX w3t: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
        SELECT ?y
        WHERE {
         dbr:""" + keyword + """ w3t:type ?y.
        }
        """    
    
    # we want to extract the type of the keyword from the returned json string
    #ex - http://www.w3.org/1999/02/22-rdf-syntax-ns#type
    json_obj =  query(myquery,"http://dbpedia.org/sparql")
    json_data = json.loads(json_obj)
    results = json_data['results']
    results_data = results['bindings']

    if len(results_data) == 0:
        print keyword + ' has no type attribute'
    else:
        print keyword + ' has the following type attributes:'
    for i in range(len(results_data)):
        current_index = results_data[i]
        current_obj = current_index['y']
        obj_type = current_obj['value']
        print '\t' + obj_type


    # --------------------------------------------------------------------------
    # now get the subject lines that the keyword falls under
    # --------------------------------------------------------------------------    
    myquery = """
       PREFIX purl: <http://purl.org/dc/terms/>        
       SELECT ?y
       WHERE {
        dbr:""" + keyword + """ purl:subject ?y.
       }
       """    
    
    # we want to extract the type of the keyword from the returned json string
    #ex - http://www.w3.org/1999/02/22-rdf-syntax-ns#type
    json_obj =  query(myquery,"http://dbpedia.org/sparql")
    json_data = json.loads(json_obj)
    results = json_data['results']
    results_data = results['bindings']

    if len(results_data) == 0:
        print keyword + ' has no subject attribute'
    else:
        print keyword + ' has the following subject attributes:'
    for i in range(len(results_data)):
        current_index = results_data[i]
        current_obj = current_index['y']
        obj_type = current_obj['value']
        print '\t' + obj_type



if __name__ == "__main__":
    main()
