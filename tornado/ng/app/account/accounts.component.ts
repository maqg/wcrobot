import { AccountService } from './../service/account.service';
import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'my-accounts',
    templateUrl: './app/account/accounts.component.html',
   // styleUrls: ['./app/account/accounts.component.css']
})
export class AccountsComponent implements OnInit {

    accounts: Account[] = [];

    constructor(private accountService: AccountService) { }

    ngOnInit(): void {
        this.accounts = this.accountService.getAccounts().slice(1, 5);
    }
}