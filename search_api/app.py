from typing import Dict
from elasticsearch import Elasticsearch
from flask import Flask, request, render_template

app = Flask(__name__)
es = Elasticsearch(["http://elastic:changeme@localhost:9200/",])


@app.route("/")
def index():
    return render_template("index.html", fields=meta("active_jobs_full"))

@app.route("/search")
def search():
    query = request.args.get("q", "")
    fields = request.args.get("fields", "").split(",")
    return job_title_search(query, fields)

@app.route("/meta/{index}")
def meta(index):
    mapping = es.indices.get_mapping(index)
    return mapping[index]["mappings"]["properties"]

def job_title_search(query, fields):
    query_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields
                }
        }
    }
    res = es.search(index="active_jobs_full", body=query_body)
    return res

if __name__ == "__main__":
    app.run(debug=True)
