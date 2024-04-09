import { Component, AfterViewInit } from '@angular/core';
declare var componentHandler: any

@Component({
  selector: 'app-dash',
  templateUrl: './dash.component.html',
  styleUrls: ['./dash.component.scss']
})
export class DashComponent implements AfterViewInit{

  ngAfterViewInit(): void {
    componentHandler.upgradeAllRegistered();
  }
}
