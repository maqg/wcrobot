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

    bodyStr = "<tr><th>名称</th>";
    bodyStr += "<th>微信名</th>";
    bodyStr += "<th>微信Id</th>";
    bodyStr += "<th>联系人</th>";
    bodyStr += "<th>群组</th>";
    bodyStr += "<th>消息</th>";
    bodyStr += "<th>状态</th>";
    bodyStr += "<th>上次登录</th>";
    bodyStr += "<th>操作</th></tr>";

    return $(bodyStr);
}

function raiseDetail(robot) {

    $detailBody = $("#modalDetailBody");

    if ($detailBody !== null) {

        var bodyStr = "";

        bodyStr += "<table class=\"table table-striped table-hover\">";
        bodyStr += "<tr><th>属性</th><th>内容</th></tr>";

        if (robot["state"] === 0) {
            bodyStr += "<tr><td>状态</td><td style='color: red;'>" + robot["stateCN"] + "</td></tr>";
        } else if (robot["state"] === 1) {
            bodyStr += "<tr><td>状态</td><td style='color: green;'>" + robot["stateCN"] + "</td></tr>";
        } else {
            bodyStr += "<tr><td>状态</td><td style='color: sandybrown;'>" + robot["stateCN"] + "</td></tr>";
            bodyStr += "<tr><td>二维码</td><td><img src='/config/" + robot["id"] + "/wxqr.png' alt='打开微信扫描'/></td></tr>";
        }
        bodyStr += "<tr><td>ID</td><td>" + robot["id"] + "</td></tr>";
        bodyStr += "<tr><td>名称</td><td>" + robot["name"] + "</td></tr>";
        bodyStr += "<tr><td>微信Id</td><td>" + robot["uId"] + "</td></tr>";
        bodyStr += "<tr><td>微信名称</td><td>" + robot["uName"] + "</td></tr>";
        bodyStr += "<tr><td>创建时间</td><td>" + robot["createTime"] + "</td></tr>";
        bodyStr += "<tr><td>修改时间</td><td>" + robot["lastSync"] + "</td></tr>";
        bodyStr += "<tr><td>上次登录</td><td>" + robot["lastLogin"] + "</td></tr>";


        $detailBody.html(bodyStr);

        // to modify lable
        $lable = $("#modalDetailTitle");
        if ($lable !== null) {
            $lable.html("机器人详情-" + robot["name"]);
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
    bodyStr += "<td>" + dataObj["contacts"] + "</td>";
    bodyStr += "<td>" + dataObj["groups"] + "</td>";
    bodyStr += "<td>" + dataObj["messages"] + "</td>";
    if (dataObj["state"] === 0) {
        bodyStr += "<td style='color: red;'>" + dataObj["stateCN"] + "</td>";
    } else if (dataObj["state"] === 1) {
        bodyStr += "<td style='color: green;'>" + dataObj["stateCN"] + "</td>";
    } else {
        bodyStr += "<td style='color: sandybrown;'>" + dataObj["stateCN"] + "</td>";
    }
    bodyStr += "<td>" + dataObj["lastLogin"] + "</td><td>";

    if (dataObj["state"] === 0) {
        bodyStr += "<button class=\"btn btn-info detail-button\" onclick=\"robotlogin('" + dataObj["id"] + "');\" style=\"margin-right: 10px\">登录</button>";
    } else if (dataObj["state"] === 1) {
        bodyStr += "<button class=\"btn btn-info detail-button\" onclick=\"robotlogout('" + dataObj["id"] + "');\" style=\"margin-right: 10px\">退出</button>";
    } else {
        bodyStr += "<button class=\"btn btn-info detail-button\" onclick=\"robotlogout('" + dataObj["id"] + "');\" style=\"margin-right: 10px\">中止</button>";
    }
    bodyStr += "<button class=\"btn btn-primary detail-button\" onclick=\"robotqc('" + dataObj["id"] + "');\" style=\"margin-right: 10px\">二维码</button>";
    bodyStr += "<button class=\"btn btn-danger detail-button\" onclick=\"removerobot('" + dataObj["id"] + "');\" style=\"margin-right: 10px\" >删除</button></td></tr>";

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

function raiseRemoveModal(robotId, prompt) {

    $("#modalConfirmPrompt").html(prompt);

    $("#modalConfirmCallback").click(function () {
        json = {
            "api": "octlink.wcrobot.v1.robot.APIRemoveRobot",
            "paras": {
                "timeout": 0,
                "id": robotId,
                "mediaType": mediaType
            },
            "session": {
                "uuid": "00000000000000000000000000000000",
                "skey": "00000000000000000000000000000000"
            },
            "async": false
        };

        bodyStr = JSON.stringify(json);

        httpPost("/api/", bodyStr, function (resJson) {
            parseResponse(resJson);
            $("#modalConfirm").modal("hide");
            updateRobotList(getKeyword());
        });
    });

    $("#modalConfirm").modal("show");
}

function removerobot(fileName) {
    raiseRemoveModal(fileName, "您确认删除此机器人吗？");
}

function robotlogin(robotId) {
    json = {
        "api": "octlink.wcrobot.v1.robot.APILogin",
        "paras": {
            "timeout": 0,
            "id": robotId
        },
        "session": {
            "uuid": "00000000000000000000000000000000",
            "skey": "00000000000000000000000000000000"
        },
        "async": false
    };

    bodyStr = JSON.stringify(json);

    httpPost("/api/", bodyStr, function (resJson) {

        $("#modalAddRobot").modal("hide");
        console.log(resJson);

        updateRobotList(getKeyword());
    });
}


function robotlogout(robotId) {
    json = {
        "api": "octlink.wcrobot.v1.robot.APILogOut",
        "paras": {
            "timeout": 0,
            "id": robotId
        },
        "session": {
            "uuid": "00000000000000000000000000000000",
            "skey": "00000000000000000000000000000000"
        },
        "async": false
    };

    bodyStr = JSON.stringify(json);

    httpPost("/api/", bodyStr, function (resJson) {
        $("#modalAddRobot").modal("hide");
        console.log(resJson);

        updateRobotList(getKeyword());

    });
}

function raiseAddModal() {

    $("#modalAddRobotCallback").click(function () {

        robotName = $("#robotName").val();
        uid = $("#uId").val();
        uname = $("#uName").val();

        json = {
            "api": "octlink.wcrobot.v1.robot.APIAddRobot",
            "paras": {
                "timeout": 0,
                "name": robotName,
                "uId": uid
            },
            "session": {
                "uuid": "00000000000000000000000000000000",
                "skey": "00000000000000000000000000000000"
            },
            "async": false
        };

        bodyStr = JSON.stringify(json);

        httpPost("/api/", bodyStr, function (resJson) {
            $("#modalAddRobot").modal("hide");
            updateRobotList(getKeyword());
        });
    });

    $("#modalAddRobot").modal("show");
}

function raiseUploadModal() {
    $("#modalUploadFile").modal("show");
}

function addRobot() {
    raiseAddModal();
}
