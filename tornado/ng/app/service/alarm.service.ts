import {Injectable} from "@angular/core";

@Injectable()
export class AlarmService {

    private type: string;
    private show: boolean;
    private msg: string;

    constructor() {
        this.type = "alarm";
        this.show = false;
        this.msg = "none";
    }

    showMsg(type: string, msg: string) {
        this.type = type;
        this.msg = msg;
        this.show = true;
    }

    closeMsg() {
        this.msg = "";
        this.show = false;
    }

    getType() {
        return this.type;
    }


    getMsg() {
        return this.msg;
    }

    getShown() {
        return this.show;
    }
}