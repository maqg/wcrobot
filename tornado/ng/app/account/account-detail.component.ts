import "rxjs/add/operator/switchMap";
import {Component, OnInit} from "@angular/core";
import {ActivatedRoute, Params} from "@angular/router";
import {Location} from "@angular/common";
import {AccountService} from "../service/account.service";


@Component({
    selector: 'account-detail',
    templateUrl: './app/account/account-detail.component.html',
})
export class AccountDetailComponent implements OnInit {

    account: Account;

    constructor(
        private accountService: AccountService,
        private route: ActivatedRoute,
        private location: Location
    ) { }

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.accountService.getAccount(params["id"]))
            .subscribe(account => this.account = account);
    }

    goBack(): void {
        this.location.back();
    }
}