If you have questions, suggestions, complaints or need any help with dexy,
please email <info@dexy.it>.

Documentation is in [The Dexy Guide](/guide). For help installing dexy, see the
[installation guide](/guide/installing-dexy.html) section of the Dexy Guide.

A reference guide to the filters available in dexy is [here](/filters).

A list of currently open issues ([maintained with t](https://bitbucket.org/sjl/t/src#t))
is [here](https://github.com/ananelson/dexy/blob/develop/bugs). You can submit
a pull request to that file but email is preferred.

The old issue and bug trackers will be closed down as they are emptied, please
use email for all new issues.

This custom search helps you search dexy-related sites:

<div id="cse" style="width: 100%;">Loading</div>
<script src="//www.google.com/jsapi" type="text/javascript"></script>
<script type="text/javascript"> 
    function parseQueryFromUrl () {
        var queryParamName = "q";
        var search = window.location.search.substr(1);
        var parts = search.split('&');
        for (var i = 0; i < parts.length; i++) {
            var keyvaluepair = parts[i].split('=');
            if (decodeURIComponent(keyvaluepair[0]) == queryParamName) {
                return decodeURIComponent(keyvaluepair[1].replace(/\+/g, ' '));
            }
        }
        return '';
    }
google.load('search', '1', {language : 'en', style : google.loader.themes.MINIMALIST});
google.setOnLoadCallback(function() {
        var customSearchControl = new google.search.CustomSearchControl('015653941277163542830:bql9gpcr5om');
        customSearchControl.setResultSetSize(google.search.Search.FILTERED_CSE_RESULTSET);
        customSearchControl.draw('cse');
        var queryFromUrl = parseQueryFromUrl();
        if (queryFromUrl) {
        customSearchControl.execute(queryFromUrl);
        }
        }, true);
</script>
