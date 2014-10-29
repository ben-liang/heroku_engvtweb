/**
 * Created by bliang on 10/29/14.
 */

function getQSValue(url, query_string) {
    /* Returns value of given query string in current URL */
    var qs_re = new RegExp(query_string + '=(.*?)(?:&|$)');
    if (url.match(qs_re)) {
        return url.match(qs_re)[1];
    }
    return null;
}

