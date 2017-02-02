placetypes:
	./utils/mk-spec.py -l www/include/lib_whosonfirst_placetypes_spec.php -r https://raw.githubusercontent.com/whosonfirst/whosonfirst-sources/master/data/sources-spec-latest.json -k whosonfirst_placetypes

spec: placetypes
