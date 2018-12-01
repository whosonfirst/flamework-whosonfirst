placetypes:
	./utils/mk-spec.py -l www/include/lib_whosonfirst_placetypes_spec.php -r https://raw.githubusercontent.com/whosonfirst/whosonfirst-placetypes/master/data/placetypes-spec-latest.json -k whosonfirst_placetypes

sources:
	python ./utils/mk-spec.py -l www/include/lib_whosonfirst_sources_spec.php -r https://raw.githubusercontent.com/whosonfirst/whosonfirst-sources/master/data/sources-spec-latest.json -k whosonfirst_sources

brands:
	./utils/mk-spec.py -l www/include/lib_whosonfirst_brands_sizes_spec.php -r https://raw.githubusercontent.com/whosonfirst/whosonfirst-brands-sizes/master/data/brands-sizes-spec-latest.json -k whosonfirst_brands_sizes

spec: placetypes sources brands
