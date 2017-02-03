placetypes:
	./utils/mk-spec.py -l www/include/lib_whosonfirst_placetypes_spec.php -r https://raw.githubusercontent.com/whosonfirst/whosonfirst-placetypes/master/data/placetypes-spec-latest.json -k whosonfirst_placetypes

sources:
	./utils/mk-spec.py -l www/include/lib_whosonfirst_sources_spec.php -r https://raw.githubusercontent.com/whosonfirst/whosonfirst-sources/master/data/sources-spec-latest.json -k whosonfirst_sources

spec: placetypes sources
