# super-simple-quizz

This application was written to showcase the Azure Static Webapps service. 

It's cleaned up so it can be forked and tested on your own subscription.

## Requirements

You'll need an Azure Storage account with a table named `votes`.

## Running locally

You'll need python3 and Azure Functions cli for the API.

```bash
export AZURE_STORAGE_CONNECTION_STRING="..."
```

Once into the /api folder, install the dependencies

```bash
pip3 install -r requirements.txt
```

And start the functions

```bash
func start
```

For the site, into the /site folder, you can just open the index.html file into your favorite browser

You'll also want to change the `main.js` file to set up the full URL APIs for localhost, since it's ready to be used within an Azure Static Webapp

## Static webapps

Create an Azure Static Webapp service into your subscription and choose the repository you have this code. Choose a custom template abd set the `api` box to `/api` and the `site` box to `/site`.

Also, after the deployment you'll have to add an app setting named `AZURE_STORAGE_CONNECTION_STRING` with the connection string for your storage account.

Sorry for keeping it too manual :D
