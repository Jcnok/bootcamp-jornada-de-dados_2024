import time

import schedule
from contracts.schema import CompraSchema
from datasource.api import APICollector
from tools.aws.client import S3Client

schema = CompraSchema
aws = S3Client()


def apiCollector(schema, aws, repeat):
    reponse = APICollector(schema, aws).start(repeat)
    print("Executei")
    return reponse


schedule.every(1).minutes.do(apiCollector, schema, aws, 50)


while True:
    schedule.run_pending()
    time.sleep(1)
