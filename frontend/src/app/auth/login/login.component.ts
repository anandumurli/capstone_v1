import { Component, AfterViewInit } from '@angular/core';
declare var componentHandler: any

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements AfterViewInit {

  ngAfterViewInit(): void {
    componentHandler.upgradeAllRegistered();
  }

}
