import {Component, DoCheck} from '@angular/core';
import {AlarmService} from "../service/alarm.service";

@Component({
    selector: "tundra-alarm",
    templateUrl: "./app/alarm/alarm.component.html",
    //styleUrls: ["./app/alarm/alarm.component.css"]
})
export class AlarmComponent {

    constructor(private service: AlarmService) {
    }

    getMsg(): string {
        return this.service.getMsg();
    }

    getType(): string {
        return this.service.getType();
    }

    isShow(): string {
        return this.service.getShown() ? "show" : "";
    }

    doClose(): void {
        //this.service.doConfirm('error');
    }
}