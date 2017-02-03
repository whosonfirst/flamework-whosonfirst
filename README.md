# flamework-whosonfirst

Who's On First specific things for Flamework-derived projects

## Important

This is "wet paint". Please dress accordingly.

## Example

In your project's `Makefile` you might include something like this:

```
whosonfirst:
	curl -s -o www/include/lib_whosonfirst_placetypes.php https://raw.githubusercontent.com/whosonfirst/flamework-whosonfirst/master/www/include/lib_whosonfirst_placetypes.php
	curl -s -o www/include/lib_whosonfirst_placetypes_spec.php https://raw.githubusercontent.com/whosonfirst/flamework-whosonfirst/master/www/include/lib_whosonfirst_placetypes_spec.php
	curl -s -o www/include/lib_whosonfirst_sources.php https://raw.githubusercontent.com/whosonfirst/flamework-whosonfirst/master/www/include/lib_whosonfirst_sources.php
	curl -s -o www/include/lib_whosonfirst_sources_spec.php https://raw.githubusercontent.com/whosonfirst/flamework-whosonfirst/master/www/include/lib_whosonfirst_sources_spec.php
	curl -s -o www/include/lib_whosonfirst_uri.php https://raw.githubusercontent.com/whosonfirst/flamework-whosonfirst/master/www/include/lib_whosonfirst_uri.php
```
