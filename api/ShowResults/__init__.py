import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    from azure.data.tables import TableClient
    import os

    connection_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')

    with TableClient.from_connection_string(connection_string, 'votes') as table_client:

        try:
            entities = table_client.list_entities()

            total = 0
            partials = []

            for entity in entities:
                total += entity['votes']
                partials.push({
                    'city': entity['city']
                    'votes': entity['votes']
                })

            return str(partials)

        except:
            pass
