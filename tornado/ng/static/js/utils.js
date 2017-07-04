
function getSelectedOption(id) {
    return $(id + " option:selected").val();
}

function string2Json($textString) {

    var $jsonObj;

    if ($textString == null) {
        return null;
    }

    try {
        $jsonObj = JSON.parse($textString);
    } catch (e) {
        alert("got bad json string");
        return null;
    }

    return $jsonObj;
}

function updateErrorPrompt(type, msg) {

    $errorPrompt = $("#errorPrompt");

    strBody = "<div class=\"alert alert-" + type + "\">" + msg + "</div>";

    $errorPrompt.html(strBody);
}

function parseResponse(jsonObj) {
    if (jsonObj == null) {
        updateErrorPrompt("error", "got null response");
        return null;
    }

    errorObj = jsonObj["errorObj"];
    if (errorObj == null) {
        updateErrorPrompt("error", "got null error response");
        return null;
    }

    if (errorObj["errorNo"] != 0) {
        updateErrorPrompt("error", errorObj["errorMsg"]);
        return null;
    }

    updateErrorPrompt("success", "Command successful");

    return jsonObj["data"];
}



function httpPost($url, $data, $callback) {

    var http;

    try {
        http = new XMLHttpRequest();
    } catch (e) {
        try {
            http = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                http = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                alert("您的浏览器不支持AJAX！");
                return false;
            }
        }
    }

    http.onreadystatechange = function()
    {
        if (http.readyState == 4 && http.status == 200) {
            $callback(string2Json(http.responseText));
        } else if (http.readyState == 4 && http.status != 200) {
            alert("编辑API错误！")
        }
    };


    http.open("POST", $url, true);
    http.setRequestHeader("Content-Type", "application/json");
    http.send($data);
}

function getFileSize(bytes) {
    G = 1024 * 1024 * 1024;
    M = 1024 * 1024;
    K = 1024;

    if (bytes >= G) {
        return (bytes / G).toFixed(2) + " G";
    }

    if (bytes >= M) {
        return (bytes / M).toFixed(2) + " M";
    }

    return (bytes / K).toFixed(2) + " K";
}


function funcNotFound(imageId) {
    alert("function not found");
}