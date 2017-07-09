import "rxjs/add/operator/switchMap";
import {Component, OnInit} from "@angular/core";
import {ActivatedRoute, Params} from "@angular/router";
import {Location} from "@angular/common";
import {AccountService} from "../service/account.service";


@Component({
    selector: 'account-quota',
    templateUrl: './app/account/quota.component.html',
})
export class AccountQuotaComponent implements OnInit {

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