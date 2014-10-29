/**
 * Created by bliang on 10/29/14.
 */

function replaceQueryString(url, param, value) {
    /* Replaces value of query string in URL with provided new value.
     Will append to URL if no matching query string is found.

     Args:
     url - current/old URL
     param - query string key
     value - new value to assign to query string */
    var re = new RegExp("([?|&])" + param + "=.*?(&|$)", "i");
    if (url.match(re)) {
        return url.replace(re, '$1' + param + "=" + value + '$2');
    }
    else if (url.search(/\?/) > 0) {
        return url + '&' + param + "=" + value;
    }
    else {
        return url + '?' + param + "=" + value;
    }
}

function removeAllQueryStrings(url, param, value) {
    /* Recursively removes all query strings found in URL matching param and value
       strings.

     Args:
     url - current/old URL
     param - query string key
     value - value substring to match */
    var re1 = new RegExp("[?|&]" + param + "=" + value + ".*?(?=&)", "i");
    var re2 = new RegExp("[?|&]" + param + "=" + value + ".*?(?=$)", "i");
    var new_url = '';
    if (url.match(re1)) {
        new_url = url.replace(re1, '');
        return removeAllQueryStrings(new_url, param, value);
    } else if (url.match(re2)) {
        new_url = url.replace(re2, '');
        return removeAllQueryStrings(new_url, param, value);
    } else {
        return url;
    }
}

function getQSValue(url, query_string) {
    /* Returns value of given query string in current URL */
    var qs_re = new RegExp(query_string + '=(.*?)(?:&|$)');
    if (url.match(qs_re)) {
        return url.match(qs_re)[1];
    }
    return null;
}

