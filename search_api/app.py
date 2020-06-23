from typing import Dict
from elasticsearch import Elasticsearch

es = Elasticsearch(["http://elastic:changeme@localhost:9200/",])


# res = es.search(index="jobs")

# print(type(res))


def job_title_search(job_title: str) -> Dict:
    query_body = {"query": {"match": {"job_title": job_title}}}
    res = es.search(index="jobs", body=query_body)
    return res


print(job_title_search("engineer"))
