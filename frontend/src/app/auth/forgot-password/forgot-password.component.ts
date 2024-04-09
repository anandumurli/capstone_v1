import { Component, AfterViewInit } from '@angular/core';
declare var componentHandler: any

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})
export class ForgotPasswordComponent implements AfterViewInit{
  ngAfterViewInit(): void {
    componentHandler.upgradeAllRegistered();
  }
}
