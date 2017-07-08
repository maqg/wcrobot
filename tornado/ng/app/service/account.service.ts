import { Account } from './account';

import { Injectable } from "@angular/core";
import {Quota} from "./quota";

@Injectable()
export class AccountService {

    getAccounts(): Account[] {
        let accounts = [
            {
                id: "a01d4f96-62e3-11e7-8a52-525400659eb7",
                state: 1,
                name: "admin",
                email: "admin@octlink.com",
                lastSync: "2017-12-12 22:33:44",
                createTime: "2017-12-12 22:33:44",
                lastLogin: "2017-12-12 22:33:44",
                phoneNumber: "22011-33123-1312",
                desc: "Super Admin User",
                quota: new Quota(100)
            },
            {
                id: "b01d4f96-62e3-11e7-8a52-525400659eb7",
                state: 1,
                name: "henry",
                email: "henry@octlink.com",
                lastSync: "2017-12-12 22:33:44",
                createTime: "2017-12-12 22:33:44",
                lastLogin: "2017-12-12 22:33:44",
                phoneNumber: "22011-33123-1312",
                desc: "",
                quota: new Quota(200)
            },
            {
                id: "c01d4f96-62e3-11e7-8a52-525400659eb7",
                state: 1,
                name: "jacky",
                email: "jacky@octlink.com",
                lastSync: "2017-12-12 22:33:44",
                createTime: "2017-12-12 22:33:44",
                lastLogin: "2017-12-12 22:33:44",
                phoneNumber: "22011-33123-1312",
                desc: "Admin Account of Jacky",
                quota: new Quota(300)
            }                        
        ];
        return accounts;
    }
}