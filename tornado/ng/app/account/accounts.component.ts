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
        this.accounts = this.accountService.getAccounts().slice(1, 5);
    }

    delete(account: Account): void {

    }

    gotoDetail(account: Account): void {
        this.router.navigate(['/detail', account.id]);
    }

}