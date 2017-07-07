import { DashboardComponent } from './dashboard/dashboard.component';
import { AccountService } from './service/account.service';
import { AppRoutingModule } from './app-routing.component';
import { AppComponent } from './app.component';
import { NgModule } from '@angular/core'
import { FormsModule }   from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser'

@NgModule({
    imports: [
        FormsModule,
        BrowserModule,
        AppRoutingModule
    ],

    declarations: [
        AppComponent,
        DashboardComponent
    ],

    providers: [
        AccountService
    ],

    bootstrap: [
        AppComponent
    ],
})
export class AppModule { }
