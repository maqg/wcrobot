import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params, Router} from "@angular/router";
import {AccountService} from "../service/account.service";

@Component({
    selector: 'my-dashboard',
    templateUrl: './app/dashboard/dashboard.component.html',
    styleUrls: ['./app/dashboard/dashboard.component.css']
})
export class DashboardComponent implements OnInit {
    accounts: Account[] = [];

    constructor(private accountService: AccountService,
                private route: ActivatedRoute) { }

    ngOnInit(): void {
        this.accountService.getAccounts()
            .then(accounts => this.accounts = accounts.slice(1, 5));

  }
}