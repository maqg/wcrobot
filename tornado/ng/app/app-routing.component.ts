import { DashboardComponent } from './dashboard/dashboard.component';
import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AccountsComponent} from "./account/accounts.component";
import {AccountDetailComponent} from "./account/account-detail.component";
import {AccountQuotaComponent} from "./account/quota.component";
import {AlterComponent} from "./alter/alter.component";

const routes:Routes = [
    { path: "", redirectTo: "/dashboard", pathMatch: "full" },
    { path: "dashboard", component: DashboardComponent },
    { path: "alter", component: AlterComponent },
    {
        path: "accounts",
        children: [
            { path: "", component: AccountsComponent },
            { path: ":id", component: AccountDetailComponent },
            { path: ":id/quota", component: AccountQuotaComponent },
        ]
    }
];


@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {
}