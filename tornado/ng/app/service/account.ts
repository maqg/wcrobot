import {Quota} from "./quota";

export class Account {
    id: string;
    state: number;
    name: string;
    email: string;
    lastSync: string;
    createTime: string;
    lastLogin: string;
    phoneNumber: string;
    desc: string;

    quota: Quota;
}