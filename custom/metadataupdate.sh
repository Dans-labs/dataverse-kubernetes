#!/bin/bash

# Bash script to read all files with custom metadata blocks from the remote github repository and import to Dataverse
CUSTOM=`/usr/bin/python $HOME_DIR/metadatareader.py`
old=$IFS
IFS=' '
for DIR in $CUSTOM ;
        do echo $DIR ;
        data=$(curl -s $DIR --output /tmp/data.tsv)
        curl -X POST http://${DATAVERSE_SERVICE_HOST}:${DATAVERSE_SERVICE_PORT_HTTP}/api/admin/datasetfield/load -X POST --data-binary @/tmp/data.tsv -H "Content-type: text/tab-separated-values"
done
IFS=$old
