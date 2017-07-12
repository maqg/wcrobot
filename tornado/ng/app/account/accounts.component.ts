import {Component, OnInit} from "@angular/core";
import {AccountService} from "../service/account.service";
import {Router} from "@angular/router";
import {AlarmService} from "../service/alarm.service";

@Component({
    selector: 'my-accounts',
    templateUrl: './app/account/accounts.component.html',
   // styleUrls: ['./app/account/accounts.component.css']
})
export class AccountsComponent implements OnInit {

    accounts: Account[] = [];

    constructor(private accountService: AccountService,
                private router: Router, private alarmService: AlarmService) {
    }

    ngOnInit(): void {
        this.accountService.getAccounts().then(accounts => this.accounts = accounts);
    }

    delete(account: Account): void {
    }

    alarm(account: Account) {
        this.alarmService.showMsg("alarm", account.name);
    }

    gotoDetail(account: Account): void {
        this.router.navigate(["/accounts", account.id]);
    }

    gotoEditQuota(account: Account): void {
        let url = "/accounts/" + account.id + "/quota";
        this.router.navigate([url]);
    }

}