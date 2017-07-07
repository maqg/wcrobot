import { AccountService } from './../service/account.service';
import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'my-dashboard',
    templateUrl: './app/dashboard/dashboard.component.html',
    styleUrls: ['./app/dashboard/dashboard.component.css']
})
export class DashboardComponent implements OnInit {

    accounts: Account[] = [];

    constructor(private accountService: AccountService) { }

    ngOnInit(): void {
        this.accounts = this.accountService.getAccounts().slice(1, 5);
    }
}