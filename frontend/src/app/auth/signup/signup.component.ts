import { AfterViewInit, Component } from '@angular/core';
declare var componentHandler: any
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements AfterViewInit{

  ngAfterViewInit(): void {
    componentHandler.upgradeAllRegistered();
  }

}
