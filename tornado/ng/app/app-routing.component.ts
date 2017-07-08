import { DashboardComponent } from './dashboard/dashboard.component';
import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AccountsComponent} from "./account/accounts.component";

/*
const routes:Routes = [
    {path: '', redirectTo: '/dashboard', pathMatch: 'full'},
    {path: 'dashboard', component: DashboardComponent},
    {path: 'accounts', component: AccountsComponent},

];*/

const routes:Routes = [
    {path: '', component: DashboardComponent},
    {path: 'dashboard', component: DashboardComponent},
    // { path: 'login', component: LoginComponent },
    {
        path: 'home', component: DashboardComponent,
        children: [
            {path: '', redirectTo: '/home/user', pathMatch: 'full'},
            {path: 'accounts', component: AccountsComponent},
        ]
    },
    {path: "**", component: AccountsComponent}
];


@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {
}