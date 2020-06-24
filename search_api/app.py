from typing import Dict
from elasticsearch import Elasticsearch
from flask import Flask

app = Flask(__name__)
es = Elasticsearch(["http://elastic:changeme@localhost:9200/",])


@app.route("/")
def index():
    return {
        "thing": "value",
    }

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return job_title_search(query)

def job_title_search(job_title: str) -> Dict:
    query_body = {"query": {"match": {"job_title": job_title}}}
    res = es.search(index="jobs", body=query_body)
    return res


print(job_title_search("engineer"))
