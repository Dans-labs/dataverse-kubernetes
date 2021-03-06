# Dataverse Metadata Blocks

This is about handling upstream changes to "system" metadata blocks and
how to handle custom metadata block support.

See also: [Upstream documentation about customizing metadata](http://guides.dataverse.org/en/latest/admin/metadatacustomization.html)

## Add custom metadata blocks
Please put any metadata TSV files to the `/metadata` directory of the jobs
container below.

This can happen via
* custom/derived images
* volume mounts
* `ConfigMap` files
* sidecar container(s), downloading/cloning/checking out/...

`ConfigMap`s seem to be the easiest option, but in case you use a large amount
of custom metadata blocks, you might want to use another method.

## Update Dataverse metadata blocks
Simply deploy a metadata update job:
```
kubectl create -f k8s/dataverse/jobs/metadata-update.yaml
```
Remember: you will need to get your custom metadata inside that job somehow, see above.

### Force re-export of citation metadata after update
Especially when the core `citation.tsv` metadata schema changed, you will need
to re-export all citation metadata. A simple job does the trick:
```
kubectl create -f k8s/dataverse/jobs/metadata-reexport.yaml
```
Having a large set of published dataverses and datasets, you might want to run
this during off-hours.

See also: [upstream docs](http://guides.dataverse.org/en/latest/admin/metadataexport.html).

## Update Solr Search Index

> TODO for release 4.17 containing necessary scripts.
