import {Component, OnInit} from "@angular/core";
import {AccountService} from "../service/account.service";
import {Router} from "@angular/router";

@Component({
    selector: 'my-accounts',
    templateUrl: './app/account/accounts.component.html',
   // styleUrls: ['./app/account/accounts.component.css']
})
export class AccountsComponent implements OnInit {

    accounts: Account[] = [];

    constructor(private accountService: AccountService,
                private router: Router) {
    }

    ngOnInit(): void {
        this.accountService.getAccounts().then(accounts => this.accounts = accounts);
    }

    delete(account: Account): void {
    }

    gotoDetail(account: Account): void {
        this.router.navigate(["/accounts", account.id]);
    }

    gotoEditQuota(account: Account): void {
        this.router.navigate(["/accountquota", account.id])
    }

}