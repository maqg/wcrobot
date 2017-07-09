export class Quota {
    constructor(robots: number) {
        this.robots = robots;
        this.groups = 10;
        this.messages = 100;
        this.id = "dd";
    }
    id: string;
    robots: number;
    messages: number;
    groups: number;
}