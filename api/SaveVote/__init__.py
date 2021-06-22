import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    from azure.data.tables import TableClient
    import os

    connection_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')

    body = req.get_json()

    with TableClient.from_connection_string(connection_string, 'votes') as table_client:

        entity = {
            u'PartitionKey': u"city",
            u'RowKey': body['city']
        }

        try:
            existing = table_client.get_entity(entity['PartitionKey'], entity['RowKey'])

            existing["votes"] = existing["votes"] + 1

            table_client.upsert_entity(entity = existing)

            return "True"
        except:
            try:
                entity['votes'] = 1
                
                table_client.upsert_entity(entity = entity)

                return "True"

            except Exception as err:

                return str(err)






