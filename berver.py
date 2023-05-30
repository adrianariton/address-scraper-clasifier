from flask import Flask
from flask import request
from extract2 import run
from ner import recognize_m
# from extract2 import recognize_addresses
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

def format(address_array, header=""):
    i = 0
    yield header
    for a in address_array:
        yield f"""<h1>#{i}</h1><ul>"""
        for x in a:
            yield f"""
                <li>{x}</li>
            """
        i += 1
        yield "</ul>"

@app.route("/") 
def home():
    '''
        Max urls is the number of urls to be sampled
    '''
    addresses, failed, empty = run(max_urls=50)
    print(addresses)
    head = f"<span>Failed: {failed} | Empty: {empty}</span>"
    
    with open("output/NER_REC.txt", "w") as f:
        i = 0
        for site_adrss in addresses:
            i += 1
            print(f"\n--#{i}", file=f)
            data = recognize_m(site_adrss)
            for el in data:
                el = [x for x in el if x[1] != "STATE_FULL"]
                print(el, file=f)
    
    with open("output/intermediary.txt", "w") as f:
        print(addresses, file=f)
    
    print("\n\n\n")
    
    return format(addresses, header=head)

@app.route("/me")
def me():
    return "<h1>helo</h1>"

@app.route("/aa")
def aa():
    return "<h1>aa</h1>"