import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashRoutingModule } from './dash-routing.module';
import { DashComponent } from './dash.component';
import { LoadSheetComponent } from './load-sheet/load-sheet.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { AccountComponent } from './account/account.component';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    DashComponent,
    LoadSheetComponent,
    DashboardComponent,
    AccountComponent
  ],
  imports: [
    CommonModule,
    DashRoutingModule,
    HttpClientModule
  ]
})
export class DashModule { }
