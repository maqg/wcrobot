/**
 * Created by henry on 2017/6/2.
 */

function getKeyword() {
    return $("#queryKeyword").val();
}

function doQuery() {
    var keyword = getKeyword();
    updateRobotList(keyword);
}

function updateRobotList(keyword) {

    json = {
        "api": "octlink.wcrobot.v1.robot.APIShowAllRobot",
        "paras": {
            "timeout": 0,
            "accountId": "",
            "sName": keyword
        },
        "session": {
            "uuid": "00000000000000000000000000000000",
            "skey": "00000000000000000000000000000000"
        },
        "async": false
    };

    bodyStr = JSON.stringify(json);

    httpPost("/api/", bodyStr, function (resJson) {

        retData = parseResponse(resJson);
        if (retData === null) {
            return;
        }

        updateFileTable(retData["robots"]);
    });
}

function createHeader() {

    bodyStr = "<tr><th>别名</th>";
    bodyStr += "<th>用户名</th>";
    bodyStr += "<th>成员数量</th>";
    bodyStr += "<th>操作</th></tr>";

    return $(bodyStr);
}

function raiseDetail(robot) {

    $detailBody = $("#modalDetailBody");

    if ($detailBody !== null) {

        var bodyStr = "";

        bodyStr += "<table class=\"table table-striped table-hover\">";
        bodyStr += "<tr><th>属性</th><th>内容</th></tr>";

        bodyStr += "<tr><td>ID</td><td>" + robot["id"] + "</td></tr>";
        bodyStr += "<tr><td>别名</td><td>" + robot["name"] + "</td></tr>";
        bodyStr += "<tr><td>用户名</td><td>" + robot["uId"] + "</td></tr>";
        bodyStr += "<tr><td>组员数量</td><td>" + robot["lastLogin"] + "</td></tr>";

        $detailBody.html(bodyStr);

        // to modify lable
        $lable = $("#modalDetailTitle");
        if ($lable !== null) {
            $lable.html("联系人详情-" + robot["name"]);
        }

        $("#modalDetail").modal("show");
    } else {
        updateErrorPrompt("error", "获取详细页面错误！");
    }
}

function printrobot(dataObj) {

    bodyStr = "<tr><td>" + dataObj["name"] + "</td>";
    bodyStr += "<td>" + dataObj["uName"] + "</td>";
    bodyStr += "<td>" + dataObj["uId"] + "</td>";
    bodyStr += "<td>" + dataObj["messages"] + "</td>";
    bodyStr += "<td>" + dataObj["lastLogin"] + "</td><td>";

    bodyStr += "<div class=\"robotbutton\" onclick=\"robotqc('" + dataObj["id"] + "');\" style=\"margin-right: 10px\" title='查看'><img src='/ng/static/imgs/button_qrcode.png'></div>";

    $tr = $(bodyStr);

    $tr.dblclick(function () {
        raiseDetail(dataObj);
    });

    return $tr;
}

function updateFileTable(fileList) {

    $fileTable = $("#fileListContent");

    $fileTable.html("");
    $fileTable.append(createHeader());

    for (var i = 0; i < fileList.length; i++) {
        dataObj = fileList[i];
        G_ROBOTS[dataObj["id"]] = dataObj;
        $tr = printrobot(dataObj);
        $fileTable.append($tr);
    }
}